import requests
book_data={
    "title":"To Mockingbird",
    "author":"Harper Lee",
    "pages":120,
    "publisher":"J. B. Lippincott & Co.",
    "published_date":"1960-07-11"
}

request=requests.put('http://127.0.0.1:8000/books/change_record/2?q=True',json=book_data)
print(request.status_code)
print(request.text)