import requests
book_data={
    "title":"Pride and Prejudice",
    "author":"Jane Austen",
    "pages":279,
    "publisher":"T. Egerton, Whitehall",
    "published_date":"1813-01-28"
}


request=requests.post('http://127.0.0.1:8000/books/create_record',json=book_data)
print(request.status_code)
print(request.text)
