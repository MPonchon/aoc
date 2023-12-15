package com.aoc2023.day05;

import com.aoc2023.day05.almanac.AlmanacMap;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Day05Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day05Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("day05");
		long result = 0;

		AlmanacMap almanacMap = new AlmanacMap("src/main/resources/demo.txt");
		result =  almanacMap.lowestFromSeeds();
		System.out.println("demo result:" + result);


		almanacMap = new AlmanacMap("src/main/resources/input.txt");
		result =  almanacMap.lowestFromSeeds();
		System.out.println("part1 result:" + result);

		/**
		 * day05
		 * demo result:35
		 * part1 result:313045984
		 */
		almanacMap = new AlmanacMap("src/main/resources/demo.txt");
		result =  almanacMap.lowestFromLocationPart2();
		System.out.println("demo2 result:" + result);

		almanacMap = new AlmanacMap("src/main/resources/input.txt");
		result =  almanacMap.lowestFromLocationPart2();
		System.out.println("part2 result:" + result);

	}
}
