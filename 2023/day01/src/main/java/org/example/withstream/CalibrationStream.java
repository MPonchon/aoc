package org.example.withstream;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toList;

public class CalibrationStream {

    public static int computeData( List<String> data) {
        return data.stream()
                .map(s -> s.replaceAll("\\D", ""))
//                .peek( s -> {
//                    System.out.println("s:" + s);
//                })
                .map(s -> s.length() == 1 ? s + s : s)
                .map(s -> s.length() > 2 ? s.charAt(0) + s.substring(s.length()-1) : s)
                .mapToInt(Integer::parseInt)
                .sum();
    }



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


    public static int computeMixedData(List<String> data) {

        data = data.stream()
                .map(s -> {
                    for (Map.Entry<String, String> entry : chiffres.entrySet()) {
                        s = s.replaceAll(entry.getKey(), entry.getValue());
                    }
                    return s;
                })
                .toList();

        return  computeData(data);

//        return data.stream()
//                .map(s -> {
//                    for (Map.Entry<String, String> entry : chiffres.entrySet()) {
//                        s = s.replaceAll(entry.getKey(), entry.getValue());
//                    }
//                    return s;
//                })
////                .peek( s -> {
////                    System.out.println("s:" + s);
////                })
//                .map(s -> s.replaceAll("\\D", ""))
////                .peek( s -> {
////                    System.out.println("s:" + s);
////                })
//                .map(s -> s.length() == 1 ? s + s : s)
//                .map(s -> s.length() > 2 ? s.charAt(0) + s.substring(s.length()-1) : s)
//                .mapToInt(Integer::parseInt)
//                .sum();
    }

}
