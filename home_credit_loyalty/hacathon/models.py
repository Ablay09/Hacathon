from django.db import models
from django.contrib.auth.models import User
import datetime

class Customer(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=15)
    current_points = models.IntegerField(default=0)
    levelup_points = models.IntegerField(default=0)
    completed_tasks = models.IntegerField(default=0)
    rank = models.CharField(max_length=255, default='')
    tasks = models.ManyToManyField('Task', null=True, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=250)
    date = models.CharField(max_length=1000)
    TYPE_CHOICES = (
        ('tel', 'Tel'),
        ('card', 'Card'),
        ('bug', 'Bug'),
        ('evaluate', 'Evaluate'),
        ('feedback', 'Feedback'),
        ('question', 'Question'),
        ('transaction', 'Transaction'),
        ('recommend', 'Recommend'),
    )
    type = models.CharField(max_length=1000, choices=TYPE_CHOICES)
    description = models.CharField(max_length=1000)
    bonus = models.IntegerField(default=0)
    status = models.CharField(max_length=500)
    donePercent = models.IntegerField(default=0)

    @classmethod
    def create(cls, title, body):
        task = cls(title=title, date=datetime.datetime.now(), type='Card', description=body,bonus=60,status="onprogress",donePercent=0)
        return task

    def __str__(self):
        return self.title

class History(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(datetime.datetime.now())
    payment = models.CharField(max_length=255)
    #from_field = models.CharField(max_length=50)
    #to_field = models.CharField(max_length=50)

    @classmethod
    def create(cls, title, date, payment):
        history = cls(title=title, date=date, payment=payment)
        return history

class Card(models.Model):
    card_number = models.CharField(max_length=16, null=True)
    cvv = models.CharField(max_length=3, null=True)
    username = models.CharField(max_length=255, null=True)
    expiration = models.CharField(max_length=255, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
'''

class Onai(models.Model):
    type_of_card = models.CharField(max_length=255)
    digits = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

class Phone(models.Model):
    tel_number = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    type = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


'''
