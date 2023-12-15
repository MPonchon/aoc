package com.aoc2023.day05.almanac;

import org.aoc.utils.Utils;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class AlmanacMapTest {

    @Test
    void loadParts_with_maps() {
        //Given
        List<String> lines = Utils.loadFile("src/main/resources/demo.txt");
        //Then
        Map<String, List<List<Long>>> maps = AlmanacMap.loadParts("src/main/resources/demo.txt");
        //When
        List<String> mapNames = maps.keySet().stream().toList();
//        System.out.println(mapNames);
//        System.out.println(maps);
//        System.out.println("light-to-temperature" + maps.get("light-to-temperature"));
        //Then
        assertEquals(List.of(79L, 14, 55, 13), maps.get("seeds").get(0));
        assertEquals(List.of(45L, 77, 23), maps.get("light-to-temperature").get(0));
        assertEquals(List.of(81L, 45, 19), maps.get("light-to-temperature").get(1));
    }

    @Test
    void create_AlmanacMap() {
        AlmanacMap almanacMap = new AlmanacMap("src/main/resources/demo.txt");
    }

    @Test
    void getMapValue_should_return_fisrt_src() {
        //Given
        //When
        AlmanacMap almanacMap = new AlmanacMap("src/main/resources/demo.txt");
        //Then
        assertEquals(44, almanacMap.getMapValue("light-to-temperature", 44));
        assertEquals(45, almanacMap.getMapValue("light-to-temperature", 77));
        assertEquals(67, almanacMap.getMapValue("light-to-temperature", 99));

    }

    @Test
    void lowestFromSeeds_from_demo_return35() {
        //Given
        //When
        AlmanacMap almanacMap = new AlmanacMap("src/main/resources/demo.txt");
        //Then
        assertEquals(35, almanacMap.lowestFromSeeds());
    }

    @Test
    void lowestFromLocationPart2_demo() {
        //Given
        //When
        AlmanacMap almanacMap = new AlmanacMap("src/main/resources/demo.txt");
        //Then
        assertEquals(46, almanacMap.lowestFromLocationPart2());
    }
}