from django.contrib.auth.models import User

# Create users
akshita, created = User.objects.get_or_create(
    username='akshita',
    defaults={
        'email': 'akshita@akroventures.com',
        'first_name': 'Akshita',
        'is_staff': True,
    }
)
if created:
    akshita.set_password('akshita123')
    akshita.save()
    print("Created user: akshita (password: akshita123)")
else:
    print("User akshita already exists")

rohit, created = User.objects.get_or_create(
    username='rohit',
    defaults={
        'email': 'rohit@akroventures.com',
        'first_name': 'Rohit',
        'is_staff': True,
    }
)
if created:
    rohit.set_password('rohit123')
    rohit.save()
    print("Created user: rohit (password: rohit123)")
else:
    print("User rohit already exists")

print("\n✅ Setup complete!")
print("Login credentials:")
print("  Akshita - username: akshita, password: akshita123")
print("  Rohit   - username: rohit, password: rohit123")
