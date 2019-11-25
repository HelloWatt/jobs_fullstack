from django.test import TestCase, Client as DjClient
from django.urls import reverse

from dashboard.models import Client


class DashBoardTestCase(TestCase):
    fixtures = ["prices", "clients", "consumptions"]


class HttpCodeTestCase(DashBoardTestCase):
    def setUp(self):
        self.djclient = DjClient()

    def assertSuccess(self, response, msg_prefix):
        status_code = response.status_code
        failure_msg = (
            msg_prefix and msg_prefix + " " or ""
        ) + f"expected success status code (200-299)"
        self.assertGreaterEqual(status_code, 200, failure_msg)
        self.assertLess(status_code, 300, failure_msg)

    def assertGet(self, path):
        response = self.djclient.get(path)
        self.assertSuccess(response, f"{path}")

    def assert404(self, path):
        response = self.djclient.get(path)
        self.assertEqual(response.status_code, 404)

    def test_clients_list_view(self):
        path = reverse("dashboard:clients_list")
        self.assertGet(path)

    def test_404_consumption_view(self):
        client_id = 0
        path = reverse("dashboard:consumption_details", kwargs={"client_id": client_id})
        self.assert404(path)

    def test_consumption_view(self):
        clients_ids = Client.objects.values_list("pk", flat=True)
        for cid in clients_ids:
            path = reverse("dashboard:consumption_details", kwargs={"client_id": cid})
            self.assertGet(path)
