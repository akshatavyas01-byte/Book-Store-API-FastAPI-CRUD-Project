import requests
request=requests.delete('http://127.0.0.1:8000/books/delete_record/2?q=True')
print(request)
print(request.text)