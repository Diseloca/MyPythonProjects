M = ["january", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
     "noviembre", "diciembre"]


def validate_input(day, month):
    if day > 31:
        print("Error day greater than 31")
        exit(0)

    if month not in M:
        print("Error invalid month")
        exit(0)

    # months with 30 days
    if (month in ("abril", "junio", "septiembre", "noviembre")) and day > 30:
        print(month, "has not day", day)
        exit(0)

    if month == "febrero" and day > 29:
        print("Error dia de febrero mayor que 29")
        exit(0)


def get_sign(day, month):
    if (month == "january" and day >= 21) or (month == "febrero" and day <= 19):
        sign = "Acuario"
    elif month == "febrero" or (month == "marzo" and day <= 20):
        sign = "Piscis"
    elif month == "marzo" or (month == "abril" and day <= 20):
        sign = "Aries"
    elif month == "abril" or (month == "mayo" and day <= 20):
        sign = "Tauro"
    elif month == "mayo" or (month == "junio" and day <= 21):
        sign = "Geminis"
    elif month == "junio" or (month == "julio" and day <= 22):
        sign = "Cancer"
    elif month == "julio" or (month == "agosto" and day <= 23):
        sign = "Leo"
    elif month == "agosto" or (month == "septiembre" and day <= 22):
        sign = "Virgo"
    elif month == "septiembre" or (month == "octubre" and day <= 22):
        sign = "Libra"
    elif month == "octubre" or (month == "noviembre" and day <= 22):
        sign = "Escorpio"
    elif month == "noviembre" or (month == "diciembre" and day <= 21):
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
