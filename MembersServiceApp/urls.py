from django.conf.urls import url
from MembersServiceApp.views import ListMembers, CSVUpload

urlpatterns = {
    url('^members/', ListMembers.as_view(), name="members"),
    url(r'^upload_csv/$', CSVUpload.as_view(), name="upload_csv")
}

