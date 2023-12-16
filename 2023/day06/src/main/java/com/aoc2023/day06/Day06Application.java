package com.aoc2023.day06;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import static com.aoc2023.day06.race.Race.part1;
import static com.aoc2023.day06.single.SingleRace.part2;

@SpringBootApplication
public class Day06Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day06Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("day06");

		int result = part1("src/main/resources/demo.txt");
		System.out.println("Demo result:" + result);

		result = part1("src/main/resources/input.txt");
		System.out.println("Part 1 result:" + result);
		/**
		 * day06
		 * Demo result:288
		 * Part 1 result:2756160
		 */
		long result2 = part2("src/main/resources/demo.txt");
		System.out.println("Demo Part 2 result:" + result2);

		result2 = part2("src/main/resources/input.txt");
		System.out.println("Part 2 result:" + result2);

	}
}
