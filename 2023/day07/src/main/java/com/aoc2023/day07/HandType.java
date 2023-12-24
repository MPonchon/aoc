package com.aoc2023.day07;

import java.util.*;

public enum HandType {
    FIVE_OAK,
    FOUR_OAK,
    FULL_HOUSE,
    THREE_OAK,
    TWO_PAIR,
    ONE_PAIR,
    HIGH_CARD;

    public static HandType getType(String hand) {
        List<Integer> counts = findTypes(hand);
        if (counts.isEmpty()) {
            return HIGH_CARD;
        }

        if (counts.size() == 1) {
            if (counts.get(0) == 5) {
                return FIVE_OAK;
            } else if (counts.get(0) == 4) {
                return FOUR_OAK;
            } else if (counts.get(0) == 3) {
                return THREE_OAK;
            } else {
                return ONE_PAIR;
            }
        } else {
            if (counts.contains(3)) {
                return FULL_HOUSE;
            }
            return TWO_PAIR;
        }
    }

    private static List<Integer> getCounts(String hand) {
        Map<Character, Integer> charCount = getMap(hand);
        List<Integer> counts = new ArrayList<>(charCount.values());
        Collections.sort(counts, Collections.reverseOrder());
        return counts;
    }

    private static Map<Character, Integer> getMap(String hand) {
        Map<Character, Integer> charCount =  new LinkedHashMap<>();
        for (char c: hand.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        return charCount;
    }

    static int maxSameChar(String hand) {
        List<Integer> counts = getCounts(hand);
        return counts.get(0);
    }

    // carte contigues
    static List<Integer> findTypes(String hand) {
        char old =  hand.charAt(0);
        int same = 0;
        List<Integer> lcounts =  new ArrayList<>();
        for(int i=0; i <5; i++) {
            char current = hand.charAt(i);
            if (old == current) {
                same += 1;
            }
            else {
                if (same > 1) { lcounts.add(same); }
                same = 1;
                old = current;
            }
        }
        if (same > 1) { lcounts.add(same); }
//        System.out.println(".. " + hand + " lcount " + lcounts);
        return lcounts;
    }
}
