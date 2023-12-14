package com.aoc2013.day04.part2;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CopyCardsTest {

    @Test
    void totalScratchcards_demo_return_30() {
        assertEquals(30, CopyCards.totalScratchcards("src/main/resources/demo.txt"));
    }
}