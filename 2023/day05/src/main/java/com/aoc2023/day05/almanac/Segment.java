package com.aoc2023.day05.almanac;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Segment {
    private final Long _origin;
    private final Long _extremity;

    Segment(Long origin, Long extremity) {
        this._origin = origin;
        this._extremity = extremity - 1;
    }

    public static Segment createWithRange(Long origin, Long range) {
        return new Segment(origin, origin + range);
    }

    public Long o() { return _origin; }
    public Long e() { return _extremity + 1; }

    public Long size() { return _extremity - _origin + 1; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Segment segment)) return false;
        return Objects.equals(_origin, segment._origin) && Objects.equals(_extremity, segment._extremity);
    }

    @Override
    public int hashCode() {
        return Objects.hash(_origin, _extremity);
    }

    public boolean contains(Long value) {
        return value >= _origin && value <= _extremity;
    }

    public boolean overlap(Segment other) {
        return contains(other.e()) || contains(other.o());
    }

    @Override
    public String toString() {
        return "<" + _origin + "-" + _extremity + "<";
    }

    public static List<Segment> fragment(Segment current, Segment other) {
        List<Segment> result = new ArrayList<>();
        if (!current.overlap(other)) {
            result.add(current);
            result.add(other);
            return result;
        }
        // overlap
        // other on left
        if(!current.contains(other.o())) {
            result.add(new Segment(other.o(), current.o()));
            result.add(new Segment(current.o(), other.e()));
            result.add(new Segment(other.e(), current.e()));
            return result;
        }
        // overlap - other inside current
        if (current.contains(other.o()) && current.contains(other.e())) {
            result.add(new Segment(current.o(), other.o()));
            result.add(other);
            result.add(new Segment(other.e(), current.e()));
        }
        // overlap - other on right
        if (!current.contains(other.e())) {
            result.add(new Segment(current.o(), other.o()));
            result.add(new Segment(other.o(), current.e()));
            result.add(new Segment(current.e(), other.e()));
        }
        return result;
    }
}
