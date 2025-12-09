import requests 
request=requests.get('http://127.0.0.1:8000/books/get_record/1')
print(request.status_code)
print(request.text)