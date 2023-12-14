package com.aoc2013.day04.cards;


import org.aoc.utils.Utils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

public class Cards {

    public static List<List<List<Integer>>> loadData(String pathToFile) {
        List<String> data = Utils.loadFile(pathToFile);
        if (data == null || data.isEmpty()) { return null; }
//        List<List<List<Integer>>> result = List.of(new ArrayList<>(), new ArrayList<>());
//        for (String line : data) {
//            String[] parts = line.split("\\:");
//            parts = parts[1].split("\\|");
//            List<List<Integer>> wins = new ArrayList<>();
//            List<List<Integer>> nums = new ArrayList<>();
//            wins.add(getIntegerList(parts, 0));
//            nums.add(getIntegerList(parts, 1));
//            result.get(0).addAll(wins);
//            result.get(1).addAll(nums);
//        }
        List<List<List<Integer>>> result = data.stream()
                .map(line -> {
                    String[] parts = line.split(":");
                    parts = parts[1].split("\\|");
                    List<Integer> wins = getIntegerList(parts, 0);
                    List<Integer> nums = getIntegerList(parts, 1);
                    return Arrays.asList(Collections.singletonList(wins), Collections.singletonList(nums));
                })
                .reduce(
                        Arrays.asList(new ArrayList<>(), new ArrayList<>()),    // initial
                        (acc, lists) -> {
                            acc.get(0).addAll(lists.get(0));
                            acc.get(1).addAll(lists.get(1));
                            return acc;
                        }
                );
        return result;

    }

    private static List<Integer> getIntegerList(String[] parts, int x) {
        return Arrays.stream(parts[x].split(" +"))
                .filter(s -> !s.isEmpty())
                .mapToInt(Integer::parseInt).boxed().toList();
    }

    public static int worthPoints(List<List<Integer>> winningsList, List<List<Integer>> numbersList) {
//        int[] points = {0};
//        IntStream.range(0, winningsList.size()).forEach(i -> {
//            List<Integer> winnings = winningsList.get(i);
//            List<Integer> numbers = numbersList.get(i);
//            int bonus = (int) winnings.stream().filter(numbers::contains).count();
//            points[0]  += (int) Math.pow(2, bonus - 1);
//        });
//        return points[0];
        return IntStream.range(0, winningsList.size())
                .map(i -> nbWonCards(winningsList.get(i), numbersList.get(i)))
                .map(i -> (int)Math.pow(2, i - 1))
                .sum();
    }

    public static int nbWonCards(List<Integer> winningsList, List<Integer> numbersList) {
        return (int) winningsList.stream()
                .filter(numbersList::contains)
                .count();
    }

    public static int computeWorthPointFromData(String pathToFile) {
        List<List<List<Integer>>>  allnumbers = Cards.loadData(pathToFile);
        return Cards.worthPoints(
            allnumbers.get(0),
            allnumbers.get(1));
    }
}
