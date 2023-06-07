from django.urls import path, include
from .views import message_view, message_post, homepage, fetch_all_emails,post_email

urlpatterns = [
     path("", homepage, name="homepage"),
     path('alldetails/', message_view, name='home-page-view'),
     path("postdetails/", message_post, name='home-page-post'),
     path("allemails/", fetch_all_emails, name='fetch-all-emails'),
     path("postemail/", post_email, name='post-email'),
]
