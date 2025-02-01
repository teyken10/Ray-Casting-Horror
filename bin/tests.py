with open('../resources/maps/first_floor.txt', 'r', encoding='utf-8') as f:
    first_floor = [row.rstrip() for row in f.readlines()]

for j, row in enumerate(first_floor):
    for i, char in enumerate(row):
        print(char == '1', end=', ')
    print()
