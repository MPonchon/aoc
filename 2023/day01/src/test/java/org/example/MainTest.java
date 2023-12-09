package org.example;

import org.junit.Test;

import java.util.List;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.Is.is;


public class MainTest {

    @Test
    public void loadExemple_should_return_listString() {
        //Given
        final String repopath = "sample_demo.txt";

        //When
        List<String> mystrings = Main.loadExemple(repopath);

        //Then
        assertThat(mystrings.size(), is(equalTo(4)));
    }
}
