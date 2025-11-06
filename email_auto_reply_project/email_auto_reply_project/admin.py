from django.contrib import admin
from .models import InquiryUser, EmailInquiry, InquiryQuestion

# Register your models here.
admin.site.register(EmailInquiry)
admin.site.register(InquiryQuestion)
admin.site.register(InquiryUser)
