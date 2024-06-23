from django.contrib import admin
from Contact_And_Feedback.models import ContactAndFeedBacks

# Register your models here.
class ContactUAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submit_date', 'email_send_status')
    list_filter = ('submit_date', 'email_send_status')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('submit_date',)

admin.site.register(ContactAndFeedBacks,ContactUAdmin)