package com.aoc2023.day08.carte;

import org.apache.commons.lang3.tuple.ImmutablePair;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class DesertMapTest {

    @Test
    void make_demo_map() {
        // Given
        List<String> inputLines = new ArrayList<>(Arrays.asList(
                "LLR\n",
                "\n",
                "AAA = (BBB, BBB)\n",
                "BBB = (AAA, ZZZ)\n",
                "ZZZ = (ZZZ, ZZZ)\n"));

        Map<String, ImmutablePair<String, String>> demoMap = Map.of(
                "AAA", ImmutablePair.of("BBB", "BBB"),
                "BBB", ImmutablePair.of("AAA", "ZZZ"),
                "ZZZ", ImmutablePair.of("ZZZ", "ZZZ")

        );
        //When
        Map<String, ImmutablePair<String, String>> mymap = DesertMap.makeMap(inputLines);
        //Then
        assertEquals(demoMap, mymap);
    }

    @Test
    void instruction_is_LLR() {
        // Given
        List<String> inputLines = new ArrayList<>(Arrays.asList(
                "LLR\n",
                "\n",
                "AAA = (BBB, BBB)\n",
                "BBB = (AAA, ZZZ)\n",
                "ZZZ = (ZZZ, ZZZ)\n"));
        //When
        String instruction = DesertMap.makeInstruction(inputLines);
        //Then
        assertEquals("LLR", instruction);
    }

    @Test
    void loadFromLines_set_instructions_and_desertmap() {
        // Given
        List<String> inputLines = new ArrayList<>(Arrays.asList(
                "LLR\n",
                "\n",
                "AAA = (BBB, BBB)\n",
                "BBB = (AAA, ZZZ)\n",
                "ZZZ = (ZZZ, ZZZ)\n"));
        Map<String, ImmutablePair<String, String>> demoMap = Map.of(
                "AAA", ImmutablePair.of("BBB", "BBB"),
                "BBB", ImmutablePair.of("AAA", "ZZZ"),
                "ZZZ", ImmutablePair.of("ZZZ", "ZZZ")

        );
        DesertMap map =  new DesertMap();
        //When
        map.loadFromLines(inputLines);
        //Then
        assertEquals("LLR", map.getInstructions());
        assertEquals(demoMap, map.getDesertMap());
    }
    @Test
    void parcours_demo1_is_2_steps() {
        //Given
        List<String> inputLines = new ArrayList<>(
                Arrays.asList(
                    "RL\n",
                    "\n",
                    "AAA = (BBB, CCC)\n",
                    "BBB = (DDD, EEE)\n",
                    "CCC = (ZZZ, GGG)\n",
                    "DDD = (DDD, DDD)\n",
                    "EEE = (EEE, EEE)\n",
                    "GGG = (GGG, GGG)\n",
                    "ZZZ = (ZZZ, ZZZ)\n"));
        DesertMap map = new DesertMap();
        map.loadFromLines(inputLines);
        //When
        int steps = map.parcours();
        //Then
        assertEquals(2, steps);
    }

    @Test
    void parcours_demo2_from_file_is_6_steps() {
        //Given
        DesertMap map = new DesertMap();
        map.loadFromFile("src/main/resources/demo2.txt");
        //When
        int steps = map.parcours();
        //Then
        assertEquals(6, steps);
    }

    @Test
    void parcoursGhost_demo3_from_file_is_6_steps() {
        //Given
        DesertMap map = new DesertMap();
        map.loadFromFile("src/main/resources/demo3.txt");
        //When
        int steps = map.parcoursGhost();
        //Then
        assertEquals(6, steps);
    }




}
