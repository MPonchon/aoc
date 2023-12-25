package com.aoc2023.day08;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Day08Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day08Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		Day08 day08 = new Day08(8);
		day08.run();
	}
}
