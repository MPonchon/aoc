package org.example.cubes;

import java.util.*;

public class CubeCompute {

    private List<String> data;

    public CubeCompute(List<String> data) {
        this.data = data;
    }



    public int SumFor(int maxRed, int maxGreen, int maxBlue) {
//        System.out.println(this.data.size());
        Set<Integer> gameIds = new HashSet<>();
        int somme = 0;
        for(String line : this.data) {
            String[] parts = line.split(":");
            Integer gameId = Integer.parseInt(parts[0].replaceAll("\\D", ""));
            line = parts[1];
            String[] partRgb = line.split(";");
            boolean possible = true;
            for(String redgreenblue : partRgb) {
                String[] rgb = redgreenblue.split(",");
                for(String color : rgb) {
                    int n = Integer.parseInt(color.replaceAll("\\D", ""));
                    if (color.contains("red") && n > maxRed
                            || color.contains("green") && n > maxGreen
                            || color.contains("blue") && n > maxBlue) {
                        possible = false;
                    }
                }
            }
            if (possible) {
                somme += gameId;
            }
        }
        return somme;
    }

    public int SumOfPower(){
        Set<Integer> gameIds = new HashSet<>();
        int somme = 0;
        for(String line : this.data) {
            String[] parts = line.split(":");
            Integer gameId = Integer.parseInt(parts[0].replaceAll("\\D", ""));
            line = parts[1];
            String[] partRgb = line.split(";");
            boolean possible = true;
            // max color for the game
            int maxRed, maxGreen, maxBlue;
            maxRed = maxGreen = maxBlue = 0;
            for(String redgreenblue : partRgb) {
                String[] rgb = redgreenblue.split(",");
                for(String color : rgb) {
                    int n = Integer.parseInt(color.replaceAll("\\D", ""));
                    if (color.contains("red") && n > maxRed) { maxRed = n; }
                    if (color.contains("green") && n > maxGreen) { maxGreen = n; }
                    if (color.contains("blue") && n > maxBlue) { maxBlue = n; }
                }
            }
            int power = maxRed * maxGreen * maxBlue;

            somme += power;

        }
        return somme;
    }

}
