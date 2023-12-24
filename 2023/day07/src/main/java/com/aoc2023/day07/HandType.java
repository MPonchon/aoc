package com.aoc2023.day07;

import java.util.*;

public enum HandType {
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIR,
    THREE_OAK,
    FULL_HOUSE,
    FOUR_OAK,
    FIVE_OAK;

    public static HandType getType(String hand) {
        List<Integer> counts = getCounts(hand);

        if (counts.get(0) == 5) {
            return FIVE_OAK;
        } else if (counts.get(0) == 4 ) {
            return FOUR_OAK;
        }
        else if (counts.get(0) == 3) {
            if (counts.get(1) == 2) {
                return FULL_HOUSE;
            }
            return THREE_OAK;
        } else if (counts.get(0) == 2) {
            if (counts.get(1) == 2) {
                return TWO_PAIR;
            }
            return ONE_PAIR;
        }
        return HIGH_CARD;
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
