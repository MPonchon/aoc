package com.aoc2013.day04;

import com.aoc2013.day04.cards.Cards;
import com.aoc2013.day04.part2.CopyCards;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class Day04ApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
	void part1_should_return_xxx() {
		assertEquals(18653, Cards.computeWorthPointFromData("src/main/resources/input.txt"));

	}

}
