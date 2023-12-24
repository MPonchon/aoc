package com.aoc2023.day07;

import org.aoc.BaseDay;
import org.aoc.BaseDay.*;
import org.aoc.utils.Utils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.aoc.utils.Utils.DEMO_PATH;

public class Day07  extends BaseDay<Integer, Integer> {

    Day07() {
        super(7);
    }

    @Override
    public Integer getDemoPart1() {
        List<String> lines = Utils.loadFile(DEMO_PATH);
        List<String> hands = new ArrayList<>();
        List<Integer> bids = new ArrayList<>();
        Map<HandType, List<Integer>> typesIndex =  new HashMap<>();
        for (int index=0; index < lines.size(); index++) {
            String line = lines.get(index);
            String[] parts = line.split(" ");
            String hand = parts[0];
            int bid = Integer.parseInt(parts[1]);
            hands.add(hand);
            bids.add(bid);
            System.out.println("hand " + hand + " bid " + bid);
            HandType handType = HandType.getType(hand);
            List<Integer> temp = typesIndex.getOrDefault(handType, new ArrayList<>());
            temp.add(index);
            typesIndex.put(handType, temp);
        }
        System.out.println("hands " + hands);
        System.out.println("map " + typesIndex);
        return 0;
    }


}
