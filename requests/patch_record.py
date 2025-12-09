import requests
request=requests.patch('http://127.0.0.1:8000/books/update_record/2?title=To%20Kill%20a%20Mockingbird&pages=324')
print(request.status_code)
print(request.text)