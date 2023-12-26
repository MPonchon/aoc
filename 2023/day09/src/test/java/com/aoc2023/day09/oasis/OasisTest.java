package com.aoc2023.day09.oasis;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class OasisTest {

    @Test
    void nextNumber_from_Demo_line1_is_18() {
        //Given
        List<Integer> seq = List.of(0, 3, 6, 9, 12, 15);
        //When
        //Then
        assertEquals(18, Oasis.nextNumber(seq));
    }

    @Test
    void nextNumber_from_Demo_line2_is_28() {
        assertEquals(28, Oasis.nextNumber(List.of(1, 3, 6, 10, 15, 21 )));
    }    @Test
    void nextNumber_from_Demo_line2_is_68() {
        assertEquals(68, Oasis.nextNumber(List.of(10, 13, 16, 21, 30, 45)));
    }

    @Test
    void makeLine_return_line_of_3() {
        //Given
        List<Integer> seq = List.of(0, 3, 6, 9, 12, 15);
        //When
        //Then
        assertEquals(List.of(3, 3, 3, 3, 3), Oasis.makeLine(seq));
    }

    @Test
    void makeLine_second_line_return_line_of_0() {
        //Given
        List<Integer> seq = List.of(3, 3, 3, 3, 3);
        //When
        //Then
        assertEquals(List.of(0, 0, 0, 0), Oasis.makeLine(seq));
    }


    @Test
    void makeSum_demo_is_114() {
        List<List<Integer>> seq =List.of(
                List.of(0, 3, 6, 9, 12, 15),
                List.of(1, 3, 6, 10, 15, 21 ),
                List.of(10, 13, 16, 21, 30, 45));
        assertEquals(114, Oasis.makeSum(seq));
    }

    @Test
    void computeBackward() {
        assertEquals(5, Oasis.nextNumberBackward(List.of(10, 13, 16, 21, 30, 45) ));
        assertEquals(0, Oasis.nextNumberBackward(List.of(1, 3, 6, 10, 15, 21 )));
        assertEquals(-3, Oasis.nextNumberBackward(List.of(0, 3, 6, 9, 12, 15 )));
    }

    @Test
    void makeSumBackward_demo_is_2() {
        List<List<Integer>> seq =List.of(
                List.of(0, 3, 6, 9, 12, 15),
                List.of(1, 3, 6, 10, 15, 21 ),
                List.of(10, 13, 16, 21, 30, 45));
        assertEquals(2, Oasis.makeSumBackward(seq));
    }

}