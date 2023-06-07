from django.contrib import admin

from .models import Messages, EmailIds

# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "email_id","message_box")
    
class EmailIdsAdmin(admin.ModelAdmin):
    list_display=("email_id",)

admin.site.register(Messages, MessagesAdmin)
admin.site.register(EmailIds, EmailIdsAdmin)
