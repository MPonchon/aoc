import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import static org.example.Main.find_marker;

class mainTestTest {
    @Test
    void testFindMarker() {
        assertEquals(7 , find_marker( "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4));
        assertEquals (5 ,find_marker( "bvwbjplbgvbhsrlpgdmjqwftvncz", 4));
        assertEquals (6  ,find_marker( "nppdvjthqldpwncqszvftbrmjlhg", 4));
        assertEquals (10  ,find_marker( "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4));
        assertEquals (11  ,find_marker( "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4));
    }

    @Test
    void testFindMarker14() {
        assertEquals(19 , find_marker( "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14));
        assertEquals (23 ,find_marker( "bvwbjplbgvbhsrlpgdmjqwftvncz", 14));
        assertEquals (23  ,find_marker( "nppdvjthqldpwncqszvftbrmjlhg", 14));
        assertEquals (29  ,find_marker( "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14));
        assertEquals (26  ,find_marker( "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14));
    }
}