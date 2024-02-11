from .upload import handle_uploaded_file, UploadFileForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from django.conf import settings
import os


music_dir = os.path.join(settings.BASE_DIR, 'media', 'music')
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
    music_files = os.listdir(music_dir)
    indexed = list(enumerate(music_files))
    template = 'index.html'
    context = {
        'title': 'Python Bootcamp Day 05 ex01',
        'music_files': indexed,
        'form': form
    }
    return render(request, template, context)


def music(request):
    music_list = os.listdir(music_dir)
    return JsonResponse({'files': music_list},
    json_dumps_params={'ensure_ascii': False, 'indent': 4}, charset='utf-8')


# class FileUploadAPIView(APIView):
#     def post(self, request):
#         file = request.FILES.get('file')
#         if file:
#             file_path = default_storage.save(f'/media/music/{file.name}', ContentFile(file.read()))
#             return Response({'file_path': file_path}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

class FileUploadAPIView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if file:
            file_path = default_storage.save(f'music/{file.name}', ContentFile(file.read()))
            return Response({'file_path': file_path}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
