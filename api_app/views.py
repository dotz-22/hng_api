from django.http import JsonResponse
from django.utils.timezone import now

# Create your views here.

def Json_details_View(request):
    data = {
        "email": "babarindesheriff@gmail.com.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/dotz-22/hng_api.git"
    }
    return JsonResponse(data)

