import csv

total = -1

with open('teste.csv', 'r') as new_file:
    csv_reader = csv.reader(new_file, delimiter=";")

    for line in csv_reader:
        total += 1
    
    print("Total de Serviços: {}" .format(total))