from django.test import TestCase

# Create your tests here.
from taggy.apps.tagging.models import Taggable


class TaggableTests(TestCase):

    def test_str(self):
        taggable = Taggable(name='Test')

        self.assertEquals(
            str(taggable),
            'Test',
        )