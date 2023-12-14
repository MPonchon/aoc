package org.aoc.utils;

import static org.junit.jupiter.api.Assertions.*;

class UtilsTest {

    @org.junit.jupiter.api.Test
    void loadFile_should_load_strings() {
        // Given
        String pathToFile = "src/main/resources/demo.txt";
        //When
        var lines = Utils.loadFile(pathToFile);

        //Then
        assertEquals(3, lines.size());

    }

}