import requests
book_data={
    'title':'The Great Gatsby',
    'author':'F. Scott Fitzgerald',
    'pages':180
}

request=requests.post('http://127.0.0.1:8000/books/create_record',json=book_data)
print(request.status_code)
print(request.text)