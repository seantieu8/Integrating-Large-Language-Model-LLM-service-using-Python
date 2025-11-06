import json
import re

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import views_util
from . import model_util
from . import models


def home(request):
    # return HttpResponse("Hello, Build Follows!")
    # return render(request, 'home.html')
    all_inquiry_questions = model_util.retrieve_all_inquiry_questions()
    return render(request, 'auto_reply_inquiry_questions.html', {'inquiry_questions': all_inquiry_questions})

@csrf_exempt
def auto_reply_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email_content = data.get("paragraph", "")
            email_address = data.get("email", "")
            print(email_address)

            receiver_name = views_util.extract_receiver_name(email_content)
            sender_name = views_util.extract_sender_name(email_content)

            print(receiver_name)
            print(sender_name)

            extracted_questions_list = views_util.extract_inquiry_question(email_content, email_address, sender_name if sender_name else None)
            inquiry_question_display = "\n".join(extracted_questions_list) if extracted_questions_list else None

            # Construct reply message
            if sender_name and receiver_name:
                reply_message = f"Hi {sender_name}, \n\n thanks for your email, I will get back to you soon. \n\n Best, {receiver_name}."
            else:
                print(f"Could not extract sender or receiver names from content. Sender: {sender_name}, Receiver: {receiver_name}")
                reply_message = "Hi there, thanks for the email. I will get back to you soon."

            return JsonResponse(
                {
                    'reply': reply_message,
                    'status': 'success',
                    'receiver_name': receiver_name,
                    'sender_name': sender_name,
                    'inquiry_question': inquiry_question_display, # Use the formatted string

                }
            )

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format', 'status': 'failure'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed', 'status': 'failure'}, status=405)
