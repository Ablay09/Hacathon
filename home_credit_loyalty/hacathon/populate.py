
import django
import os


if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_credit_loyalty.settings')
    django.setup()
    from hacathon.models import Customer, Task

    user = Customer.objects.get(pk=1)
    user.tasks.add(Task.objects.get(pk=2))
    user.tasks.add(Task.objects.get(pk=3))
    user.save()
    print(user.tasks.all())