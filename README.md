# WorkCRM - Personal Task & Client Management System

A Django-based CRM and task management system built for Akro Ventures.

## Features

✅ **Multi-user support** - Separate workspaces for Akshita and Rohit
✅ **Task Management** - Create, track, and complete tasks with priorities
✅ **Client Database** - Store client information and link to tasks
✅ **Work Logging** - Track hours and productivity
✅ **Smart Dashboard** - See urgent, overdue, and today's tasks at a glance
✅ **Motivational Push** - Get reminded to GET TO WORK! 💪
✅ **Priority System** - Urgent, High, Medium, Low priorities
✅ **Status Tracking** - To Do, In Progress, Waiting, Done

## Login Credentials

**Akshita:**
- Username: `akshita`
- Password: `akshita123`

**Rohit:**
- Username: `rohit`
- Password: `rohit123`

## How to Run

```bash
cd /home/claude/workcrm
python manage.py runserver 0.0.0.0:8000
```

Then open your browser to: http://localhost:8000

## Quick Start

1. Login with your credentials
2. View your dashboard to see task overview
3. Create tasks with priorities and due dates
4. Add clients to your database
5. Log your work hours
6. Mark tasks as complete when done!

## Dashboard Features

- **Completion Rate** - See your productivity percentage
- **Urgent Tasks** - Tasks marked as URGENT that need immediate attention
- **Overdue Tasks** - Stop procrastinating! See what you missed
- **Today's Tasks** - Focus on what's due today
- **Recent Work Logs** - Track your recent activity

## Motivation System

Your dashboard will push you based on completion rate:
- 80%+ → "🔥 You're crushing it!"
- 60-79% → "💪 Great progress!"
- 40-59% → "⚡ You can do better!"
- <40% → "🚨 TIME TO GET TO WORK! No more excuses!"

## Task Priorities

- **Urgent** - Red badge, shows at top of dashboard
- **High** - Orange badge
- **Medium** - Blue badge  
- **Low** - Gray badge

## Password Change

To change passwords, run:
```bash
python manage.py changepassword akshita
# or
python manage.py changepassword rohit
```

Built with Django 6.0 and lots of caffeine ☕
