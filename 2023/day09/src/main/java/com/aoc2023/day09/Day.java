package com.aoc2023.day09;

import com.aoc2023.day09.oasis.Oasis;
import org.aoc.BaseDay;
import org.aoc.utils.Utils;

import java.util.Arrays;
import java.util.List;

import static org.aoc.utils.Utils.DEMO_PATH;
import static org.aoc.utils.Utils.INPUT_PATH;

public class Day extends BaseDay<Integer, Integer> {
    public Day() {
        super(9);
    }

    public static List<List<Integer>> getSequences(String pathToFile) {
        List<String> sequences = Utils.loadFile(pathToFile);
        return sequences.stream()
                .map( line -> Arrays
                        .stream(line.split(" +"))
                        .map(Integer::parseInt)
                        .toList()
                ).toList();
    }

    @Override
    public Integer getDemoPart1() {
        List<List<Integer>> sequences = getSequences(DEMO_PATH);
        return Oasis.makeSum(sequences);
    }

    @Override
    public Integer getPart1() {
        List<List<Integer>> sequences = getSequences(INPUT_PATH);
        return Oasis.makeSum(sequences);
    }

    @Override
    public Integer getDemoPart2() {
        List<List<Integer>> sequences = getSequences(DEMO_PATH);
        return Oasis.makeSumBackward(sequences);
    }
    @Override
    public Integer getPart2() {
        List<List<Integer>> sequences = getSequences(INPUT_PATH);
        return Oasis.makeSumBackward(sequences);
    }

}
