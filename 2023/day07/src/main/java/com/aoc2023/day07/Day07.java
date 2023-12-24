package com.aoc2023.day07;

import org.aoc.BaseDay;
import org.aoc.BaseDay.*;
import org.aoc.utils.Utils;

import java.util.*;

import static org.aoc.utils.Utils.DEMO_PATH;
import static org.aoc.utils.Utils.INPUT_PATH;

public class Day07  extends BaseDay<Long, Integer> {

    Day07() {
        super(7);
    }

    public Long firstPart(String pathToFile) {
        List<String> lines = Utils.loadFile(pathToFile);
        List<String> hands = new ArrayList<>();
        Map<HandType, List<String>> mapHandsByType =  new HashMap<>();
        Map<String, Integer> mapBids =  new HashMap<>();
        makeHandMapType(lines, hands, mapBids, mapHandsByType);
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

    private static void makeHandMapType(List<String> lines, List<String> hands, Map<String, Integer> mapBids, Map<HandType, List<String>> mapHandsByType) {
        for (int index = 0; index < lines.size(); index++) {
            String line = lines.get(index);
            String[] parts = line.split(" ");
            String hand = parts[0];
            int bid = Integer.parseInt(parts[1]);
            hands.add(hand);
            mapBids.put(hand, bid);
            System.out.println("hand " + hand + " bid " + bid);
            HandType handType = HandType.getType(hand);
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
                sortHands(handsListForKey);
                for (String hand: handsListForKey) {
                    rank++;
                    win += rank * mapBids.get(hand);
                }
            }
        }
        return win;
    }

    public static void sortHands(List<String> handsListForKey) {
        Collections.sort(handsListForKey, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                for (int i=0; i < 5 ; i++) {
                    char c1 = o1.charAt(i);
                    char c2 = o2.charAt(i);
                    if (c1 == c2) { continue; }
                    Card card1 = Card.fromChar(c1);
                    Card card2 = Card.fromChar(c2);
                    return card1.compareTo(card2);
                }
                return 0;
            }
        });
    }


}
