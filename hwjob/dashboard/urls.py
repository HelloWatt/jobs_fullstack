from django.urls import path

from dashboard.views import consumption_view, search_client_view, search_by_name

app_name = "dashboard"
urlpatterns = [
    path("", search_client_view, name="search_client"),
    path(
        f"consumption/<int:client_id>",
        consumption_view,
        name="consumption_details",
    ),
    path("api/search-clients", search_by_name, name="search_by_name"),
]
