import json
import csv


with open('users.json', 'r') as user:
    data = json.load(user)
    with open('books.csv') as book:
        reader = csv.DictReader(book)
        for item, row in zip(data, reader):
            book_owner = {
                "name": item['name'],
                "gender": item['gender'],
                "address": item['address'],
                "books": [
                    {
                        "title": row['Title'],
                        "author": row['Author'],
                        "height": row['Height']
                    }
                ]
            }

            with open('book_owners.json', 'a') as file:
                person = json.dumps(book_owner, indent=2)
                file.write(person)
                file.write(',\n')
