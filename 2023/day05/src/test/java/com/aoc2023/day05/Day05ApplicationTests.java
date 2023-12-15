package com.aoc2023.day05;

import com.aoc2023.day05.almanac.AlmanacMap;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class Day05ApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
	void part1() {
        AlmanacMap almanacMap = new AlmanacMap("src/main/resources/input.txt");
        long result =  almanacMap.lowestFromSeeds();
        assert result == 313045984L;
    }

}
