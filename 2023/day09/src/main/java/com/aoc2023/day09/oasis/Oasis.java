package com.aoc2023.day09.oasis;

import lombok.Getter;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

@Getter
public class Oasis {

    public static int nextNumber(List<Integer> line) {
        List<Integer>  temp = compute(line, true);
        return temp.get(temp.size() - 1);
    }

    public static List<Integer> makeLine(List<Integer> sequence) {
        return IntStream.range(0, sequence.size() -1 )
                .mapToObj( i -> sequence.get(i+1) - sequence.get(i) )
                .toList();
    }

    public static boolean isLastLine(List<Integer> line) {
        return line.stream().allMatch(x -> x == 0);
    }

    public static List<Integer> computeTempLine(List<Integer> line, boolean endOfLine) {
        int indexLine = endOfLine ? line.size() - 1 : 0;
        List<Integer> computedTable = new ArrayList<>();
        computedTable.add(line.get(indexLine));
        List<Integer> result = line;
        do {
            result = makeLine(result);
            computedTable.add(result.get(endOfLine ? result.size() - 1 : 0));
        } while(! isLastLine(result));
        Collections.reverse(computedTable);
        return computedTable;
    }

    public static int makeSum(List<List<Integer>> sequences) {
        return sequences.stream()
                .map(Oasis::nextNumber)
                .mapToInt(Integer::intValue)
                .sum();
    }

    public static  List<Integer> compute(List<Integer> line, boolean endOfLine) {
        List<Integer> computedTable = computeTempLine(line, endOfLine);

        List<Integer> resultTable = new ArrayList<>();
        resultTable.add(0);
        for (int i = 1; i < computedTable.size(); i++) {
            if (endOfLine) {
                resultTable.add(resultTable.get(i-1) + computedTable.get(i));
            } else {
                resultTable.add(computedTable.get(i) - resultTable.get(i-1) );
            }
        }
        return resultTable;
    }

    public static int nextNumberBackward(List<Integer> line) {
        List<Integer>  temp = compute(line, false);
        return temp.get(temp.size() - 1);
    }


    public static int makeSumBackward(List<List<Integer>> sequences) {
        return sequences.stream()
                .map(Oasis::nextNumberBackward)
                .mapToInt(Integer::intValue)
                .sum();
    }
}
