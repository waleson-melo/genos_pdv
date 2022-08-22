from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.pessoa import Pessoa


class User(AbstractUser, Pessoa):
    def __str__(self):
        return "{} ({})".format(self.first_name, self.last_name)
