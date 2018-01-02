import csv 

def read_rolls():
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            read_roll(row)


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    del row[name]

    print("Roll: {}".format(name))
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        print(" * {} will default {}? {}".format(name, k, can_defeat))

    print()

read_rolls()