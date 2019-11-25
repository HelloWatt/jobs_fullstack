from django.urls import path

from dashboard.views import ClientsListView, ConsumptionView


app_name = "dashboard"
urlpatterns = [
<<<<<<< HEAD
    path("", ClientsListView.as_view(), name="clients_list"),
    path(
        f"consumption/<int:client_id>",
        ConsumptionView.as_view(),
        name="consumption_details",
    ),
=======
    path('', ClientsListView.as_view(), name="clients_list"),
    path(f"{_('consumption')}/<int:client_id>", ConsumptionView.as_view(), name="consumption_details")
>>>>>>> 1df5eef... Rename paths
]
