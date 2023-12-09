package org.example.question;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Calibration {

    public static Map<String, String> chiffres = new HashMap<>();
    static {
        chiffres.put("zero", "z0o");
        chiffres.put("one", "o1e");
        chiffres.put("two", "t2o");
        chiffres.put("three", "t3e");
        chiffres.put("four", "f4r");
        chiffres.put("five", "f5e");
        chiffres.put("six", "s6x");
        chiffres.put("seven", "s7n");
        chiffres.put("eight", "e8t");
        chiffres.put("nine", "n9e");
    }

    public static boolean containsKeyInString(String inputString) {
        for (String key : chiffres.keySet()) {
            if (inputString.contains(key)) {
                return true;
            }
        }
        return false;
    }

    public static int computeData( List<String> data) {
        int result = 0;
        for(String s : data) {
            String s2 = lettersToNumbers(s);
            s2 = extractNumbers(s2);
//            System.out.println("s2 parse " + s2);
            int n = Integer.parseInt(s2);
//            System.out.println("n: " + n);
            result += n;
        }
        return result;
    }

    private static String extractNumbers(String s2) {
//            System.out.println("s2 " + s2);
        if (s2.length() == 0) {
            s2 = "0";
        } else if (s2.length() > 2) {
            s2 =  "" + s2.charAt(0) + s2.charAt(s2.length()-1);
//                s2 = s2[0] +s2[1];
        }
        else if (s2.length() == 1) {
            s2 = s2 +s2;
        }
        return s2;
    }

    private static String lettersToNumbers(String s) {
        String s2 = s.replaceAll("\\D", "");
        return s2;
    }

    public static String lettersMixedToNumbers(String s) {
        String s2 = s;
        do {
            for (String key : chiffres.keySet()) {
                if (s2.contains(key)) {
                    s2 = s2.replaceAll(key, chiffres.get(key).toString());
                }
            }
        } while (containsKeyInString(s2));
        return s2;
    }


    public static int computeMixedData(List<String> data) {
        int somme = 0;
        for(String s : data) {
            String s2 = lettersMixedToNumbers(s);
            s2 = lettersToNumbers(s2);
            s2 = extractNumbers(s2);
            int n = Integer.parseInt(s2);
            somme += n;
        }
        return somme;
    }
}

