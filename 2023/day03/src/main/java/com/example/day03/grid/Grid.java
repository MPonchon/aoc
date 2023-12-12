package com.example.day03.grid;

import java.util.List;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

public class Grid {

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

                List<String> window = getWindow(lines, line, posStart, posFin);
                if (symbolAround(window, null) != null){
                    numbers.add(Integer.parseInt(nombreTrouve));
                }

            }
        }
        return numbers;
    }


    public static Coord symbolAround(List<String> window, Character symbol) {
        for(int i = 0; i < window.get(0).length(); i++) {
            for (String line : window) {
                Character thechar = line.charAt(i);
//                System.out.println("i: " + i + " line: " + line + " -> char = " + thechar);
                if (symbol == null && (thechar != '.' && (thechar < '0' || thechar > '9'))) {
                    return new Coord(i, window.indexOf(line));
                } else {
                    if (symbol == thechar) return new Coord(i, window.indexOf(line));
                }
            }
        }
        return null;
    }

    public static int sumParts(List<String> lines) {
        List<Integer> numbers =  getAdjacentNumbers(lines);

        return numbers.stream()
                .mapToInt(Integer::intValue)
                .sum();
    }

    private static List<String> getWindow(List<String> lines, String line, int posStart, int posFin) {
        List<String> window = new ArrayList<>();
        int i = lines.indexOf(line);

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
        return window;
    }

    // --- part 2
    public static List<Integer> getGearsInWindow(List<String> lines) {
//        List<Integer> gears = new ArrayList<>();
        List<String> window = null;
        // 1- find all star with gears
        Map<Coord, List<Integer>> mapStars = new HashMap<>();
        for(int i = 0; i < lines.size() - 2; i++) {
            window = lines.subList(i, i + 3);
            findGearsInWindow(window, mapStars);
        }

    }

    public static void findGearsInWindow(List<String> window, Map<Coord, List<Integer>> mapStars ) {
        List<Integer> numbers = new ArrayList<>();

        String regexStar = "\\*";
        Pattern patternStar = Pattern.compile(regexStar);
        window.forEach(line -> {
            Matcher matcherStar = patternStar.matcher(line);
            while (matcherStar.find()) {
                int posStar = matcherStar.start();
                //Coord coordStar = new Coord(posStar, window.indexOf(line));
                List<Integer> gears = getNumbersAroundStar(window, line, posStar);

                if (symbolStarAround(windowStar) ){
                    numbers.add(Integer.parseInt(nombreTrouve));
                }

            }
        });
        return numbers;
    }

    static List<Integer> getNumbersAroundStar(List<String> window, String line, posStar){
        Coord s = symbolAround(window, '*');

    }

//    public static List<Integer> getGearsInLinesOrNull(List<String> lines) {
//        List<Integer> numbers = new ArrayList<>();
//        String regex = "\\d+";
//        Pattern pattern = Pattern.compile(regex);
//        lines.forEach(line -> {
//            Matcher matcher = pattern.matcher(line);
//            while (matcher.find()) {
//                String nombreTrouve = line.substring(matcher.start(), matcher.end());
//                int posStart = matcher.start() == 0 ? 0 :  matcher.start() - 1;
//                int posFin = matcher.end() == line.length()  ?  matcher.end()  : matcher.end() + 1;
//
//                List<String> window = getWindow(lines, line, posStart, posFin);
//                if (symbolStarAround(window) ){
//                    numbers.add(Integer.parseInt(nombreTrouve));
//                }
//
//            }
//        });
//        return numbers.size() == 0 ? null : numbers;
//    }

//    public static boolean symbolStarAround(List<String> window) {
//        for (int i = 0; i < window.get(0).length(); i++) {
//            for (String line : window) {
//                Character thechar = line.charAt(i);
//                if (thechar == '*') {
//                    return true;
//                }
//            }
//        }
//        return false;
//    }

}


@Getter
@Setter
@AllArgsConstructor
class Coord {
    int x;
    int y;
}
