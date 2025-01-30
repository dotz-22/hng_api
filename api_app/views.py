from django.http import JsonResponse
from django.utils.timezone import now
import datetime

# Create your views here.

def Json_details_View(request):
    data = {
        "email": "babarindesheriff@gmail.com.com",
        "current_datetime": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/dotz-22/hng_api"
    }
    return JsonResponse(data)

