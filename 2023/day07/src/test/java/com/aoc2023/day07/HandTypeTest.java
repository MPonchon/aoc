package com.aoc2023.day07;

import org.junit.jupiter.api.Test;

import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class HandTypeTest {


    @Test
    void getType() {
        assertEquals(HandType.FIVE_OAK, HandType.getType("OOOOO"));
        assertEquals(HandType.FOUR_OAK, HandType.getType("IOOOO"));
        assertEquals(HandType.FOUR_OAK, HandType.getType("OOOOE"));
        assertEquals(HandType.FULL_HOUSE, HandType.getType("23332"));
        assertEquals(HandType.FULL_HOUSE, HandType.getType("11333"));
        assertEquals(HandType.FULL_HOUSE, HandType.getType("333AA"));

        assertEquals(HandType.THREE_OAK, HandType.getType("3331A"));
        assertEquals(HandType.THREE_OAK, HandType.getType("2333A"));
        assertEquals(HandType.THREE_OAK, HandType.getType("IO333"));
        assertEquals(HandType.TWO_PAIR, HandType.getType("IIO33"));
        assertEquals(HandType.TWO_PAIR, HandType.getType("II33O"));
        assertEquals(HandType.ONE_PAIR, HandType.getType("IIO1U"));
        assertEquals(HandType.ONE_PAIR, HandType.getType("AEIIU"));
        assertEquals(HandType.HIGH_CARD, HandType.getType("12345"));
        assertEquals(HandType.THREE_OAK, HandType.getType("32343"));
    }


    @Test
    void getMap_with_joker_FIVE_OAK() {
        assertEquals(HandType.FIVE_OAK, HandType.getType("OOOOO", true));
        assertEquals(HandType.FIVE_OAK, HandType.getType("JOOOO", true));
        assertEquals(HandType.FIVE_OAK, HandType.getType("JJJJO", true));
        assertEquals(HandType.FIVE_OAK, HandType.getType("JOJOJ", true));
        assertEquals(HandType.FIVE_OAK, HandType.getType("OJJJO", true));
        assertEquals(HandType.FIVE_OAK, HandType.getType("2JJJ2", true));
    }

    @Test
    void getMap_with_joker_FOUR_OAK() {
        assertEquals(HandType.FOUR_OAK, HandType.getType("AOJOO", true));
        assertEquals(HandType.FOUR_OAK, HandType.getType("AJJOO", true));
        assertEquals(HandType.FOUR_OAK, HandType.getType("AJJOJ", true));
        assertEquals(HandType.FOUR_OAK, HandType.getType("T55J5", true));
    }

    @Test
    void getMap_with_joker_THREE_OAK() {
        assertEquals(HandType.THREE_OAK, HandType.getType("23J31", true));
        assertEquals(HandType.THREE_OAK, HandType.getType("AJJ31", true));
        assertEquals(HandType.THREE_OAK, HandType.getType("AJ31J", true));
    }

    @Test
    void getMap_with_joker_FULL_HOUSE() {
        assertEquals(HandType.FULL_HOUSE, HandType.getType("23J32", true));
    }

    @Test
    void getMap_with_joker_TWO_PAIR() {
        assertEquals(HandType.TWO_PAIR, HandType.getType("2AA32", true));
    }

    @Test
    void getMap_with_joker_ONE_PAIR() {
        assertEquals(HandType.ONE_PAIR, HandType.getType("2345J", true));
    }
}