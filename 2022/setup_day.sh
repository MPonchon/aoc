#! /bin/env bash
day=$1
if [[ ${day:0:3} != "day" ]]; then
    echo "aoc : param must start whith 'day' !"
    exit
fi

cwd=$(pwd)
[[ "${cwd##*/aoc}" == "/2022" ]] || {
    echo "$cwd pas bon";
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

def main():
    file_data="exemple.txt"
    # file_data="input.txt"
    
    with open(file_data , 'r') as f:
        lines = [line.strip("\n")  for line in f.readlines()]

    reponse1 = 0
    reponse2 = 0
    print(f"reponse part1:{reponse1}")
    print(f"reponse part2:{reponse2}")

if __name__ == "__main__":
        main()
EOF

touch ${aoc_dir}/exemple.txt
touch ${aoc_dir}/input.txt
