package org.example.utils;


import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.*;

public class UtilsTest {

    @Test
    public void test_load_file() {
        // Given

        //When
        List<String> data = Utils.loadExemple("demo1.txt");

        // Then
        assertEquals(5, data.size());
    }
}
