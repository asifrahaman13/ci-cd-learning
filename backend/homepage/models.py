from django.db import models

# Create your models here.


class Messages(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email_id=models.EmailField(max_length=120)
    message_box=models.CharField(max_length=256)

    def __str__(self):
        return "Data of "+ self.first_name + "Email address: " +self.email_id

class EmailIds(models.Model):
    email_id=models.CharField(max_length=120)

    def __str__(self):
        return self.email_id

    