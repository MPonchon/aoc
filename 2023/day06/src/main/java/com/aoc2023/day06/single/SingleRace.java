package com.aoc2023.day06.single;

import org.aoc.utils.Utils;
import org.apache.commons.lang3.tuple.Pair;

import java.util.List;


public class SingleRace {

    public static Long mergeToLong(String s) {
        String result = s.substring(s.indexOf(":")+1).trim().replaceAll(" +", "");
        return Long.parseLong(result);
    }

    public static Pair<Long, Long> loadRaces(String pathToFile) {
        List<String> data = Utils.loadFile(pathToFile);
        return Pair.of(
                mergeToLong(data.get(0)),
                mergeToLong(data.get(1))
        );
    }

    public static long nbWinnings(long millis, long distanceRef) {
        long breaker = 0;
        for (int i = 0; i < millis; i++) {
            long distance = (millis - i) * i;
            if (distance > distanceRef) {
                breaker = i;
                break;
            }
        }
        return (millis +1) - 2 * breaker;
    }


    public static long part2(String pathToFile) {
        Pair<Long, Long> race = loadRaces(pathToFile);
        System.out.println("race: " + race);
        long mul = 1L;
            long nbWin = nbWinnings(race.getLeft(), race.getRight());
            if (nbWin != 0) {
                mul *= nbWin;
            }
        return mul;
    }
}
