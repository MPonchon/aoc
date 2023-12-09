package org.example;

import java.util.List;
import org.example.utils.*;
import org.example.cubes.*;

public class Main {
    /**
     * Determine which games would have been possible if the bag had been loaded with only
     * 12 red cubes, 13 green cubes, and 14 blue cubes
     *
     * @param args
     */
    public static void main(String[] args) {

        System.out.println("Day 2");

        List<String> data = Utils.loadExemple("input.txt");
        CubeCompute cube = new CubeCompute(data);
        int somme = cube.SumFor(12, 13, 14);
        System.out.println("la somme: " + somme);

        somme = cube.SumOfPower();
        System.out.println("part 2: " + somme);

    }
}