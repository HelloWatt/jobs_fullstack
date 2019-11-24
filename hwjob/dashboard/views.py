from django.views import View
from django.views.generic.list import ListView

from dashboard.models import Client


class ClientsListView(ListView):
    """
        A list of clients

        TODO client.has_elec_heating should be set
        TODO client.has_anomaly should be set
    """

    queryset = Client.objects.all()
    context_object_name = "clients_list"
    template_name = "dashboard/clients_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = {
            "title": "Clients list",
            "description": "Browse which clients has an electrical heating or an anomaly",
        }
        return context


class ConsumptionView(View):
    """
        A detailed dashboard about a client's consumption
    """

    template = "dashboard/consumption_detail.html"
