package com.example.day03.grid;

import com.example.day03.dir.Direction;
import com.example.day03.utils.Utils;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

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
        boolean result = Grid.symbolAround(lines);

        //Then
        assertTrue(result);

    }

    @Test
    void find_numbers_adjentSymbol_3lines(){
        // Given
        List<String> lines = new ArrayList<>();
        lines.add("....");
        lines.add("467.");
        lines.add("..&.");

        // When
        boolean result = Grid.symbolAround(lines);

        //Then
        assertTrue(result);
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
    void getStarAroundNumber_return_star_position() {
        // Given
        Map<Integer, List<Integer>> stars = new HashMap<>();
        List<String> lines = new ArrayList<>();
        lines.add("467..114");
        lines.add("...*....");
        lines.add("..35.633.");

        // When
        List<Integer> starAndNumbers = Grid.getNumbersAroundStar(lines, 1, stars);

        //Then
        assertEquals(11, starAndNumbers.get(0));
        assertEquals(Integer.valueOf(467), starAndNumbers.get(1));
        assertEquals(Integer.valueOf(35), starAndNumbers.get(2));
    }

    @Test
    void getNumber_left_is_617() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("617*......");
        //When
        Integer n = Grid.getNumber(lines, 0, 3, Direction.LEFT);
        //Then
        assertEquals(Integer.valueOf(617), n);
    }
    @Test
    void getNumber_right_is_618() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("......*618");
        //When
        Integer n = Grid.getNumber(lines, 0, 6, Direction.RIGHT);
        //Then
        assertEquals(Integer.valueOf(618), n);
    }

    @Test
    void getNumber_UP_right_is_619() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...45..619");
        lines.add("......*618");
        //When
        Integer n = Grid.getNumber(lines, 1, 6, Direction.UP);
        //Then
        assertEquals(Integer.valueOf(619), n);
    }

    @Test
    void getNumber_UP_right_is_600() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...600..89");
        lines.add("......*618");
        //When
        Integer n = Grid.getNumber(lines, 1, 6, Direction.UP);
        //Then
        assertEquals(Integer.valueOf(600), n);
    }

    @Test
    void getNumber_UP_right_isnull() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...60...89");
        lines.add("......*618");
        //When
        Integer n = Grid.getNumber(lines, 1, 6, Direction.UP);
        //Then
        assertNull(n);
    }
    /*
            ...123..234..345..456..567.
            ..*.....*.....*.....*.....*
     */
    @Test
    void getNumber_DOWN_right_is_601() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...600..89");
        lines.add("......*618");
        lines.add("...601..89");
        //When
        Integer n = Grid.getNumber(lines, 1, 6, Direction.DOWN);
        //Then
        assertEquals(Integer.valueOf(601), n);
    }

    @Test
    void mapStarAroundNumber_map_all_gears() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = new ArrayList<>();
        lines.add("467..114");
        lines.add("...*....");
        lines.add("..35.633.");

        // When
        stars = Grid.mapStarAroundNumber(lines);
        //Then
        System.out.println("stars: " + stars);
        assertEquals(stars.get(11), List.of(467, 35));
    }

    @Test
    void mapStarAroundNumber_map_all_gears_demo() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = Utils.loadFile("src/main/resources/demo.txt");


        // When
        stars = Grid.mapStarAroundNumber(lines);

        //Then
        System.out.println("stars: " + stars);
        System.out.println("stars nb: " + stars.size());

        assertEquals(stars.get(13), List.of(467, 35));
        assertEquals(stars.get(85), List.of(755, 598));
    }



    @Test
    void mapStarAroundNumber_map_all_gears_3lines() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = Utils.loadFile("src/main/resources/input.txt");

        lines = lines.subList(0, 3);
        System.out.println("lines: " + lines);
        // When
        stars = Grid.mapStarAroundNumber(lines);

        //Then
        assertEquals(5 , stars.size());
    }


    @Test
    void computeGearRatios_return() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = Utils.loadFile("src/main/resources/demo.txt");

        // When
        int somme = Grid.computeGearRatios(lines);
        //Then
        assertEquals(467835, somme);

    }
}