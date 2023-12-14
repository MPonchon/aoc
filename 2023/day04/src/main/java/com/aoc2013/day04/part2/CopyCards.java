package com.aoc2013.day04.part2;

import com.aoc2013.day04.cards.Cards;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

import static com.aoc2013.day04.cards.Cards.nbWonCards;


public class CopyCards {

    public static int totalScratchcards(String pathToFile) {
        List<List<List<Integer>>> allnumbers = Cards.loadData(pathToFile);
        List<List<Integer>> winningsList = allnumbers.get(0);
        List<List<Integer>> numbersList = allnumbers.get(1);
        Map<Integer, Integer> totalCopies = new HashMap<>();
        return IntStream.range(0, winningsList.size())
            .map( i -> {
                    int copiesOfActualCard = totalCopies.getOrDefault(i, 0);
                    List<Integer> winnings = winningsList.get(i);
                    List<Integer> numbers = numbersList.get(i);
                    int nbWons = nbWonCards(winnings, numbers);
                    for (int card = 1; card < nbWons+1; card++) {
                        int oldvalue = totalCopies.getOrDefault(card + i, 0);
                        totalCopies.put(card + i, oldvalue + 1 + copiesOfActualCard );
                    }
//                    System.out.println("i: "+ i + " totalCopies: " + totalCopies + " nbWons: " + nbWons);
                    return totalCopies.getOrDefault(i, 0) + 1;
                    })
            .sum();
    }
}
