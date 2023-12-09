package org.example.question;

import org.example.Main;
import org.junit.Test;

import java.util.List;


import static org.junit.Assert.assertThat;
import static org.testng.AssertJUnit.assertEquals;

public class CalibrationTest {

    @Test
    public void result_with_demo_is_142() {
        //Given
        List<String> myStrings = Main.loadExemple("sample_demo.txt");

        //When
        int result = Calibration.computeData(myStrings);
        //Then
        assertEquals(142, result);
    }

    @Test
    public void result_with_demo2_is_281() {
        //Given
        List<String> myStrings = Main.loadExemple("sample_demo2.txt");

        //When
        int result = Calibration.computeMixedData(myStrings);
        //Then
        assertEquals(281, result);
    }


    @Test
    public void lettersMixedToNumbers_return_1_with_number_one() {
        //Given
        String s ="onetotohello";
        //When
        String n = Calibration.lettersMixedToNumbers(s);
        //Then
        assertEquals("o1etotohello", n);
    }

    @Test
    public void lettersMixedToNumbers_return_1_with_multi_number_one() {
        //Given
        String s ="onetoonetohelonelo";
        //When
        String n = Calibration.lettersMixedToNumbers(s);
        //Then
        assertEquals("o1etoo1etohelo1elo", n);
    }

    @Test
    public void lettersMixedToNumbers_return_19_with_two1nine() {
        //Given
        String s ="two1nine";
        //When
        String n = Calibration.lettersMixedToNumbers(s);
        //Then
        assertEquals("t2o1n9e", n);
    }

    @Test
    public void lettersMixedToNumbers_return_823_with_eightwothree() {
        //Given
        String s ="eightwothree";
        //When
        String n = Calibration.lettersMixedToNumbers(s);
        //Then
        assertEquals("e8t2ot3e", n);
    }
}
