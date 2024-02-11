import requests
import sys

ALLOWED_EXTENSIONS = ['mp3', 'wav', 'aac', 'ogg']

if len(sys.argv) > 1 and sys.argv[1] == 'list':
    resp = requests.get("http://localhost:8888/api/music/")
    # Reading as text
    print(resp.text)
elif len(sys.argv) > 2 and sys.argv[1] == 'upload':
    file_path = sys.argv[2]
    file_extension = file_path.split('.')[-1].lower()

    if file_extension in ALLOWED_EXTENSIONS:
        print(file_path)
        r = requests.post('http://localhost:8888/api/upload/',
                          files={'file': open(file_path, 'rb')})
        print(r.content)
    else:
        print("Расширение файла не поддерживается. Разрешенные расширения: mp3, wav, aac, ogg.")
