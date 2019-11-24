from django.urls import path

from dashboard.views import ClientsListView, ConsumptionView


app_name = "dashboard"
urlpatterns = [
    path("", ClientsListView.as_view(), name="clients_list"),
    path(
        f"consumption/<int:client_id>",
        ConsumptionView.as_view(),
        name="consumption_details",
    ),
]
