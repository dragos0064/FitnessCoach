import openai
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import json
from django.shortcuts import render


openai.api_key = settings.OPENAI_API_KEY  # Add your key in settings

@csrf_exempt
@api_view(['POST'])
def fitness_chat(request):
    user_message = request.data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a certified fitness coach. Give personalized, safe, science-based advice."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message["content"]
        return Response({"reply": reply})
    except Exception as e:
        return Response({"error": str(e)}, status=500)


def chat_page(request):
    return render(request, 'chat/index.html')