combinaisonPart1 = {
    "A X": 4,    "B X": 1,    "C X": 7,
    "A Y": 8,    "B Y": 5,    "C Y": 2,
    "A Z": 3,    "B Z": 9,    "C Z": 6
}

combinaisonPart2 = {
    "A X": 3,    "B X": 1,    "C X": 2,
    "A Y": 4,    "B Y": 5,    "C Y": 6,
    "A Z": 8,    "B Z": 9,    "C Z": 7
}

with open("input01.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

couples = [i.split(" ") for i in data]
map(combinaisonPart1.get(combi), )
couple = [i for i in couples]
print(f'couple: >{couple}<')


resultatPart1 = 0
resultatPart2 = 0
for i in range(len(couple)):
    combi = f"{couple[i][0]} {couple[i][1]}"
    resultatPart1 += combinaisonPart1.get(combi)  # type: ignore
    resultatPart2 += combinaisonPart2.get(combi)  # type: ignore

print(f"Résultat part1 : {resultatPart1}\nRésultat part2 : {resultatPart2}")
