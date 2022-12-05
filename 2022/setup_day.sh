#! /bin/env bash
day=$1
if [[ ${day:0:3} != "day" ]]; then
    echo "aoc : please issue a param that start whith 'day' !"
    exit 1
fi

cwd=$(pwd)
[[ "${cwd##*/aoc}" == "/2022" ]] || {
    echo "the path $cwd must be in /2022";
    exit 1;
}

aoc_dir="${cwd}/$1"
if [[ ! -d  ${aoc_dir} ]]; then
    mkdir "${aoc_dir}"
fi

cat << EOF >${aoc_dir}/main.py
#! /bin/env python3
#
# https://adventofcode.com/
#

from icecream import ic


def add_reponse(tag, reponse):
    import subprocess
    import os
    path_to_main = os.path.join(os.getcwd(), "main.py")
    if os.path.exists(path_to_main):
        command = f"sed -i 's/# {tag}.*$/# {tag}: {reponse}/g' {path_to_main}"
        subprocess.run(command, shell=True)
    else:
        ic(f"Erreur chemin: {path_to_main}")


def main():
    # reponse1 = 0
    # reponse2 = 0

    file_data = "exemple.txt"
    # file_data = "input.txt"
    
    with open(file_data, 'r') as f:
        lines = [line.strip("\n") for line in f.readlines()]

    return reponse1, reponse2


if __name__ == "__main__":
    reponse1, reponse2 = main()
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")
    add_reponse("reponse part1", reponse1)
    add_reponse("reponse part2", reponse2)

# -----------------------------
# reponse part1
# reponse part2
EOF

touch ${aoc_dir}/exemple.txt
touch ${aoc_dir}/input.txt
