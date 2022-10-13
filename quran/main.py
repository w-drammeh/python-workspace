from random import randint


index = {
    1: "Fatiha",
    2: "Baqarah",
    3: "Ali Imran",
    4: "Nisa",
    5: "Maidah",
    6: "Anham",
    7: "Ahraf",
    8: "Anfal",
    9: "Tawbah",
    10: "Yunus",
    11: "Hud",
    12: "Yusuf",
    13: "Rahd",
    14: "Ibrahim",
    15: "Hijr",
    16: "Nahl",
    17: "Isra",
    18: "Kahf",
    19: "Maryam",
    20: "Ta-Ha",
    21: "Anbiyah",
    22: "Hajj",
    23: "Muhminun",
    24: "Nur",
    25: "Furqan",
    26: "Shuharah",
    27: "Naml",
    28: "Qasas",
    29: "Ankabut",
    30: "Rum",
    31: "Luqman",
    32: "Sajdah",
    33: "Ahzab",
    34: "Saba",
    35: "Fatir",
    36: "Ya-Seen",
    37: "Saffat",
    38: "Saad",
    39: "Zumur",
    40: "Ghafir",
    41: "Fussilat",
    42: "Shurah",
    43: "Zukhruf",
    44: "Dukhan",
    45: "Jasiyah",
    46: "Ahqaf",
    47: "Muhammad",
    48: "Fath",
    49: "Hujurat",
    50: "Qaf",
    51: "Dhariyat",
    52: "Tur",
    53: "Najm",
    54: "Qamar",
    55: "Rahman",
    56: "Waqihah",
    57: "Hadid",
    58: "Mujadilah",
    59: "Hashr",
    60: "Mumtahana",
    61: "Saff",
    62: "Jumuhah",
    63: "Munafiqun",
    64: "Taghabun",
    65: "Talaq",
    66: "Tahrim",
    67: "Mulk",
    68: "Qalam", # Nuhn
    69: "Haqqah",
    70: "Mahrij",
    71: "Nuh",
    72: "Jin",
    73: "Muzzammil",
    74: "Muddathir",
    75: "Qiyamah",
    76: "Insan", # Dhar
    77: "Mursalat",
    78: "Nabah",
    79: "Naziat",
    80: "Abasa",
    81: "Takwir",
    82: "Infitar",
    83: "Mutaffifin",
    84: "Inshiqaq",
    85: "Buruj",
    86: "Tariq",
    87: "Ahla",
    88: "Ghasiyah",
    89: "Fajr",
    90: "Balad",
    91: "Shams",
    92: "Layl",
    93: "Duhaa",
    94: "Sharha",
    95: "Tin",
    96: "Alaq", # Iqrah
    97: "Qadr",
    98: "Bayyinah",
    99: "Zalzalah",
    100: "Adiyat",
    101: "Qhariah",
    102: "Takathur",
    103: "Asr",
    104: "Humazah",
    105: "Fil",
    106: "Quraysh",
    107: "Mahun",
    108: "Kawthar",
    109: "Kafirun",
    110: "Nasr",
    111: "Masad", # Lahab
    112: "Ikhlas",
    113: "Falaq",
    114: "Nas"
}

length = len(index)

def indexToName():
    print("Welcome to the Quranic Indexing Exercise!\nFor this exercise, a random surah number will be generated. Will you know its name?\n")

    shown = []
    correct = 0
    i = 1
    while i <= length:
        j = randint(1, length)
        if j in shown:
            continue
        else:
            shown.append(j)

        answer = input(f"{i}. What's the name of surah number {j}: ")

        if answer == index[j]:
            correct += 1
            print(True)
        else:
            print(False)
        
        i += 1

    printResult(correct, length)


def nameToIndex():
    print("Welcome to the Quranic Indexing Exercise!\nFor this exercise, a random surah name will be generated. Will you know its index?\n")

    shown = []
    correct = 0
    i = 1
    while i <= length:
        j = randint(1, len(index))
        if j in shown:
            continue
        else:
            shown.append(j)

        name = index[j]

        answer = int(input(f"{i}. What's the index of Surah {name}: "))

        if answer == j:
            correct += 1
            print(True)
        else:
            print(False)
        
        i += 1

    printResult(correct, length)


def printResult(correct, total):
    percent = round((correct/total) * 100)
    print(f"\nFinal score: {correct}/{total} [{percent}%]")


if __name__ == "__main__":
    # indexToName()
    nameToIndex()