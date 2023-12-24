package org.aoc;


//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        BaseDay<String, String> baseDay =  new BaseDay<>(15);
        baseDay.setDemoPart1("demo part1 1");
        baseDay.setPart1("part1 10");
        baseDay.setPart2("part2 20");
        baseDay.setDemoPart1("demo part2 20");

        baseDay.run();
    }
}