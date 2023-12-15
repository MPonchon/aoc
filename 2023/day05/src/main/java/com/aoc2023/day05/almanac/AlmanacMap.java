package com.aoc2023.day05.almanac;

import org.aoc.utils.Utils;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.tuple.ImmutablePair;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class AlmanacMap {

    private final Map<String, List<List<Long>>> maps;
    private Map<String, String > mapsOrder;

    public AlmanacMap(String pathToFile) {
        maps = loadParts(pathToFile);
        mapsOrder = new HashMap<>();
        maps.keySet().stream()
                .filter(name -> name.contains("-"))
                .forEach(
                    name -> mapsOrder.put(
                        name.substring(0, name.indexOf("-") ),
                        name.substring(name.lastIndexOf("-") + 1)));
    }

    public static Long strNumberToLong(String number) {
        try {
            return Long.parseLong(number);
        } catch (NumberFormatException e) {
            System.out.println(number + " long -> ex : " + e.getMessage());
            return 0L;
        }
    }
    public static Map<String, List<List<Long>>> loadParts (String pathToFile) {
        Map<String, List<List<Long>>> maps = new HashMap<>();
        List<List<String>> parts = new ArrayList<>();
        List<String> lines = Utils.loadFile(pathToFile);

        String line0 = lines.get(0);
        String mapName = "seed";
        line0 = line0.substring(line0.indexOf(":") + 1);
        List<Long> numbers = Arrays.stream(line0.split(" +"))
                .filter(s -> !s.isEmpty())
                .map(AlmanacMap::strNumberToLong)
                .toList();
        ArrayList<List<Long>> seeds = new ArrayList<>();
        seeds.add(numbers);
        maps.put(mapName, seeds);

        for (int i = 1; i < lines.size(); i++) {
            String line = lines.get(i);
            if (line.isEmpty()) { continue; }
            if (line.contains(":")) {
                mapName = line.substring(0, line.indexOf(":") - 4);
                maps.put(mapName, new ArrayList<>());
            }
            else {
                numbers = Arrays.stream(line.split(" +"))
                        .filter(s -> !s.isEmpty())
                        .map(AlmanacMap::strNumberToLong)
                        .toList();
                maps.get(mapName).add(numbers);
            }
        }
        return maps;
    }

    public long getMapValue(String mapName, long start) {

        List<List<Long>> table = maps.get(mapName);
//        System.out.println("table: " + table);
//        Collections.sort(table, (l1, l2) -> Long.compare(l1.get(1), l2.get(1)));
        for (List<Long> list : table) {
            long source = list.get(1);
            long dest = list.get(0);
            long range = list.get(2);
//            System.out.println("start:" + start + ", source: "+ source + ", dest: " + dest + ", range: " + range + "list: " + list);
            if (start >= source && start <= source + range - 1) {
                return dest + (start - source);
            }
        }
        return start; // not in map
    }

    public long lowestFromSeeds() {
        String actualMap = "seed";
        long  locationLowest = Long.MAX_VALUE;
        for (Long start: maps.get("seed").get(0)) {
            locationLowest  = parcoursMaps(actualMap, start, locationLowest);
            actualMap = "seed"; // reset boucle
        }
        return locationLowest;
    }

    public Long parcoursMaps(String actualMap, long start, long locationLowest) {
        while (mapsOrder.containsKey(actualMap)) {
            String next = mapsOrder.get(actualMap);
            start = getMapValue(actualMap + "-to-" + next, start);
            actualMap = next;
        }
        if (actualMap.equals("location") && start < locationLowest) {
            locationLowest = start;
        }
        return locationLowest;
    }

    public long lowestFromLocationPart2() {
        String actualMap = "seed";
        long  locationLowest = Long.MAX_VALUE;
        List<Long> seeds  = maps.get("seed").get(0);
        Map<Long, Long> cache = new HashMap<>();
        // rewrite seeds
        for (int i = 0; i < seeds.size(); i +=2) {
            System.out.println("i: " + i + " / " + seeds.size() / 2);
            System.out.println("seed start : " + seeds.get(i) + ", seed end: " + (seeds.get(i)  + seeds.get(i+1)));
            for (long start = seeds.get(i); start <= (seeds.get(i) + seeds.get(i+1)); start++) {
                long start0 = start;
                if (!cache.containsKey(start0)) {
                    locationLowest = parcoursMaps(actualMap, start, locationLowest);
                    cache.put(start0, locationLowest);
                }
                actualMap = "seed"; // reset boucle
            }
        }
        return locationLowest;
    }



}
