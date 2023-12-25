package com.aoc2023.day08;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day08Test {

    @Test
    void getPart2() {
        Day08 day = new Day08(8);
        assertEquals(17099847107071, day.getPart2());
    }
}