months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

date = input("Please enter a date:\n").replace(",", "")


try:
    # Determine whether the inputted date is formatted as "MM/DD/YYYY" or
    # "MONTH DD, YYYY" and split
    if "/" in date:
        date = date.split("/")
        print(date[2].rjust(2, "0"), date[1].rjust(2, "0"), date[0], sep="-")
    else:
        date = date.split(" ")
        print(
            date[2].rjust(4, "0"),
            date[1].rjust(2, "0"),
            str(months.index(date[0]) + 1).rjust(2, "0"),
            sep="-",
        )
except (TypeError, ValueError):
    print("Invalid date")


#    elif (  # Handle "MONTH DD, YYYY" input
#        int(date.replace(",", "").split(" ")[1]) <= 31
#        and int(date.replace(",", "").split(" ")[1]) > 0
#    ):
#
#        date = date.replace(",", "").split(" ")
#
#        print(  # Print justified date in correct order
#           date[2].rjust(4, "0"),
#          str(months.index(date[0])).rjust(2, "0"),
#         date[1].rjust(2, "0"),
#        sep="-",
# )
