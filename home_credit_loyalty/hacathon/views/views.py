from rest_framework import viewsets
from rest_framework.views import APIView
from hacathon.models import *
from hacathon.serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from hacathon.models import *
from hacathon.serializers import *
import json

#5178

@csrf_exempt
def authorize(request):
    if request.method == 'GET':
        try:
            email = request.GET.get('email', '')
            password = request.GET.get('password', '')
            print(email, password)
            user = Customer.objects.get(email=email, password=password)
            return JsonResponse({'code': 0, 'user': CustomerSerializer(user, many=False).data})
        except Exception as e:
            return JsonResponse({'code': 1, 'user': None})

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list_by_id(self, request, user_id):
        user = Customer.objects.get(pk=int(user_id))
        all_tasks = user.tasks.all()
        tasks = []

        for task in self.queryset:
            flag = False
            for intask in all_tasks:
                if (task==intask):
                    flag = True
                    break
            if (not flag):
                newtask = TaskSerializer(task,many=False).data
                tasks.append(newtask)
        return Response(tasks)

    def add_point(self, request, user_id, task_id):
        user = Customer.objects.get(pk=int(user_id))
        task = Task.objects.get(pk=int(task_id))
        user.tasks.add(task)
        user.current_points += task.bonus
        user.levelup_points += task.bonus
        user.completed_tasks += 1
        #history = History.create(type, datetime.datetime.now())
        #history.save()
        task.save()
        user.save()
        tasks = []
        for task in user.tasks.all():
            taskSerializer = TaskSerializer(task, many=False).data
            tasks.append(taskSerializer)

        customerserializer = CustomerSerializer(user)
        return Response([{'customer': customerserializer.data}, {'task': tasks}])

    def add_task(self, request):
        title = request.GET.get('title')
        body = request.GET.get('body')
        Task.objects.create(title=title, description=body, date=datetime.datetime.now(), type='Card' ,bonus=60, status="onprogress", donePercent=0)
        return Response({'code': 1})

def make_transaction(request, user_id, balance):
    user = Customer.objects.get(pk=user_id)
    user.current_points -= balance
    history = History.create('title_name', datetime.datetime.now(), 'payment')

    user.save()
    return JsonResponse({'code': 0})


class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, user_id):
        user = Customer.objects.get(pk=user_id)

        username = request.GET.get('cardholder')
        card_number = request.GET.get('card_number')
        expiration = request.GET.get('expiration_date')
        cvv = request.GET.get('cvv')

        ncard = Card.objects.create(card_number=card_number, username=username, expiration=expiration, cvv=cvv, customer=user)
        ncard.save()
        serializer = CardSerializer(ncard, many=False)
        return Response(serializer.data)
