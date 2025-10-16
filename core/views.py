from django.shortcuts import render
import requests
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ProfileView(APIView):
    def get(self, request):
        try:
            response = requests.get("https://catfact.ninja/fact", timeout=5)
            if 200 <= response.status_code < 300:
                cat_fact = response.json().get("fact")
            else:
                raise requests.RequestException
                
        except requests.RequestException:
            cat_fact = "Could not get cat facts at the moment"
        
        data = {
            "status": "success",
            "user": {
                "email": "okumborfranklin@gmail.com",
                "name": "Okumbor Abraham Franklin (Franklin07)",
                "stack": "Python/Django"
            },
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fact": cat_fact
        }

        return Response(data)