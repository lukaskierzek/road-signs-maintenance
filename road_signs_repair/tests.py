from django.test import TestCase
from .models import Region


# Create your tests here.

class RegionTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self) -> None:
        Region.objects.create(name="Oswiecim city")

    def tearDown(self) -> None:
        pass

    def test_name_max_length(self):
        region = Region.objects.get(id=1)
        max_length = region._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_help_text_label(self):
        region = Region.objects.get(id=1)
        help_text = region._meta.get_field('name').help_text
        expected_help_text = 'Enter the name of the region where there may be road signs'
        self.assertEqual(help_text, expected_help_text)

    def test_object_name_is_name(self):
        region = Region.objects.get(id=1)
        expected_object_name = region.name
        self.assertEqual(str(region), expected_object_name)

    def test_verbose_name_label(self):
        region = Region.objects.get(id=1)
        verbose_name = 'names'
        expected_verbose_name = region._meta.get_field('name').verbose_name
        self.assertEqual(verbose_name, expected_verbose_name)
