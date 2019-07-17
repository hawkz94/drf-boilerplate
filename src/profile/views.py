from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from utils import notifications
from .tasks import send_sms
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Profile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import ProfileSerializer
from rest_framework.decorators import (
    action, parser_classes, authentication_classes, permission_classes
)
from django.contrib.auth.hashers import make_password

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = Profile.objects.get(user_id=token.user_id)
        return Response({'token': token.key, 'id': token.user_id, 'typeUser': user.typeUser})

class ProfileViewSet(viewsets.ModelViewSet):
    lookup_field = 'user_id'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['POST'], detail=False)
    def create_profile(self, request):
        user = User.objects.create(
            email = request.data['email'],
            username = request.data['username'],
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            password = make_password(request.data['password']),
        )

        profile = Profile.objects.create(
            user = user,
            age = 0,
            typeUser = request.data['typeUser'],
            referralCode = request.data['referralCode']
        )

        user_dict = model_to_dict(user)
        profile_dict = model_to_dict(profile, ['typeUser', 'referralCode'])
        user_dict.update(profile_dict)

        send_sms.delay(request.data['username'], request.data['referralCode'])

        return Response(user_dict, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def valid_register(self, request):
        pk = request.data['userId']
        referral_code = request.data['referralCode']
        user = Profile.objects.get(user_id=pk, referralCode=referral_code)
        if(user):
            user.mobileVerified = True
            user.save()
            return Response({'msg': 'Ok'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'something bad happened'}, status=status.HTTP_404_NOT_FOUND)