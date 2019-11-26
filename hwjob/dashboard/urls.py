from django.urls import path

from dashboard.views import consumption_view, search_client_view


app_name = "dashboard"
urlpatterns = [
    path("", search_client_view, name="search_client"),
    path(
        f"consumption/<int:client_id>",
        consumption_view,
        name="consumption_details",
    ),
]
