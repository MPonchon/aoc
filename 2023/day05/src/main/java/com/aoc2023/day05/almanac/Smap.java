package com.aoc2023.day05.almanac;

import java.util.ArrayList;
import java.util.List;

public class Smap {
    private Long dest, src, range;
    Smap(Long dest, Long src, Long range) {
        this.dest = dest;
        this.src = src;
        this.range = range;
    }

    Long destOrg() { return dest; }
    Long srcOrg() { return src; }
    Long getRange() { return range; }
    Long destExt() { return dest + range; }
    Long srcExt() { return src + range; }


    void merge(Long oDest, Long oSrc, Long oRange) {
        // 1ere borne inf
        if (this.dest + this.range < oSrc   // ajout new liste : pas de conflit
            || this.dest < oSrc) {   //idem
            return;
        }
        // conflits
        // cas 1 range > oRange
        if (oSrc < dest  && oSrc+oRange > dest && oSrc+oRange < dest + range) {

        }
        long deltaRange = this.range - oRange;
        long newDest = oDest + oRange;

    }

    public String toString() {
        return "dest : " + dest + ", src : " + src + ", range : " + range;
    }


    public static List<Smap> merge(Smap current, Smap other) {
        List<Smap> result = new ArrayList<>();
        // cas 1        ou    cas 2
        //       [--]   |   [--]
        // [--]         |         [--]
        if (current.destOrg() > other.destExt() || current.srcExt() < other.srcOrg()) {
            result.add(other);
            result.add(current);
            return result;
        }
        // cas 3
        //       [-----]
        //    [--#-]
        if (other.srcOrg() < current.destOrg() && other.srcExt() > current.destOrg() && other.srcExt() < current.destOrg()) {
            // [--#
            long deltaRange = current.destOrg() - other.srcOrg();
            result.add(new Smap(other.srcOrg(), current.srcOrg() - deltaRange, deltaRange));
            // #-]
            deltaRange = other.destExt() - current.destOrg();
            result.add(new Smap(current.destOrg(), other.srcOrg(), deltaRange));
            // ---]
            long deltaRange2 = current.destExt() - other.srcExt();
            result.add(new Smap(current.srcOrg() + deltaRange, current.srcOrg() - deltaRange, deltaRange));
            return result;
        }
        // cas 3
        //       [---]
        // [--]

        return result;
    }

    public record SmapPart(Long dest, Long src, Long range) {}
}
