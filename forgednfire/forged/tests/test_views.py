import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Forged
from ..serializers import ForgedSerializer

client = Client()




