import json


def main():
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [[138, 164, 151], [125, 113, 113], [52, 50, 63]]
    most_wanted = dict(zip(names, production))

    with open("new_criminals.json") as json_data:
        new_criminals = json.load(json_data)
    print(criminals(most_wanted, new_criminals))

def criminals(most_wanted, new_criminals):
    for item in new_criminals:
        if item not in most_wanted:
           most_wanted[item] = new_criminals[item]
        else:
            most_wanted[item].extend(new_criminals[item])
    return most_wanted


if __name__ == '__main__':
   main()
