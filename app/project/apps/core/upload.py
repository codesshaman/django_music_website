from django.core.validators import FileExtensionValidator
from django import forms
import os


def handle_uploaded_file(f):
    file_path = os.path.join("media", "music", f.name)
    with open(file_path, "wb+") as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    return file_path


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Выберите аудио файл", 
    validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'aac', 'ogg'])])
