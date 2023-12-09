package org.example.utils;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


import java.io.FileInputStream;
public class Utils {
    public static List<String> loadExemple(String cheminFichier) {
        List<String> lignes = new ArrayList<>();
        try {
//             Utilisez le ClassLoader pour obtenir un InputStream
//            ClassLoader classLoader = Utils.getClass().getClassLoader();
            ClassLoader classLoader = Utils.class.getClassLoader();
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
