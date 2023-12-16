package com.aoc2023.day06.race;

import org.apache.commons.lang3.tuple.Pair;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.aoc.utils.Utils;


public class Race {

    public static List<Integer> stringToInt(String s) {
        return Arrays.stream(s.substring(s.indexOf(":")+1).split(" +"))
                    .filter(line ->!line.isEmpty()).mapToInt(Integer::parseInt).boxed().toList();
    }

    public static List<Pair<Integer, Integer>> loadRaces(String pathToFile) {
        List<String> data = Utils.loadFile(pathToFile);
        List<Pair<Integer, Integer>> result = new ArrayList<>();
        List<Integer> lefts = stringToInt(data.get(0).trim());
        List<Integer> rights = stringToInt(data.get(1).trim());
        for (int i = 0; i < lefts.size(); i++) {
            result.add(Pair.of(lefts.get(i), rights.get(i)));
        }
        return result;
    }

    public static int nbWinnings(int millis, int distanceRef) {
        int breaker = 0;
        for (int i = 0; i < millis; i++) {
            int distance = (millis - i) * i;
            if (distance > distanceRef) {
                breaker = i;
                break;
            }
        }
        return (millis +1) - 2 * breaker;
    }

    public static int part1(String pathToFile) {
        List<Pair<Integer, Integer>> races = Race.loadRaces(pathToFile);
        int mul = 1;
        for (var race: races) {
            int nbWin = nbWinnings(race.getLeft(), race.getRight());
            if (nbWin != 0) {
                mul *= nbWin;
            }
        }
        return mul;
    }
}
