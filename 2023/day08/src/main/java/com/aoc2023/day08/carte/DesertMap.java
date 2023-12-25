package com.aoc2023.day08.carte;

import lombok.Getter;
import org.aoc.utils.Utils;
import org.apache.commons.lang3.tuple.ImmutablePair;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Getter
public class DesertMap {
    static final String ARRIVAL = "ZZZ";
    static final String DEPART = "AAA";

    public DesertMap() {
        desertMap =  new HashMap<>();
    }

    private  Map<String, ImmutablePair<String, String>> desertMap;
    private String instructions;

    public static Map<String, ImmutablePair<String, String>> makeMap(List<String> lines) {
        Map<String, ImmutablePair<String, String>> desertMap = new HashMap<>();
        lines.remove(0);

        for (String line :lines) {
            if (line.trim().isEmpty()) { continue; }
            String[] parts = line.split(" = ");
            String[] pairParts = parts[1].split(", ");
            desertMap.put(parts[0], new ImmutablePair<>(
                    pairParts[0].substring(1),
                    pairParts[1].substring(0, 3)
            ));
        }
        return desertMap;
    }

    public static String makeInstruction(List<String> inputLines) {
        return inputLines.get(0).trim();
    }

    public void loadFromLines(List<String> inputLines) {
        instructions = makeInstruction(inputLines);
        desertMap = makeMap(inputLines);
    }

    public void loadFromFile(String pathToFile) {
        loadFromLines(Utils.loadFile(pathToFile));
    }

    public int parcours() {
        String current = DEPART;
        int index = 0;
        int steps = 0;
        while (!current.equals(ARRIVAL)) {
            if (index >= instructions.length()) { index = 0; }
            Character instruction = instructions.charAt(index);
            if (instruction.equals('L')) {
                current = desertMap.get(current).getLeft();
            } else {
                current = desertMap.get(current).getRight();
            }
            index++;
            steps++;
        }
        return steps;
    }

    public long parcoursGhost() {
        List<String> nodes = new ArrayList<>(desertMap.keySet().stream()
                .filter(x -> x.endsWith("A"))
                .toList());

        List<Long> nodesMaxSteps = new ArrayList<>();
        // pour chaque node, recherche du nb de steps
        for (String node : nodes) {
            long steps = 0;
            while(!node.endsWith("Z")) {
                for (Character instruction : instructions.toCharArray()) {
                    if (instruction.equals('L')) {
                        node = desertMap.get(node).getLeft();
                    } else {
                        node = desertMap.get(node).getRight();
                    }
                    steps++;
                    if (node.endsWith("Z")) {
                        break;
                    }
                }
            }
            nodesMaxSteps.add(steps);
        }
        return ppcm(nodesMaxSteps);
    }

    // ppcm = a * b / pgcd(a, b)
    public static long ppcm(List<Long> numbers) {
        long result = numbers.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            result =  (result * numbers.get(i)) / pgcd(result, numbers.get(i));
        }
        return result;
    }

    //PGCD: algorithme d'Euclide
    private static long pgcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

}
