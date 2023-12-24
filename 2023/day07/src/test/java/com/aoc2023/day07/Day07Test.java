package com.aoc2023.day07;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day07Test {

    @Test
    void sortHands() {
        List<String> hands = new ArrayList<>(List.of("3KA", "2KK"));

        Day07.sortHands(hands);
        System.out.println("hands " + hands);
    }
}