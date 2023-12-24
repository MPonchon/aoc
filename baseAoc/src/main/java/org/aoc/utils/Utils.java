package org.aoc.utils;


import java.io.FileNotFoundException;
import java.sql.SQLOutput;
import java.util.List;
import java.util.ArrayList;
import java.io.File;
import java.util.Scanner;

public class Utils {

    public static String DEMO_PATH = "src/main/resources/demo.txt";
    public static String INPUT_PATH = "src/main/resources/input.txt";

    public static List<String> loadFile(String pathToFile) {
        List<String> lines = new ArrayList<>();
        try {
            Scanner input = new Scanner(pathToFile);
            File file = new File(input.nextLine());
            input = new Scanner(file);
            while (input.hasNextLine()) {
                String line = input.nextLine();
                if (line.length() > 0) lines.add(line);
            }
            input.close();
        } catch (FileNotFoundException ex) {
            System.out.println("File not found " + pathToFile);
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return lines;
    }
}
