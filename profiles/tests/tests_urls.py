from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import (
    profile)


class TestUrls(SimpleTestCase):

    def test_profile_url_is_resolves(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
