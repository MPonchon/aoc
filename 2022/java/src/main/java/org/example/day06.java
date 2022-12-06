package org.example;
import java.io.File;
import java.io.FileNotFoundException;
import java.nio.file.Paths;
import java.util.*;

public class day06 {

    //    final static String filedata = "exemple_d06.txt";
    final static String filename = "input_d06.txt";
    final static String path_to_file = Paths.get(
            System.getProperty("user.dir"),
            "data",
            filename
    ).toString();

    public static void print(String ch) {
        System.out.println(ch);
    }

    protected static boolean markerFound(HashMap <String, Integer> counter) {
        for (String chaine : counter.keySet()) {
            Integer count = counter.get(chaine);
            if (count > 1) {
                return false;
            }
        }
        return true;
    }

    public static int find_marker(String input, int longueur) {
        int nb_chars = 0;
        String[] chaines = input.split("");
        Deque deque = new ArrayDeque();

        for (String ch: chaines) {
            deque.addFirst(ch);
            nb_chars++;
            if (deque.size() >= longueur) {
                HashMap <String, Integer> counter = new HashMap<>();
                deque.forEach( c1 -> {
                    counter.put((String) c1 , counter.getOrDefault(c1, 0) + 1);
                });
                if (markerFound(counter)) {
                    return nb_chars;
                }
                String c2 = (String) deque.pollLast();
            }
        }
        throw new IllegalArgumentException("find_marker: out of chars");
    }

    public static void run() {
//        System.out.println("Hello world!");
        print("path_to_file: "+ path_to_file);

        int taille = 4;  // part 1
        taille = 14;  // part 2
        Scanner scanner = null;
        try {
            File myfile = new File(path_to_file);
            scanner = new Scanner(myfile);
            while(scanner.hasNextLine()) {
                String filedata = scanner.nextLine();
                System.out.println(filedata);
                int nb_chars = find_marker(filedata, taille);
                System.out.println("nb_chars: "+ nb_chars);
            }
        }
        catch (FileNotFoundException e) {
            System.out.println("Exception: " + e.getMessage());
            scanner.close();
        }
    }
}
