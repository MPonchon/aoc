package com.example.day03.grid;

import com.example.day03.dir.Direction;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

import static java.lang.Character.isDigit;

public class Grid {
    static final int NumberSize = 3;

    public static List<Integer> getAdjacentNumbers(List<String> lines) {
        List<Integer> numbers = new ArrayList<>();
        String regex = "\\d+";
        Pattern pattern = Pattern.compile(regex);

        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            Matcher matcher = pattern.matcher(line);
            while (matcher.find()) {
                String nombreTrouve = matcher.group();
                int posStart = matcher.start() == 0 ? 0 :  matcher.start() - 1;
                int posFin = matcher.end() == line.length()  ?  matcher.end()  : matcher.end() + 1;
                List<String> window = new ArrayList<>();
                if (i == 0) {
                    window.add(line.substring(posStart, posFin));
                    window.add(lines.get(i+1).substring(posStart, posFin));
                } else if (i == lines.size()-1) {
                    window.add(lines.get(i-1).substring(posStart, posFin));
                    window.add(line.substring(posStart, posFin));
                } else {
                    window.add(lines.get(i-1).substring(posStart, posFin));
                    window.add(line.substring(posStart, posFin));
                    window.add(lines.get(i+1).substring(posStart, posFin));
                }
                if (symbolAround( window) ){
                    numbers.add(Integer.parseInt(nombreTrouve));
                }
            }
        }
        return numbers;
    }

    public static boolean symbolAround(List<String> window) {
        for(int i = 0; i < window.get(0).length(); i++) {
            for (String line : window) {
                Character thechar = line.charAt(i);
                if (thechar != '.' && (thechar < '0' || thechar > '9')) { return true; }
            }
        }
        return false;
    }

    public static int sumParts(List<String> lines) {
        List<Integer> numbers =  getAdjacentNumbers(lines);
        return numbers.stream()
                .mapToInt(Integer::intValue)
                .sum();
    }

    // ---------------- part 2 -------------------

    public static Integer findFirstNumber(String line) {
        String regex = "\\d+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);
        if (! matcher.find()) { return null; }
        return Integer.parseInt(matcher.group(0));
    }

    public static Integer findFirstNumberFromStar(String line, int posStar) {
        String regex = "\\d+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);
        while(matcher.find()){
            if (posStar >=  matcher.start() - 1  && posStar <= matcher.end()  ) {
                return Integer.parseInt(matcher.group());
            }
        }
        return null;
    }

    public static Integer getNumber(List<String> lines, int pos, int posStar, Direction dir) {
        Integer result = null;
        if (dir == Direction.LEFT && posStar >= Grid.NumberSize) {
            if(! isDigit(lines.get(pos).charAt(posStar - 1)) ) { return null; }
            String line = lines.get(pos).substring(posStar - Grid.NumberSize, posStar);
//            System.out.println("line "+ line);
            result = findFirstNumber(line);

        }
        else if (dir == Direction.RIGHT && posStar < lines.get(0).length() - Grid.NumberSize) {
            if(! isDigit(lines.get(pos).charAt(posStar + 1)) ) { return null; }
            String line = lines.get(pos).substring(posStar,  posStar + Grid.NumberSize+1);
            result = findFirstNumber(line);
        }
        else if (dir == Direction.UP && pos > 0) {
            String line = lines.get(pos -1);
            result = findFirstNumberFromStar(line, posStar);
        }
        else if (dir == Direction.DOWN && pos < lines.size() - 1) {
            String line = lines.get(pos +1);
            result = findFirstNumberFromStar(line, posStar);
        }
        return result;
    }

    public static Integer getNumberAbove(List<String> lines,int pos, int posStar) {
        return getNumber(lines, pos, posStar, Direction.UP);
    }
    public static Integer getNumberBellow(List<String> lines,int pos, int posStar) {
        return getNumber(lines, pos, posStar, Direction.DOWN);
    }

    public static int calcIndex(int line, int column, int lineSize) {
        return column + line * lineSize;
    }


    public static void addNumberToList(List<Integer> numbers, Integer number) {
        if (number!= null) { numbers.add(number);}
    }

    public static List<Integer> findNumbersAroundStar( List<String> lines, int idxline, int posStar ) {
        List<Integer> result = new ArrayList<>();
        if (idxline > 0) {
            String line0 = lines.get(idxline -1);
            if (isDigit(line0.charAt(posStar))) {
                Integer number = getNumber(lines, idxline, posStar, Direction.UP);
                if (number!= null) { result.add(number); }
            }
            else {
                Integer number = getNumber(lines, idxline -1, posStar, Direction.LEFT);
                if (number!= null) { result.add(number); }
                number = getNumber(lines, idxline - 1, posStar, Direction.RIGHT);
                if (number!= null) { result.add(number); }
            }
        }
        Integer number = getNumber(lines, idxline, posStar, Direction.LEFT);
        if (number!= null) { result.add(number); }
        number = getNumber(lines, idxline, posStar, Direction.RIGHT);
        if (number!= null) { result.add(number); }

        if (idxline < lines.size() - 1) {
            String line = lines.get(idxline + 1);
            if (isDigit(line.charAt(posStar))) {
                number = getNumber(lines, idxline, posStar, Direction.DOWN);
                if (number != null) {
                    result.add(number);
                }
            } else {
                number = getNumber(lines, idxline + 1, posStar, Direction.LEFT);
                if (number != null) { result.add(number);}
                number = getNumber(lines, idxline + 1, posStar, Direction.RIGHT);
                if (number != null) { result.add(number); }
            }
        }
        return result.size() == 2 ? result : null;
    }

    public static Map<Integer, List<Integer>>  mapLine (List<String> lines, int idxline ) {
        Map<Integer, List<Integer>> mapStars = new HashMap<>();
        String line = lines.get(idxline);
        String regex = "\\*";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);
        while (matcher.find()) {
            int posStar = matcher.start();
            int indexStar = calcIndex(idxline, posStar, line.length());
            List<Integer> result = findNumbersAroundStar(lines, idxline, posStar);
            if (result != null && result.size() == 2 ) {
                 mapStars.put(indexStar, result);
            }
        }
        return mapStars.isEmpty() ? null : mapStars;
    }

    public static Map<Integer, List<Integer>>  mapStarAroundNumber(List<String> lines) {
        Map<Integer, List<Integer>> mapStars = new java.util.HashMap<>();
        IntStream.range(0, lines.size()).forEach(
                index -> {
                    Map<Integer, List<Integer>> mapLineStars = mapLine(lines, index);
                    if (mapLineStars != null) { mapStars.putAll(mapLineStars); }
                });
        return mapStars;
    }

    public static int computeGearRatios(List<String> lines) {
        Map<Integer, List<Integer>> mapStars =  mapStarAroundNumber(lines);
        displayMap(mapStars, lines.get(0).length());
        return mapStars.values()
                .stream()
                .mapToInt(
                        gearsList -> gearsList.stream()
                                .reduce(1 , (a, b) -> a * b))
                .sum();

    }

    public static void displayMap(Map<Integer, List<Integer>> mapStars, int lineSize ) {
        List<Integer> keys = new ArrayList<>(mapStars.keySet());
        Collections.sort(keys);
        for(Integer key : keys) {
            int line = key / lineSize;
            int column = key % lineSize;
            System.out.printf("l %d c %d (index %d):%s %n", line, column, key, mapStars.get(key));

        }
    }


}
