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
//            System.out.println("inst   " + instruction);
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

    public int parcoursGhost() {
        List<String> nodes = new ArrayList<>(desertMap.keySet().stream()
                .filter(x -> x.endsWith("A"))
                .toList());

        int index = 0;
        int steps = 0;
        boolean finished = false;
        while (! finished) {
            if (index >= instructions.length()) { index = 0; }
            Character instruction = instructions.charAt(index);
            int countEnds = 0;
            for (int i = 0; i < nodes.size(); i++) {
                String node = nodes.get(i);
                if (instruction.equals('L')) {
                    node = desertMap.get(node).getLeft();
                } else {
                    node = desertMap.get(node).getRight();
                }
                nodes.set(i, node);
                if (node.endsWith("Z")) { countEnds ++; }
            }
            if (countEnds == nodes.size()) {
                finished = true;
            }
            index++;
            steps++;
        }
        return steps;
    }
}
