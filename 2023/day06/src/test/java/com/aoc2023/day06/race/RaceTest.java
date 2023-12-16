package com.aoc2023.day06.race;

import org.apache.commons.lang3.tuple.Pair;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class RaceTest {

    @Test
    void loadRaces_should_return_data_from_file() {
        //Given
        List<Pair<Integer, Integer>> data = Race.loadRaces("src/main/resources/demo.txt");
        //When

        //Then
        assertEquals(3, data.size());
        assertEquals(7, data.get(0).getLeft());
        assertEquals(9, data.get(0).getRight());

    }

    @Test
    void nbWinnings_demo() {
        //Given
        //When
        //Then
        assertEquals(4, Race.nbWinnings(7, 9));
        assertEquals(8, Race.nbWinnings(15, 40));
        assertEquals(9, Race.nbWinnings(30, 200));
    }

    @Test
    void part1_demo() {
        assertEquals(288, Race.part1("src/main/resources/demo.txt"));
    }
}