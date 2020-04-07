from django.db import models
import uuid
from api.apps.accounts.models import Company, Client, User

# Create your models here.

class Inquiry(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name="inquiry_company")
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                                related_name="inquiry_client")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="inquiry_user")
    description = models.TextField(blank=True, null=True)
    inquirystatus = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'inquiries'
