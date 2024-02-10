from .upload import handle_uploaded_file, UploadFileForm
from django.shortcuts import render
from django.conf import settings
import os


# Create your views here.
def home(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    music_dir = os.path.join(settings.BASE_DIR, 'media', 'music')
    music_files = os.listdir(music_dir)
    indexed = list(enumerate(music_files))
    template = 'index.html'
    context = {
        'title': 'Python Bootcamp Day 05 ex01',
        'music_files': indexed,
        'form': form
    }
    return render(request, template, context)
