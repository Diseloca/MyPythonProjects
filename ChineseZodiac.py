SIGNS = {
    0: "monkey", 1: "rooster", 2: "dog", 3: "pig",
    4: "rat", 5: "ox", 6: "tiger", 7: "rabbit",
    8: "dragon", 9: "snake", 10: "horse", 11: "goat"
}

print("Your sign is:", SIGNS.get(int(input("Introduce your birth year [YYYY]: ")) % 12))
