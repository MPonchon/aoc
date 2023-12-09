package com.example.day03.grid;

import java.util.List;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

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
}
