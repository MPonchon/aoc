package com.aoc2023.day07;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day07Test {

    @Test
    void sortHands() {
        List<String> hands = new ArrayList<>(List.of("3KA", "2KK"));
        Day07 day07 = new Day07();
        day07.cardValues = Day07.cardValues1;
        day07.sortHands(hands, day07.handComparatorP1);
        System.out.println("hands " + hands);
    }

    @Test
    void getDemoPart1() {
        Day07 day07 = new Day07();
        assertEquals(6440, day07.getDemoPart1());
    }

    @Test
    void getPart1() {
        Day07 day07 = new Day07();
        assertEquals(250951660, day07.getPart1());
    }

    @Test
    void getDemoPart2() {
        Day07 day07 = new Day07();
        assertEquals(5905, day07.getDemoPart2());
    }

    @Test
    void getPart2() {
        Day07 day07 = new Day07();
        assertEquals(251481660, day07.getPart2());
    }
}