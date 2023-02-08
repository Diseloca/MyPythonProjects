meses = {
    0: "mono", 1: "gallo", 2: "perro", 3: "cerdo",
    4: "rata", 5: "buey", 6: "tigre", 7: "conejo",
    8: "dragon", 9: "serpiente", 10: "caballo", 11: "cabra"
}


def getsign(year, d):
    n = year % 12
    return d.get(n)


def main():
    year = int(input("Introduce tu fecha de nacimineto [YYYY]: "))
    sign = getsign(year, meses)
    print("Tu signo es:", sign)


main()
