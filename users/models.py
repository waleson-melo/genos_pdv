from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.pessoa import Pessoa


class User(AbstractUser, Pessoa):
    pass
