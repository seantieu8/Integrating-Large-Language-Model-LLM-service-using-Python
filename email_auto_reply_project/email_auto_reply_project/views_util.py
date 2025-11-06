import re
from . import llm_util
from . import model_util
from . import views

def extract_receiver_name(email_content: str):

    # greetings = ["Hi", "Hello", "Dear", "Mr." + "Miss", "Mrs.", "Dr."]
    # pattern = r"\b(" + "|".join(greetings) + r")\s+(\w+)"
    # match = re.search(pattern, email_content, re.IGNORECASE)
    # return match.group(2) if match else None
    receiver_name = llm_util.extract_sender_and_receiver_names(email_content)[1]

    if(receiver_name == "N/A"):
        return None
    else:
        return receiver_name

def extract_sender_name(email_content: str):
    # closing_phrases = ["Regards,", "Cheers,", "Thanks,", "Best,", "Sincerely,", "Yours,"]
    # pattern = r"\b(" + "|".join(re.escape(phrase) for phrase in closing_phrases) + r")\s*(\w+)"

    #match = re.search(pattern, email_content, re.IGNORECASE)

    sender_name = llm_util.extract_sender_and_receiver_names(email_content)[0]

    if(sender_name == "N/A"):
        return None
    else:
        return sender_name

def extract_inquiry_question(email_content, email, name):
    inquiry_questions = llm_util.extract_sender_and_receiver_names(email_content)[2]
    model_util.save_inquiry_question(inquiry_questions, email_content, email, name)
    return inquiry_questions
