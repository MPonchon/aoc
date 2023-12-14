package com.aoc2013.day04.cards;

import org.junit.jupiter.api.Test;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class CardsTest {

    @Test
    void worthPoints_demo_is_13() {
        //Given
        List<List<List<Integer>>>  allnumbers = Cards.loadData("src/main/resources/demo.txt");
        List<List<Integer>> winnings = allnumbers.get(0);
        List<List<Integer>> numbers = allnumbers.get(1);

        //When
        int points = Cards.worthPoints(winnings, numbers);

        //Then
        assertEquals(13, points);
    }

    @Test
    void loadData_demo_return_2_lists() {
        //Given
        //When
        List<List<List<Integer>>>  allnumbers = Cards.loadData("src/main/resources/demo.txt");

        //Then
        assertEquals(2, allnumbers.size());
        assertEquals(List.of(41,48,83,86,17), allnumbers.get(0).get(0));
        assertEquals(List.of(13,32,20,16,61), allnumbers.get(0).get(1));
    }
}