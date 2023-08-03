from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from dashboard.models import Client


def consumption_view(request, client_id):
    client = Client.objects.get(id=client_id)
    # TODO
    context = {
        "client": client
    }
    return render(request, "dashboard/consumption_detail.html", context)


def search_client_view(request):
    return render(request, "dashboard/search_client.html")


def search_by_name(request):
    """
    This view search a client and return a list of clients matching requests.
    """
    if request.method == "GET":
        query = request.GET.get("query")
        if not query:
            return HttpResponseBadRequest()
        clients_q = Client.objects.filter(
            full_name__icontains=query
        ).values("id", "full_name")[:10]
        return JsonResponse(
            {
                "matches": list(clients_q),
            }
        )

    return HttpResponseNotAllowed(["GET"])
