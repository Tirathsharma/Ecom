from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .Serializers import UserSerializers
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
# Create your views here.
import re
import random

def generate_session_token(length=20):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(10))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'send a post request with valid parameter'})

    username=request.POST['email']
    Password=request.POST['Password']

    if not re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",username):
        return JsonResponse({'error':'enter a valid email'})
    
    if len(password)<3:
        return JsonResponse({'error':'password require for more then three'})
    
    UserModel = get_user_model()

    try:
        user=UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict=UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')

            if user.session_token !="0":
                user.session_token="0"
                user.sava()
                return JsonResponse({'error':'previos session exists'})
            toke=generate_session_token()
            user.session_token-token
            user.save()
            logi(request,user)
            return JsonResponse({'token':token, 'user': usr_dict})
        else:
            return JsonResponse({'error':'invalid email'})
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'invalid email'})

def signout(request,id):
    logout(request)

    UserModel=get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token="0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'invalid ID'})
    return JsonResponse({'success':'logout success'})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset=CustomUser.objects.all().order_by('id')
    serializer_class=UserSerializers

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]