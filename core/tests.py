from django.test import TestCase

from django.urls import reverse


class SampleTestCase(TestCase):

    def test_reverse(self):
        # Test with some example data
        print(reverse('get-vehicle-status', kwargs={'data': 'UID%3A%20BF%20B1%2066%201F'}))
