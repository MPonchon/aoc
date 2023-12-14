package com.aoc2013.day04;

import com.aoc2013.day04.cards.Cards;
import com.aoc2013.day04.part2.CopyCards;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Day04Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day04Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("day04 part1");

		int result = Cards.computeWorthPointFromData("src/main/resources/demo.txt");
		System.out.println("Demo result:" + result);

		result = Cards.computeWorthPointFromData("src/main/resources/input.txt");
		System.out.println("Part 1 result:" + result);
		/**
		 * Demo result:13
		 * Part 1 result:18653
		 */

		// part2
		result = CopyCards.totalScratchcards("src/main/resources/input.txt");
		System.out.println("Part 2 result:" + result);

		/**
		 * day04 part1
		 * Demo result:13
		 * Part 1 result:18653
		 * Part 2 result:5921508
		 */
	}
}
