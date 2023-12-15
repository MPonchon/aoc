package com.aoc2023.day05.almanac;

import org.junit.jupiter.api.Test;

class SmapTest {

    @Test
    void merge_map1_below_map2_1() {
        //Given
        Smap map1 = new Smap(10L, 20L, 10L);
        Smap map2 = new Smap(100L, 30L, 4L);
        //When
        map1.merge(map2.destOrg(), map2.srcOrg(), map2.getRange());
        //Then
        System.out.println("map1 : " + map1);
    }

}