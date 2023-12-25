package com.aoc2023.day07;

import org.aoc.BaseDay;
import org.aoc.utils.Utils;

import java.util.*;

import static java.util.Map.entry;
import static org.aoc.utils.Utils.DEMO_PATH;
import static org.aoc.utils.Utils.INPUT_PATH;

import com.aoc2023.day07.HandType;

public class Day07  extends BaseDay<Long, Long> {

    Day07() {
        super(7);
    }

    public static final Map<Character, Integer> cardValues1 = Map.ofEntries(
            entry('2', 2),
            entry('3', 3),
            entry('4', 4),
            entry('5', 5),
            entry('6', 6),
            entry('7', 7),
            entry('8', 8),
            entry('9', 9),
            entry('T', 10),
            entry('J', 11),
            entry('Q', 12),
            entry('K', 13),
            entry('A', 14)
    );

    public static final Map<Character, Integer> cardValues2 = Map.ofEntries(
            entry('J', 1),
            entry('2', 2),
            entry('3', 3),
            entry('4', 4),
            entry('5', 5),
            entry('6', 6),
            entry('7', 7),
            entry('8', 8),
            entry('9', 9),
            entry('T', 10),
            entry('Q', 12),
            entry('K', 13),
            entry('A', 14)
    );

    public static Map<Character, Integer> cardValues = null;

    public Long firstPart(String pathToFile) {
        List<String> lines = Utils.loadFile(pathToFile);
        List<String> hands = new ArrayList<>();
        Map<HandType, List<String>> mapHandsByType =  new HashMap<>();
        Map<String, Integer> mapBids =  new HashMap<>();
        cardValues = Day07.cardValues1;
        makeHandMapType(lines, hands, mapBids, mapHandsByType, false);
        return computeWin(mapHandsByType, mapBids);
    }

    @Override
    public Long getDemoPart1() {
        return firstPart(DEMO_PATH);
    }
    @Override
    public Long getPart1() {
        return firstPart(INPUT_PATH);
    }

    public Long secondPart(String pathToFile) {
        List<String> lines = Utils.loadFile(pathToFile);
        List<String> hands = new ArrayList<>();
        Map<HandType, List<String>> mapHandsByType =  new HashMap<>();
        Map<String, Integer> mapBids =  new HashMap<>();
        cardValues = Day07.cardValues2;
        makeHandMapType(lines, hands, mapBids, mapHandsByType, true);
        return computeWin(mapHandsByType, mapBids);
    }


    @Override
    public Long getDemoPart2() {
        return secondPart(DEMO_PATH) ;
    }

    @Override
    public Long getPart2() {
        return secondPart(INPUT_PATH);
    }


    private static void makeHandMapType(List<String> lines, List<String> hands, Map<String, Integer> mapBids, Map<HandType, List<String>> mapHandsByType, boolean joker) {
        for (int index = 0; index < lines.size(); index++) {
            String line = lines.get(index);
            String[] parts = line.split(" ");
            String hand = parts[0];
            int bid = Integer.parseInt(parts[1]);
            hands.add(hand);
            mapBids.put(hand, bid);
//            System.out.println("hand " + hand + " bid " + bid);
            HandType handType = HandType.getType(hand, joker);
            List<String> temp = mapHandsByType.getOrDefault(handType, new ArrayList<>());
            temp.add(hand);
            mapHandsByType.put(handType, temp);
        }
    }


    private static long computeWin(Map<HandType, List<String>> typesIndex, Map<String, Integer> mapBids) {
        int rank = 0;
        long win = 0L;
        for (HandType handtype : HandType.values()) {
            if (typesIndex.containsKey(handtype)) {
                List<String> handsListForKey = typesIndex.get(handtype);
                sortHands(handsListForKey, handComparatorP1);
                for (String hand: handsListForKey) {
                    rank++;
                    win += rank * mapBids.get(hand);
                }
            }
        }
        return win;
    }

    public static Comparator<String> handComparatorP1 = new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            for (int i=0; i < 5 ; i++) {
                char c1 = o1.charAt(i);
                char c2 = o2.charAt(i);
                if (c1 == c2) { continue; }
                Integer i1 = cardValues.get(c1);
                Integer i2 = cardValues.get(c2);
                return i1.compareTo(i2);
            }
            return 0;
        }
    };

    public static void sortHands(List<String> handsListForKey, Comparator<String> comparator) {
        Collections.sort(handsListForKey, comparator);
    }

}
