package com.aoc2023.day05.almanac;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class SegmentTest {

    @Test
    void fragment_outside_left() {
        //Given
        final Segment current = new Segment(10L,20L);
        final Segment other = new Segment(2L,4L);
        //When
        List<Segment> result = Segment.fragment(current, other);
        //Then
        assertEquals(2, result.size());
    }

    @Test
    void fragment_outside_right() {
        //Given
        final Segment current = new Segment(10L,20L);
        final Segment other = new Segment(22L,24L);
        //When
        List<Segment> result = Segment.fragment(current, other);
        //Then
        assertEquals(2, result.size());
    }

    @Test
    void fragment_inside_left() {
        //Given
git branch         final Segment current = new Segment(10L,20L);
        final Segment other = new Segment(8L,14L);
        //When
        List<Segment> result = Segment.fragment(current, other);
        //Then
        assertEquals(3, result.size());
        System.out.println("result: " + result);
        assertEquals(new Segment(8L,10L), result.get(0)); ;
        assertEquals(new Segment(10L,14L), result.get(1)); ;
        assertEquals(new Segment(14L,20L), result.get(2)); ;
    }

    @Test
    void fragment_inside_inside() {
        //Given
        final Segment current = new Segment(10L,20L);
        final Segment other = new Segment(12L,14L);
        //When
        List<Segment> result = Segment.fragment(current, other);
        //Then
        assertEquals(3, result.size());
        System.out.println("result: " + result);
        assertEquals(new Segment(10L,12L), result.get(0)); ;
        assertEquals(new Segment(12L,14L), result.get(1)); ;
        assertEquals(new Segment(14L,20L), result.get(2)); ;
    }

    @Test
    void fragment_inside_right() {
        //Given
//        final Segment current = new Segment(10L,20L);
        final Segment current = Segment.createWithRange(10L, 10L);
        final Segment other = new Segment(12L,22L);
        //When
        List<Segment> result = Segment.fragment(current, other);
        //Then
        assertEquals(3, result.size());
        System.out.println("result: " + result);
        assertEquals(new Segment(10L,12L), result.get(0)); ;
        assertEquals(new Segment(12L,20L), result.get(1)); ;
        assertEquals(new Segment(20L,22L), result.get(2)); ;
    }

    @Test
    void contains_limits() {
        //Given
        final Segment current =  new Segment(10L, 20L);
        //When
        assertTrue(current.contains(10L));
        assertTrue(current.contains(19L));
        assertFalse(current.contains(20L));
    }

    @Test
    void create_with_range_check_limits() {
        //Given
        final Segment current =  new Segment(10L, 20L);
        //When
        final Segment result = Segment.createWithRange(10L, 10L);
        //Then
        assertEquals(current, result);
        assertEquals(10, result.size());
        assertEquals(10, current.size());
        assertTrue(result.contains(19L));
        assertFalse(result.contains(20L));
        assertTrue(current.contains(19L));
        assertFalse(current.contains(20L));
    }
}