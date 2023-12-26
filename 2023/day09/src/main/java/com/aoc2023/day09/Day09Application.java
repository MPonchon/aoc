package com.aoc2023.day09;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Day09Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day09Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		Day day = new Day();
		day.run();
	}
}
