package com.example.day03.utils;

import java.util.List;
import java.util.ArrayList;
import java.io.File;
import java.util.Scanner;

public class Utils {

    public static List<String> loadFile(String pathToFile) {
        List<String> lines = new ArrayList<>();
        try {
            Scanner input = new Scanner(pathToFile);
            File file = new File(input.nextLine());
            input = new Scanner(file);
            while (input.hasNextLine()) {
                String line = input.nextLine();
                if (line.length() > 0)    lines.add(line);
            }
            input.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return lines;

    }
}
