from django.urls import path

from .views import GetCSVFileDataView, UploadFileView

app_name = "core"

urlpatterns = [
    path("", UploadFileView.as_view(), name="file"),
    path("get-csv-file-data/", GetCSVFileDataView.as_view(), name="get-csv-file-data"),
]
