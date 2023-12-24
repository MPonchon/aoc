package org.aoc;

import lombok.*;

//@NoArgsConstructor
@Getter
@Setter
//@AllArgsConstructor
public class BaseDay<T, U> {

    @Setter(AccessLevel.NONE)
    private int day;

    private T demoPart1;
    private T part1;

    private U demoPart2;
    private U part2;

    public BaseDay(int day) {
        this.day = day;
    }

    public String title() {
        return  String.format("""
            AdventOfCode day: %d
            ----------------------
            """, day);
    }
    public String getPart(int n) {
        return new StringBuilder()
                .append("- demo: ")
                .append(n == 1 ? getDemoPart1(): getDemoPart2())
                .append("\n")
                .append("- result: ")
                .append(n == 1 ? getPart1(): getPart2())
                .append("\n")
                .toString();
    }
    public void run() {
        StringBuilder sb = new StringBuilder()
                .append(title())
                .append("Part 1:\n")
                .append(getPart(1))
                .append("\nPart 2:\n")
                .append(getPart(2));

        System.out.println(sb);
    }

}
