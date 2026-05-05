from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from datetime import datetime, timedelta
from .models import Task, Client, Reminder, WorkLog

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'tracker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    user = request.user
    
    # Get tasks
    my_tasks = Task.objects.filter(assigned_to=user)
    urgent_tasks = my_tasks.filter(priority='urgent', status__in=['todo', 'in_progress'])
    overdue_tasks = [task for task in my_tasks if task.is_overdue()]
    today_tasks = my_tasks.filter(
        due_date__date=timezone.now().date(),
        status__in=['todo', 'in_progress']
    )
    
    # Get stats
    total_tasks = my_tasks.count()
    completed_tasks = my_tasks.filter(status='done').count()
    in_progress = my_tasks.filter(status='in_progress').count()
    
    # Recent work logs
    recent_logs = WorkLog.objects.filter(user=user)[:5]
    
    # Get motivational message
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    if completion_rate >= 80:
        motivation = "🔥 You're crushing it! Keep the momentum going!"
    elif completion_rate >= 60:
        motivation = "💪 Great progress! Push a bit harder!"
    elif completion_rate >= 40:
        motivation = "⚡ You can do better! Let's finish those tasks!"
    else:
        motivation = "🚨 TIME TO GET TO WORK! No more excuses!"
    
    context = {
        'urgent_tasks': urgent_tasks,
        'overdue_tasks': overdue_tasks,
        'today_tasks': today_tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress': in_progress,
        'completion_rate': round(completion_rate, 1),
        'motivation': motivation,
        'recent_logs': recent_logs,
    }
    
    return render(request, 'tracker/dashboard.html', context)

@login_required
def task_list(request):
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    
    tasks = Task.objects.filter(assigned_to=request.user)
    
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    
    context = {
        'tasks': tasks,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    }
    
    return render(request, 'tracker/task_list.html', context)

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        client_id = request.POST.get('client')
        
        task = Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            assigned_to=request.user,
            due_date=due_date if due_date else None,
            client_id=client_id if client_id else None,
        )
        
        messages.success(request, f'Task "{title}" created! Now get to work! 💪')
        return redirect('task_list')
    
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'tracker/task_create.html', {'clients': clients})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        task.due_date = due_date if due_date else None
        
        if task.status == 'done' and not task.completed_at:
            task.completed_at = timezone.now()
            messages.success(request, f'🎉 Task completed! You did it!')
        
        task.save()
        messages.success(request, 'Task updated!')
        return redirect('task_list')
    
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'tracker/task_update.html', {'task': task, 'clients': clients})

@login_required
def client_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'tracker/client_list.html', {'clients': clients})

@login_required
def client_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        notes = request.POST.get('notes')
        
        Client.objects.create(
            name=name,
            company=company,
            email=email,
            phone=phone,
            notes=notes,
            created_by=request.user,
        )
        
        messages.success(request, f'Client "{name}" added!')
        return redirect('client_list')
    
    return render(request, 'tracker/client_create.html')

@login_required
def worklog_create(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        hours = request.POST.get('hours')
        date = request.POST.get('date')
        task_id = request.POST.get('task')
        
        WorkLog.objects.create(
            user=request.user,
            description=description,
            hours_worked=hours,
            date=date,
            task_id=task_id if task_id else None,
        )
        
        messages.success(request, 'Work logged! Keep it up! 💪')
        return redirect('dashboard')
    
    tasks = Task.objects.filter(assigned_to=request.user, status__in=['todo', 'in_progress'])
    return render(request, 'tracker/worklog_create.html', {'tasks': tasks})

