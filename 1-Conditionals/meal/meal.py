def main():
    userinput = input("What time is it? ")
    convertedtime = convert(userinput)

    if convertedtime >= 7 and convertedtime <= 8:
        print("It's breakfast time")
    elif convertedtime >= 12 and convertedtime <= 13:
        print("It's lunch time")
    elif convertedtime >= 18 and convertedtime <= 19:
        print("It's dinner time")


def convert(time):
    time = time.split(":")
    time[0] = float(time[0])
    time[1] = float(time[1])
    return (time[0]) + (time[1] / 60)


if __name__ == "__main__":
    main()
