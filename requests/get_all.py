import requests 
request=requests.get('http://127.0.0.1:8000/books/get_records')
print(request.status_code)
print(request.text)