package com.aoc2023.day07;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Day07Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day07Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		Day07 day07 = new Day07();
		day07.run();
	}
}
