import sys

if len(sys.argv) == 2:
    file = sys.argv[1]
    if file.endswith(".csv"):
        sys.exit()

    linecount = 0

    try:
        file = open(file)
    except:
        sys.exit()

    for line in file:
        if line.lstrip().startswith("#") or line.lstrip() == "":
            pass
        else:
            linecount += 1

    print(linecount)

else:
    sys.exit()
