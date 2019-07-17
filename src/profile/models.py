from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    gender = models.BooleanField(null=True)
    emailVerified = models.BooleanField(null=True)
    status = models.TextField(null=True)
    documentNumber = models.TextField(null=True)
    documentNumberType = models.TextField(null=True)
    photoProfile = models.TextField(null=True)
    photoCover = models.TextField(null=True)
    birthday = models.DateField(null=True)
    typeUser = models.TextField(null=True)
    blood = models.TextField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    createdAt = models.DateField(null=True)
    createdBy = models.IntegerField(null=True)
    updatedAt = models.DateField(null=True)
    updatedBy = models.IntegerField(null=True)
    mobile = models.TextField(null=True)
    mobileVerified = models.BooleanField(null=True)
    referralCode = models.TextField(null=True)
    isVirtual = models.BooleanField(null=True)