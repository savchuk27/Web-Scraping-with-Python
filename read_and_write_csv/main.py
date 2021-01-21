import csv


def write_csv(data):
    with open('names.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):
    with open('names2.csv', 'a') as f:
        order = ['name', 'surname','age']
        writer = csv.DictWriter(f,fieldnames= order)
        writer.writerow(data)


def main():
    d = {
        'name': "Petr",
        'surname' : "Ivanov",
        'age': 21
    }
    d1 = {
        'name': "Ivan",
        'surname': "Ivanov",
        'age': 26
    }
    d2 = {
        'name': "Oleg",
        'surname': "Petrov",
        'age': 23
    }

    l = [d,d1,d2]

    # for i in l:
    #     write_csv2(i)
    #
    with open('plugins.csv') as f:
        fieldnames = ['name', 'url', 'rating']
        reader = csv.DictReader(f, fieldnames=fieldnames)

        for row in reader:
            print(row)

if __name__ == '__main__':
    main()