from django.test import TestCase
from ..models import Forged


class ForgedTest(TestCase):

    def setUp(self):
        Forged.objects.create(
            name='Katana', length=3, blade='sword', steelgrade='1050')
        Forged.objects.create(
            name='Hatchet', length=1, blade='axe', steelgrade='1040')

    def test_forged_blade_type(self):
        katana = Forged.objects.get(name = 'Katana')
        hatchet = Forged.objects.get(name = 'Hatchet')
        self.assertEqual(
            katana.get_blade_type(), "Katana's are in the sword family"
        )
        self.assertEqual(
            hatchet.get_blade_type(), "Hatchet's are in the axe family"
        )
