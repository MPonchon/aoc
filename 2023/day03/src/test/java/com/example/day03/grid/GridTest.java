package com.example.day03.grid;

import com.example.day03.dir.Direction;
import com.example.day03.utils.Utils;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

import static com.example.day03.grid.Grid.findNumbersAroundStar;
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
    void part1_input_result_is_544664() {
        // Given
        List<String> lines = Utils.loadFile("src/main/resources/input.txt");

        // When
        int somme = Grid.sumParts(lines);
        //Then
        assertEquals(544664, somme);
    }

    // --- part2 ----
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

//    @Test

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
    void getNumber_UP_is_619() {
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
    void getNumber_UP_is_600() {
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
    @Test
    void getNumber_UP_is_601() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...601.602");
        lines.add("......*...");
        //When
        Integer n = Grid.getNumber(lines, 1, 6, Direction.UP);
        //Then
        assertEquals(Integer.valueOf(601), n);
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
    void findNumbersAroundStar_cas_2_up() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("...600.601");
        lines.add("......*...");
        lines.add("..........");
        //When
        List<Integer>  ln = findNumbersAroundStar(lines, 1, 6 );

        //Then
        assertEquals(List.of(600, 601), ln);
    }
    @Test
    void findNumbersAroundStar_cas_1_up() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("....601...");
        lines.add("......*...");
        lines.add(".......999");
        //When
        List<Integer>  ln = findNumbersAroundStar(lines, 1, 6 );

        //Then
        assertEquals(List.of(601,999), ln);
    }

    @Test
    void findNumbersAroundStar_cas_2_down() {
        //Given
        List<String> lines = new ArrayList<>();
        lines.add("..........");
        lines.add("......*...");
        lines.add("...998.999");
        //When
        List<Integer>  ln = findNumbersAroundStar(lines, 1, 6 );

        //Then
        assertEquals(List.of(998,999), ln);
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
    void mapStarAroundNumber_Left_Right_Up() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = new ArrayList<>();
        lines.add("467.114.");
        lines.add("...*....");
        lines.add(".....633.");

        // When
        stars = Grid.mapStarAroundNumber(lines);
        //Then
        System.out.println("stars: " + stars);
        assertEquals(List.of(467, 114), stars.get(11));
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

        // When
        stars = Grid.mapStarAroundNumber(lines);

        //Then
        System.out.println("stars: " + stars);
        assertEquals(8 , stars.size());
        // stars: {227=[714, 746], 197=[958, 253], 153=[276, 346], 185=[612, 923], 268=[159, 674], 254=[833, 432], 239=[574, 890], 271=[297, 415]}
    }

    @Test
    void computeGearRatios_map_all_gears_3lines() {
        // Given
        List<String> lines = Utils.loadFile("src/main/resources/input.txt");
        lines = lines.subList(0, 3);

//        System.out.println("lines: " + lines);
        // When
        int somme = Grid.computeGearRatios(lines);

        //Then
        //System.out.println("stars: " + stars);
        assertEquals(2536527, somme);
        /**
         * l 1 c 13 (index 153):[276, 346]
         * l 1 c 45 (index 185):[612, 923]
         * l 1 c 57 (index 197):[958, 253]
         * l 1 c 87 (index 227):[714, 746]
         * l 1 c 99 (index 239):[574, 890]
         * l 1 c 114 (index 254):[833, 432]
         * l 1 c 128 (index 268):[159, 674]
         * l 1 c 131 (index 271):[297, 415]
         */
    }

    @Test
    void mapStarAroundNumber_map_all_gears_4lines() {
        // Given
        Map<Integer, List<Integer>> stars = null;
        List<String> lines = Utils.loadFile("src/main/resources/input.txt");
        lines = lines.subList(0, 5);

        // When
        stars = Grid.mapStarAroundNumber(lines);

        //Then
        Grid.displayMap(stars, lines.get(0).length());
        System.out.println("stars: " + stars);
        assertEquals(13 , stars.size());
        // stars: {227=[714, 746], 197=[958, 253], 153=[276, 346], 185=[612, 923], 268=[159, 674], 254=[833, 432], 239=[574, 890], 271=[297, 415]}
    }


    @Test
    void computeGearRatios_Demo_return_467835() {
        // Given
        List<String> lines = Utils.loadFile("src/main/resources/demo.txt");

        // When
        int somme = Grid.computeGearRatios(lines);
        //Then
        assertEquals(467835, somme);

    }
}