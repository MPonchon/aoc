package com.example.day03;

import com.example.day03.grid.Grid;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.List;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import com.example.day03.utils.Utils;



@SpringBootApplication
public class Day03Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Day03Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("Demo");
		List<String> lines = Utils.loafFile("src/main/resources/demo.txt");
		int sum = Grid.sumParts(lines);
		System.out.println("sum " + sum);


		System.out.println("part1");
		lines = Utils.loafFile("src/main/resources/input.txt");
		sum = Grid.sumParts(lines);
		System.out.println("sum " + sum);

	}

}
