import pandas as pd
from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework import generics

from core.forms import FileUploadForm
from core.models import File
from core.serializers import GetCSVFileDataSerializer


class UploadFileView(FormView):
    template_name = "upload_csv.html"
    form_class = FileUploadForm
    __doc__ = "this api is used to get the data from csv and store in our database"

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            file = form.files["file"]
            try:
                reader = pd.read_csv(file)
                File.objects.bulk_create(
                    [
                        File(**data)
                        for data in reader.to_dict("records")
                        if not File.objects.filter(title=data.get("title")).exists()
                    ]
                )
            except Exception as e:
                return render(
                    request,
                    self.template_name,
                    {"message_type": "failure", "message": str(e)},
                )
            return render(
                request,
                self.template_name,
                {"message_type": "success", "message": "file uplaoded successfully"},
            )
        return render(
            request,
            self.template_name,
            {"message_type": "failure", "message": form.errors},
        )


class GetCSVFileDataView(generics.ListAPIView):
    serializer_class = GetCSVFileDataSerializer
    queryset = File.objects.all()
    __doc__ = "this api is used to return the data in json response"
