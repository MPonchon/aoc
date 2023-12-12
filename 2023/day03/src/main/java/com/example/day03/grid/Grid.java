package com.example.day03.grid;

import com.example.day03.dir.Direction;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

public class Grid {
    static final int NumberSize = 3;

    public static List<Integer> getAdjacentNumbers(List<String> lines) {
        List<Integer> numbers = new ArrayList<>();
        String regex = "\\d+";
        Pattern pattern = Pattern.compile(regex);

        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
//            System.out.println("i: " + i + " line: " + line);
            Matcher matcher = pattern.matcher(line);
            // Vérifier s'il y a une correspondance
            while (matcher.find()) {
                String nombreTrouve = line.substring(matcher.start(), matcher.end());
//                System.out.println("check fot nombreTrouve: " + nombreTrouve);
                int posStart = matcher.start() == 0 ? 0 :  matcher.start() - 1;
//                System.out.println("matcher.end(): " + matcher.end() + " line.length(): " + line.length() + " posStart: " + posStart);
                int posFin = matcher.end() == line.length()  ?  matcher.end()  : matcher.end() + 1;
//                System.out.println("posStart: " + posStart + " posFin: " + posFin + " nombreTrouve: " + nombreTrouve + " line :"  + line);
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
//                System.out.println("i: " + i + " line: " + line + " -> char = " + thechar);
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

    // ----------------

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
            String line = lines.get(pos).substring(posStar - Grid.NumberSize, posStar);
            result = findFirstNumber(line);
        }
        else if (dir == Direction.RIGHT && posStar < lines.get(0).length() - Grid.NumberSize) {
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

    public static List<Integer> getStarAroundNumber(
            List<String> lines, int pos , Map<Integer, List<Integer>> stars ) {
        List<Integer> result = null;
        String regex = "\\*";
        Pattern pattern = Pattern.compile(regex);

        String line = lines.get(pos);
        Matcher matcher = pattern.matcher(line);
        while (matcher.find()) {
            int posStar = matcher.start();
            int indexStar = calcIndex(pos, posStar, line.length());
            if (stars.containsKey(posStar)) { return null; }
            result = new ArrayList<>(3);
            result.add(indexStar);
            if (pos > 0 ) {
                addNumberToList(result, getNumberAbove(lines, pos, posStar));
            }
            addNumberToList(result, getNumber(lines, pos, posStar, Direction.LEFT));
            addNumberToList(result, getNumber(lines, pos, posStar, Direction.RIGHT));
            addNumberToList(result, getNumberBellow(lines, pos, posStar));
            if (result.size() == 3 ) return  result;
        }
        if (result != null && result.size() == 3 ) return result;
        return null;
    }
    public static void addNumberToList(List<Integer> numbers, Integer number) {
        if (number!= null) { numbers.add(number);}
    }

    public static Map<Integer, List<Integer>>  mapStarAroundNumber(List<String> lines) {
        Map<Integer, List<Integer>> mapStars = new java.util.HashMap<>();
        IntStream.range(0, lines.size())
                .forEach(index -> {
//                    String line = lines.get(index);
//                    System.out.println("Index: " + index + ", line: " + line);
                    List<Integer> starAndNumbers = getStarAroundNumber(lines, index, mapStars);
                    if (starAndNumbers!= null) {
                        mapStars.put(starAndNumbers.get(0), starAndNumbers.subList(1, 3));
                    }
                });

        return mapStars;
    }

    public static int computeGearRatios(List<String> lines) {
        Map<Integer, List<Integer>> mapStars = new java.util.HashMap<>();
        int somme = 0;
        IntStream.range(0, lines.size())
                .forEach(index -> {
//                    String line = lines.get(index);
//                    System.out.println("Index: " + index + ", line: " + line);
                    List<Integer> starAndNumbers = getStarAroundNumber(lines, index, mapStars);
                    if (starAndNumbers!= null) {
                        int ratio = starAndNumbers.get(1) / starAndNumbers.get(2);
                        //   mapStars.put(starAndNumbers.get(0), starAndNumbers.subList(1, 3));
                        somme += ratio;
                    }
                });

        return somme;
    }


}
