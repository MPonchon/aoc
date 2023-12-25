package com.aoc2023.day08;

import ch.qos.logback.core.joran.sanity.Pair;
import com.aoc2023.day08.carte.DesertMap;
import org.aoc.*;
import org.aoc.utils.Utils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.aoc.utils.Utils.INPUT_PATH;

public class Day08 extends BaseDay<Integer, Integer>{
    public Day08(int day) {
        super(day);
    }

    @Override
    public Integer getPart1() {
        DesertMap desertMap = new DesertMap();
        desertMap.loadFromFile(INPUT_PATH);
        return  desertMap.parcours();
    }

    @Override
    public Integer getPart2() {
        DesertMap desertMap = new DesertMap();
        desertMap.loadFromFile(INPUT_PATH);
        return  desertMap.parcoursGhost();
    }
}
