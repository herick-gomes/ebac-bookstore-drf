from django.apps import apps
from django.test import SimpleTestCase


class ConfiguracaoDRFTests(SimpleTestCase):

    def test_rest_framework_instalado(self):
        self.assertTrue(
            apps.is_installed("rest_framework")
        )

    def test_admin_disponivel(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)
