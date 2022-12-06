from icecream import ic



def common_item(compartment1, compartment2) -> str:
    t1 = len(compartment1)
    t2 = len(compartment2)
    if t1 >= t2:
        for item in compartment1:
            if compartment2.find(item) != -1:
                return item
    else:
        return common_item(compartment2, compartment1)
    raise ValueError("common_item: rien trouvé !!")


def common_item_old(compartment1, compartment2) -> str:
    for item1 in compartment1:
        for item2 in compartment2:
            if item1 == item2:
                return item1
    raise ValueError("common_item: rien trouvé !!")


def common_items(compartment1, compartment2) -> str:
    items = ""
    for item1 in compartment1:
        for item2 in compartment2:
            if item1 == item2:
                items += item1
    return items


def common_item3(line1, line2, line3):
    c1 = common_items(line1, line2)
    return common_item(c1, line3)


def main():
    # file_data="exemple.txt"
    file_data="input.txt"

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
        # lire par groupe de 3 lignes
        # trouver l'eleme commun aux 3
        # sommer les elemnts trouvé

        # commons = []
        # prios_communs = []
        somme_prio = 0
        somme_prio_part2 = 0
        for i in range(0, len(rucksacks), 3):
            # ic(i)
            common = common_item3(
                rucksacks[i],
                rucksacks[i+1],
                rucksacks[i+2],
            )
            somme_prio_part2 += prios[common]

        for rucksack in rucksacks:
            taille = len(rucksack)
            compartment1 = rucksack[0: taille//2]
            compartment2 = rucksack[taille//2:taille]
            # ic(compartment1)
            # ic(compartment2)
            common = common_item(compartment1, compartment2)
            # ic(common)
            # common_old = common_item_old(compartment1, compartment2)
            # ic(common_old)

            # commons.append(common)
            # prios_communs.append(prios[common])
            somme_prio += prios[common]

        # ic(commons)
        # ic(prios_communs)
        print(f"part1: somme_prio = {somme_prio}")
        print(f"part2: somme_prio_part2 = {somme_prio_part2}")



if __name__ == "__main__":
        main()

        # import timeit
        # t = timeit.timeit()
        # s = "main()"
        # timeit.timeit(stmt=s, number=10)
        # print(timeit.timeit("main()") )#, setup="from __main__ import test"))



