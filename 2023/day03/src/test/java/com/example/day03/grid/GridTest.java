package com.example.day03.grid;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;
@SpringBootTest
public class GridTest {
    @Test
    void find_numbers_adjentSymbol(){
        // Given
        List<String> lines = new ArrayList<>();
        lines.add("467.");
        lines.add("*..*");

        // When
        Coord result = Grid.symbolAround(lines, null);

        //Then
        assertNotNull(result);

    }

    @Test
    void find_numbers_adjentSymbol_3lines(){
        // Given
        List<String> lines = new ArrayList<>();
        lines.add("....");
        lines.add("467.");
        lines.add("..&.");

        // When
        Coord result = Grid.symbolAround(lines, null);

        //Then
        assertNotNull(result);
    }

    @Test
    void getAdjacentNumbers_return_467() {
        // Given
        List<String> lines = new ArrayList<>();
        lines.add("467..114");
        lines.add("...*....");

        // When
        List<Integer> numbers = Grid.getAdjacentNumbers(lines);

        //Then
        assertTrue(numbers.contains(467));
    }


    @Test
    void find_Gears_in_Window3lines(){
        // Given
        List<String> lines = new ArrayList<>();
        lines.add("467..114..");
        lines.add("...*......");
        lines.add("..35..633.");

        // When
        List<Integer> numbers = Grid.findGearsInWindow(lines);

        //Then
        assertTrue(numbers.contains(467));
        assertTrue(numbers.contains(35));
        assertFalse(numbers.contains(114));
        assertFalse(numbers.contains(633));
    }
}