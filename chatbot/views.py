import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

DEEPSEEK_API_KEY = "sk-439c958fbb11413aab79fedcf68efbeb"

def chatbot_view(request):
    return render(request, 'chatbot/chatbot.html')

@csrf_exempt
def get_chat_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()

        if not user_message:
            return JsonResponse({"response": "Please enter a message."}, status=400)

        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": user_message}]
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()

            # Handle insufficient balance error
            if "error" in response_data and response_data["error"].get("code") == "invalid_request_error":
                return JsonResponse({"response": "Sorry, the chatbot service is currently unavailable due to insufficient balance."})

            if "choices" in response_data and len(response_data["choices"]) > 0:
                bot_reply = response_data["choices"][0]["message"]["content"]
            else:
                bot_reply = "I couldn't understand that. Try again."

            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"response": "Invalid request method"}, status=405)
