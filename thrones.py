houses = []
    
with open("GoT.csv") as file:
        for line in file:
            house_name, words = line.rstrip().split(",")
            house = {"house": house_name, "words": words}
            houses.append(house)
def get_house(family):
    return family["house"]
    

for house in sorted(houses, key=get_house, reverse=True):
    print(f"house: {house['house']}, words: {house['words']}")
