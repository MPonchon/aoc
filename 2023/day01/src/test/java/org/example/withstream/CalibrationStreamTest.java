package org.example.withstream;

import org.example.Main;
import org.example.question.Calibration;
import org.junit.Test;

import java.util.List;

import static org.testng.AssertJUnit.assertEquals;

public class CalibrationStreamTest {

    @Test
    public void result_with_demo_is_142() {
        //Given
        List<String> myStrings = Main.loadExemple("sample_demo.txt");

        //When
        int result = CalibrationStream.computeData(myStrings);
        //Then
        assertEquals(142, result);
    }


    @Test
    public void result_with_demo2_is_281() {
        //Given
        List<String> myStrings = Main.loadExemple("sample_demo2.txt");

        //When
        int result = CalibrationStream.computeMixedData(myStrings);
        //Then
        assertEquals(281, result);
    }

}
