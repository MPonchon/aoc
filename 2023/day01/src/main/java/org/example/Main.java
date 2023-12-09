package org.example;

import org.example.question.Calibration;
import org.example.withstream.CalibrationStream;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        System.out.println("AOC day 01");
        String cheminFichier = "sample_demo.txt";

//        int result = Calibration.computeData(loadExemple(cheminFichier));
        int result = CalibrationStream.computeData(loadExemple(cheminFichier));
        System.out.println(cheminFichier + ": "+ result);

        cheminFichier = "input1.txt";
        result = Calibration.computeData(loadExemple(cheminFichier));
        System.out.println("rep 1:" + result);


        result = Calibration.computeMixedData(loadExemple(cheminFichier));
        System.out.println("rep 2: "+ result);

    }

    public static List<String> loadExemple(String cheminFichier) {
        List<String> lignes = new ArrayList<>();
        try {
            // Utilisez le ClassLoader pour obtenir un InputStream
            ClassLoader classLoader = Main.class.getClassLoader();
            InputStream inputStream = classLoader.getResourceAsStream(cheminFichier);

            if (inputStream != null) {
                // Utilisez BufferedReader pour lire le contenu du fichier
                try (BufferedReader lecteur = new BufferedReader(new InputStreamReader(inputStream))) {
                    String ligne;
                    while ((ligne = lecteur.readLine()) != null) {
                        lignes.add(ligne);
                    }
                }
            } else {
                System.out.println("Le fichier n'a pas été trouvé.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return lignes;
    }
}




