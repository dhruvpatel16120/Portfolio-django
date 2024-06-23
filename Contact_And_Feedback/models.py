from django.db import models

# Create your models here.
class ContactAndFeedBacks(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)
    email_send_status = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"