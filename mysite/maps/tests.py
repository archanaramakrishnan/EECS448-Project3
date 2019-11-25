from django.test import TestCase

# Create your tests here.
from maps.models import Building, Map

class BuildingTestCase(TestCase):
    
    def setUpMaps(self):
        Building.objects.create(name="Budig Hall", latitude="38.958312", longitude="-95.249133")
        Building.objects.create(name="Wescoe Hall", latitude="38.957712", longitude="-95.247629")
        Building.objects.create(name="LEEP2", latitude="38.957726", longitude="-95.254068")

        Map.objects.create(building1="LEEP2", building2="Wescoe")

    def test_created_maps_form(self):
        """
        Method `__str__` should be equal to field `name` and field `latitude` and `longitude` should be set correctly
        """
        f1 = Map.objects.get(building1="LEEP2")
        self.assertEqual(str(f1), f1.building1)
        print("PASSED: 'LEEP2' form created")
    
    def test_created_buildings(self):
        """
        Method `__str__` should be equal to field `name` and field `latitude` and `longitude` should be set correctly
        """
        b1 = Building.objects.get(name="Budig Hall")
        self.assertEqual(str(b1), b1.name)
        self.assertEqual(38.958312, b1.latitude)
        self.assertEqual(-95.249133, b1.longitude)
        print("PASSED: 'Budig Hall' object created in Building class")

        b2 = Building.objects.get(name="Wescoe Hall")
        self.assertEqual(str(b2), b2.name)
        self.assertEqual(38.957712, b2.latitude)
        self.assertEqual(-95.247629, b2.longitude)
        print("PASSED: 'Wescoe Hall' object created in Building class")

        b3 = Building.objects.get(name="LEEP2")
        self.assertEqual(str(b3), b3.name)
        self.assertEqual(38.957726, b3.latitude)
        self.assertEqual(-95.254068, b3.longitude)
        print("PASSED: 'LEEP2' object created in Building class")