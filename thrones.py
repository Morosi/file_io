import csv

houses = []

with open("GoT.csv") as file:
    reader = csv.DictReader(file, fieldnames=["house", "words", "head"])
    next(reader)
    for row in reader:
        houses.append(
            {"house": row["house"], "words": row["words"], "head": row["head"]}
        )

for house in sorted(houses, key=lambda house: house["house"]):
    print(f"house {house['house']}, says: {house['words']}, leader: {house['head']}")
