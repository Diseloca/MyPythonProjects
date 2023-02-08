M = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
     "november", "december"]


def validate_input(day, month):
    if day > 31:
        print("Error day greater than 31")
        exit(0)

    if month not in M:
        print("Error invalid month")
        exit(0)

    # months with 30 days
    if (month in ("april", "june", "september", "november")) and day > 30:
        print(month, "has not day", day)
        exit(0)

    if month == "february" and day > 29:
        print("Error dia de february mayr que 29")
        exit(0)


def get_sign(day, month):
    if (month == "january" and day >= 21) or (month == "february" and day <= 19):
        sign = "Acuario"
    elif month == "february" or (month == "march" and day <= 20):
        sign = "Piscis"
    elif month == "march" or (month == "april" and day <= 20):
        sign = "Aries"
    elif month == "april" or (month == "may" and day <= 20):
        sign = "Tauro"
    elif month == "may" or (month == "june" and day <= 21):
        sign = "Geminis"
    elif month == "june" or (month == "july" and day <= 22):
        sign = "Cancer"
    elif month == "july" or (month == "august" and day <= 23):
        sign = "Leo"
    elif month == "august" or (month == "september" and day <= 22):
        sign = "Virgo"
    elif month == "september" or (month == "october" and day <= 22):
        sign = "Libra"
    elif month == "october" or (month == "november" and day <= 22):
        sign = "Escorpio"
    elif month == "november" or (month == "december" and day <= 21):
        sign = "Sagitario"
    else:
        sign = "Capricornio"

    return sign


def main():
    day = int(input("Introduce your birth day [0-31]: "))
    month = str(input("Introduce your birth month [text]: "))

    validate_input(day, month)
    print("Your sign is:", get_sign(day, month))


main()
