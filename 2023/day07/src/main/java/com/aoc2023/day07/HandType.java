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



    private static HandType getHandType(List<Integer> counts) {
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
    public static HandType getType(String hand) {
        return getType(hand, false);
    }

    public static HandType getType(String hand, boolean joker) {
        List<Integer> counts = getCounts(hand, joker);
        return getHandType(counts);
    }

    private static List<Integer> getCounts(String hand, boolean joker) {
        Map<Character, Integer> occurrences = getMap(hand, joker);
        List<Integer> counts = new ArrayList<>(occurrences.values());
        Collections.sort(counts, Collections.reverseOrder());
        return counts;
    }

    public static Map<Character, Integer> getMap(String hand, boolean joker) {
        Map<Character, Integer> occurences = new LinkedHashMap<>();
        char maxKey = '0';
        int maxCount = 0;
        for (char c: hand.toCharArray()) {
            occurences.put(c, occurences.getOrDefault(c, 0) + 1);
            if (maxCount < occurences.get(c) && c != 'J') {
                maxCount = occurences.get(c);
                if (c != 'J') { maxKey = c ; }
            }
        }

        if (joker && occurences.containsKey('J') && maxKey != '0') {
            occurences.put(maxKey, occurences.get(maxKey) + occurences.get('J'));
            occurences.remove('J');
        }
        return occurences;
    }

}
