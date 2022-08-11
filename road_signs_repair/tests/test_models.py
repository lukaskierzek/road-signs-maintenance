from django.test import TestCase
from road_signs_repair.models import Region, Locality


# Create your tests here.

class RegionTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.region = Region.objects.create(name="Oswiecim city")
        cls.region_with_long_name = Region.objects.create(name="""
                A very long name of region A very long name of region A very long name of region A very long name of region 
                """)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_name_max_length(self):
        max_length = self.region._meta.get_field('name').max_length
        max_length_for_name = 100
        self.assertEqual(max_length, max_length_for_name)

    def test_name_greater_than_max_length(self):
        name_length = len(self.region_with_long_name.name)
        max_length = self.region._meta.get_field('name').max_length
        self.assertGreater(name_length, max_length)

    def test_help_text_label(self):
        help_text = self.region._meta.get_field('name').help_text
        expected_help_text = 'Enter the name of the region where there may be road signs'
        self.assertEqual(help_text, expected_help_text)

    def test_object_name_is_name(self):
        str_region_name = str(self.region)
        expected_object_name = self.region.name
        self.assertEqual(str_region_name, expected_object_name)

    def test_verbose_name_label(self):
        verbose_name = 'Region name'
        expected_verbose_name = self.region._meta.get_field('name').verbose_name
        self.assertEqual(verbose_name, expected_verbose_name)

    def test_ordering_meta_class(self):
        ordering = ['name']
        expected_ordering = self.region._meta.ordering
        self.assertEqual(ordering, expected_ordering)

    def test_verbose_name_plural_meta_class(self):
        verbose_name_plural = 'Regions'
        expected_verbose_name_plural = self.region._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, expected_verbose_name_plural)

    def test_db_table_name_meta_class(self):
        db_table_name = 'region'
        expected_db_table = self.region._meta.db_table
        self.assertEqual(db_table_name, expected_db_table)


class LocalityTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.region = Region.objects.create(name='Oswiecim')
        cls.locality = Locality.objects.create(name='Main street',
                                               region_id=1)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_name_max_length(self):
        max_length = self.locality._meta.get_field('name').max_length
        max_length_for_name = 100
        self.assertEqual(max_length, max_length_for_name)

    def test_name_help_text_label(self):
        help_text = self.locality._meta.get_field('name').help_text
        expected_help_text = 'Enter the name of locality where there may be road sign'
        self.assertEqual(help_text, expected_help_text)

    def test_verbose_name_label(self):
        verbose_name = self.locality._meta.get_field('name').verbose_name
        expected_verbose_name = 'Locality name'
        self.assertEqual(verbose_name, expected_verbose_name)

    def test_object_name_is_name(self):
        str_name = str(self.locality)
        expected_object_name = self.locality.name
        self.assertEqual(str_name, expected_object_name)

    def test_region_foreign_key(self):
        region_name_from_locality = self.locality.region.name
        region_name = self.region.name
        self.assertEqual(region_name_from_locality, region_name)

    # TODO: test on_delete and other classes
