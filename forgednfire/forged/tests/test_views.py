import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Forged
from ..serializers import ForgedSerializer

client = Client()

class GetAllForgedTest(TestCase):

    def setUp(self):
            Forged.objects.create(
                name='Katana', length=20, blade='sword', steelgrade='1050')
            Forged.objects.create(
                name='Hatchet', length=10, blade='axe', steelgrade='1040')
            Forged.objects.create(
                name='Sabre', length=24, blade='sword', steelgrade='2020')
            Forged.objects.create(
                name='Kabar', length=8, blade='knife', steelgrade='1040')    

    def test_get_all_forged(self):
        response = client.get(reverse('get_post_forged'))
        forged = Forged.objects.all()
        serializer = ForgedSerializer(forged, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleForgedTest(TestCase):

    def setUp(self):
            self.katana = Forged.objects.create(
                name='Katana', length=20, blade='sword', steelgrade='1050')
            self.hatchet = Forged.objects.create(
                name='Hatchet', length=10, blade='axe', steelgrade='1040')
            self.sabre = Forged.objects.create(
                name='Sabre', length=24, blade='sword', steelgrade='2020')
            self.kabar = Forged.objects.create(
                name='Kabar', length=8, blade='knife', steelgrade='1040')            

    def test_get_valid_single_forged(self):
        response = client.get(
            reverse('get_delete_update_forged', kwargs={'pk': self.katana.pk}))
        forged = Forged.objects.get(pk=self.katana.pk)
        serializer = ForgedSerializer(forged)    
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_forged(self):
        response = client.get(
            reverse('get_delete_update_forged', kwargs={'pk':30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   

class CreateNewForgedTest(TestCase):
    """ Test module for inserting a new forge """

    def setUp(self):
        self.valid_payload = {
            'name': 'Katana',
            'length': 20,
            'blade': 'sword',
            'steelgrade': '1050',
            
        }
        self.invalid_payload = {
            'name': '',
            'length': 12,
            'blade': 'axe',
            'steelgrade': '1040',
        } 

    def test_create_valid_forged(self):
        response = client.post(
            reverse('get_post_forged'),
            data=json.dumps(self.valid_payload),
            content_type= 'application/json'
        ) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     

    def test_create_invalid_forged(self):
        response = client.post(
            reverse('get_post_forged'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        ) 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)     