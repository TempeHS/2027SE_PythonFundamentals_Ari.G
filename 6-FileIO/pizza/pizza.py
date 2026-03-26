import sys
import tabulate
import csv

if len(sys.argv) == 2:

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        read_file = []
        for row in reader:
            read_file.append(row)
    print(tabulate.tabulate(read_file, headers="firstrow", tablefmt="grid"))

else:
    print("Please use 1 argument\n")
