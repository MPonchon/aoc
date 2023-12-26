package com.aoc2023.day09;

import com.aoc2023.day09.oasis.Oasis;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class DayTest {
    private static Day day;
    @BeforeAll
    static void init() {
        day = new Day();
    }

    @Test
    void getPart1_input_is_1934898178() {
        assertEquals(1934898178, day.getPart1());
    }


    @Test
    void getPart2_input_is_1129() {
        assertEquals(1129, day.getPart2());
    }

}