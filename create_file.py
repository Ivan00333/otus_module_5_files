import json
import csv
from files import CSV_FILE_PATH, JSON_FILE_PATH


with open(JSON_FILE_PATH, 'r') as f:
    user = json.load(f)
    keys_to_extract = ["name", "gender", "address", "age"]

    users = [{key: d[key] for key in keys_to_extract}for d in user]

with open(CSV_FILE_PATH, newline='') as csvfile:
    book = csv.reader(csvfile)
    header = [column.lower() for column in next(book)]

    books = [dict(zip(header, row)) for row in book]

for user in users:
    user["books"] = []

user_count = len(users)
for i, book in enumerate(books):
    user_index = i % user_count
    users[user_index]["books"].append(book)

with open('files/reference.json', 'w') as file:
    json.dump(users, file, indent=4)
