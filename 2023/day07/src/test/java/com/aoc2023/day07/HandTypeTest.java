package com.aoc2023.day07;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HandTypeTest {

    @Test
    void isFiveOfAKind() {
    }

    @Test
    void nbSameChar() {
        assertEquals(5, HandType.maxSameChar("AAAAA"));
        assertEquals(4, HandType.maxSameChar("ZAAAA"));
        assertEquals(4, HandType.maxSameChar("AAAAZ"));
        assertEquals(3, HandType.maxSameChar("AAARZ"));
        assertEquals(3, HandType.maxSameChar("IAAAZ"));
        assertEquals(3, HandType.maxSameChar("IYAAA"));
        assertEquals(3, HandType.maxSameChar("IIAAA"));
        assertEquals(2, HandType.maxSameChar("IIABA"));
    }

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
    void findTypes() {
        HandType.findTypes("AAAAA");
        HandType.findTypes("1AAAA");
        HandType.findTypes("AAAA1");
        HandType.findTypes("11AAA");
        HandType.findTypes("111AA");
        HandType.findTypes("111OA");
        HandType.findTypes("11UAA");
        HandType.findTypes("U11AA");
        HandType.findTypes("U11KA");
    }

}