from django.db import models

class InquiryUser(models.Model):
    name = models.CharField(max_length=200, default="guest user")
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class EmailInquiry(models.Model):
    user = models.ForeignKey(
        InquiryUser, on_delete=models.CASCADE,
        null=True, blank=True, default=None
    )
    email_content = models.TextField()
    inquiry_timestamp = models.DateTimeField(auto_now_add=True)

class InquiryQuestion(models.Model):
    email_inquiry = models.ForeignKey(
        EmailInquiry, on_delete=models.CASCADE,
        null=True, blank=True, default=None
    )
    question = models.TextField()
    answer = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.question)
