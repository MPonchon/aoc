from icecream import ic

def common_item(compartment1, compartment2)  -> str:
    for item1 in compartment1:
        for item2 in compartment2:
            if item1 == item2:
                return item1
    raise ValueError("common_item: rien trouvé !!")


def main():
    file_data="exemple.txt"
    # file_data="input.txt"

    prios = {}
    for i in range(0, 26):
        # print(chr(i+65))
        # print(chr(i+97))
        prios[chr(i+97)] = i + 1

    for i in range(0, 26):
        prios[chr(i+65)] = i + 27



    with open(file_data , 'r') as f:
        rucksacks = [line.strip("\n")  for line in f.readlines()]
        # algo:
        # separer la ligne en 2 parts egales
        # trouve l'element commun
        # donner sa priorité
        # faire la somme des priorités

        # commons = []
        # prios_communs = []
        somme_prio = 0
        for rucksack in rucksacks:
            taille = len(rucksack)
            compartment1 = rucksack[0: taille//2]
            compartment2 = rucksack[taille//2:taille]
            # ic(compartment1)
            # ic(compartment2)
            common = common_item(compartment1, compartment2)
            # commons.append(common)
            # prios_communs.append(prios[common])
            somme_prio += prios[common]
            # ic(common)
        # ic(commons)
        # ic(prios_communs)
        print(f"part1: somme = {somme_prio}")



if __name__ == "__main__":
        main()



