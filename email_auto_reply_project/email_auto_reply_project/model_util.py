from . import models
from . import views

def retrieve_all_inquiry_questions():
    all_inquiry_questions = models.InquiryQuestion.objects.all() # type: ignore
    return all_inquiry_questions

def save_inquiry_question(questions: list[str], email_content: str, email:str, name:str | None = None):
    user = models.InquiryUser(email=email, name=name)
    email_inquiry = models.EmailInquiry(email_content=email_content, user=user)
    user.save()
    email_inquiry.save()

    for question in questions:
        inquiry_question = models.InquiryQuestion(
            question=question,
            email_inquiry=email_inquiry
        )
        inquiry_question.save()

    return email_inquiry
