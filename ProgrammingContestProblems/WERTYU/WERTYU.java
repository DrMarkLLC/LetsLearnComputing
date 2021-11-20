import java.util.*;

/**
 * Java solution to the WERTYU Kattis problem.
 * 
 * Let's Learn Computing with Dr. Mark
 * 2021-11-20
 */
public class WERTYU {

    public static void main(String[] args) {
        // all key characters, in order, left to right, top to bottom row
        String keys = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
        // map to convert input to output
        Map<Character, Character> map = new HashMap<>();
        
        // load the map with shifted equivalents
        for(int i = 1; i < keys.length(); i++) {
            map.put(keys.charAt(i), keys.charAt(i - 1));
        }
        map.put(' ', ' '); // space is always a space
        
        // now process input
        Scanner stdin = new Scanner(System.in);
        
        while(stdin.hasNextLine()) {
            String line = stdin.nextLine();
            
            for(int i = 0; i < line.length(); i++) {
                System.out.print(map.get(line.charAt(i)));
            }
            System.out.println();
        }
        
        stdin.close();
    }
} // public class WERTYU