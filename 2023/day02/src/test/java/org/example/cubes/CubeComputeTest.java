package org.example.cubes;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.List;

import org.example.utils.*;

public class CubeComputeTest {

    CubeCompute cube;


    @Test
    public void result_Demo1_is_8() {
        List<String> data = Utils.loadExemple("demo1.txt");
        cube = new CubeCompute(data);
        assertEquals(8, cube.SumFor(12, 13, 14));
    }


    @Test
    public void result_Demo2_is_2286() {
        List<String> data = Utils.loadExemple("demo1.txt");
        cube = new CubeCompute(data);
        assertEquals(2286, cube.SumOfPower());
    }
}
