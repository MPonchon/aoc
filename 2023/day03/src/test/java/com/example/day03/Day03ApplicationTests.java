package com.example.day03.grid;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;
import java.util.ArrayList;
import com.example.day03.utils.Utils;

import static org.junit.jupiter.api.Assertions.*;
//import  com.example.day03.grid.Grid;

@SpringBootTest
class Day03ApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
    void find_numbers_adjentSymbol(){
		// Given
		List<String> lines = new ArrayList<>();
        lines.add("467..114..");
        lines.add("...*......");

		// When
		List<Integer> numbers = Grid.getAdjacentNumbers(lines);

		//Then
		assertTrue(numbers.contains(467));
		assertFalse(numbers.contains(114));
    }
}
