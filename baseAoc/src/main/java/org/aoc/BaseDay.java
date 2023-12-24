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

    BaseDay(int day) {
        this.day = day;
    }

    public String title() {
        return  String.format("""
            AdventOfCode day: %d
            ----------------------
            """, day);
    }
    public void run() {
        StringBuilder sb = new StringBuilder();
//        sb.append("AdventOfCode day: ").append(day).append("\n");
        sb.append(title());
        sb.append("Part 1:\n");
        sb.append("- demo: ").append(demoPart1).append("\n");
        sb.append("- result: ").append(part1).append("\n\n");
        sb.append("Part 2:\n");
        sb.append("- demo: ").append(demoPart2).append("\n");
        sb.append("- result: ").append(part2).append("\n");
        System.out.println(sb);
    }

}
