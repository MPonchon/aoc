package org.aoc;

import org.junit.jupiter.api.Test;

import static com.github.stefanbirkner.systemlambda.SystemLambda.tapSystemOut;
import static org.junit.jupiter.api.Assertions.*;

// https://github.com/stefanbirkner/system-lambda

class BaseDayTest {

    @Test
    void Should_display_empty_day() throws Exception {
        //Given
        BaseDay<Integer, Integer> baseDay = new BaseDay<Integer, Integer>(12);
        //When
        String outputText  = tapSystemOut(() -> {
            baseDay.run();
        });
        //Then
        StringBuilder sb = new StringBuilder();
        sb.append("AdventOfCode day: 12\n");
        sb.append("----------------------\n");
        sb.append("Part 1:\n");
        sb.append("- demo: null\n");
        sb.append("- result: null\n\n");
        sb.append("Part 2:\n");
        sb.append("- demo: null\n");
        sb.append("- result: null\n\n");
        assertEquals(sb.toString(), outputText);
    }

    @Test
    void result_part1_should_display() throws Exception {
        //Given
        BaseDay<Integer, Integer> baseDay = new BaseDay<Integer, Integer>(12);
        baseDay.setDemoPart1(25);
        baseDay.setPart1(125);
        //When
        String outputText  = tapSystemOut(() -> {
            baseDay.run();
        });
        //Then
        assertEquals(25, baseDay.getDemoPart1());
        assertEquals(125, baseDay.getPart1());

        StringBuilder sb = new StringBuilder();
        sb.append("AdventOfCode day: 12\n");
        sb.append("----------------------\n");
        sb.append("Part 1:\n");
        sb.append("- demo: 25\n");
        sb.append("- result: 125\n\n");
        sb.append("Part 2:\n");
        sb.append("- demo: null\n");
        sb.append("- result: null\n\n");
        assertEquals(sb.toString(), outputText);
    }

    @Test
    void result_part2_should_display() throws Exception {
        //Given
        BaseDay<Integer, Integer> baseDay = new BaseDay<Integer, Integer>(12);
        baseDay.setDemoPart2(25);
        baseDay.setPart2(125);
        //When
        String outputText  = tapSystemOut(() -> {
            baseDay.run();
        });
        //Then
        assertEquals(25, baseDay.getDemoPart2());
        assertEquals(125, baseDay.getPart2());

        StringBuilder sb = new StringBuilder();
        sb.append("AdventOfCode day: 12\n");
        sb.append("----------------------\n");
        sb.append("Part 1:\n");
        sb.append("- demo: null\n");
        sb.append("- result: null\n\n");

        sb.append("Part 2:\n");
        sb.append("- demo: 25\n");
        sb.append("- result: 125\n\n");
        assertEquals(sb.toString(), outputText);
    }
}