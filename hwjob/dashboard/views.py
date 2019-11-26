from django.shortcuts import render

def consumption_view(request, client_id):
    return render(request, "dashboard/consumption_detail.html")

def search_client_view(request):
    """
        A list of clients

        TODO client.has_elec_heating should be set
        TODO client.has_anomaly should be set
    """
    return render(request, "dashboard/search_client.html")
