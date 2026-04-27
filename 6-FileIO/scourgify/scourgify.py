import sys
import csv

if len(sys.argv) == 3:
    try:  # Open the first file (input)
        with open(sys.argv[1]) as file1:
            pass
    except FileNotFoundError:
        sys.exit("Please enter valid files")

    try:  # Open the second file (output)
        with open(sys.argv[2]) as file2:
            pass
    except FileNotFoundError:
        sys.exit("Please enter valid files")
else:
    sys.exit("Please enter 2 arguments")
