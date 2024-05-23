import java.util.*;

public class Main {
    public static int findAnagrams(String s, String t) {
        int answer = 0;
        HashMap<Character, Integer> tMap = new HashMap<>();
        HashMap<Character, Integer> sMap = new HashMap<>();
        
        // Initialize the map for T
        for (char c : t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
        
        int tLength = t.length();
        
        // Initialize the map for the first window of S
        for (int i = 0; i < tLength - 1; i++) {
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
        }
        
        // Use sliding window to check all possible substrings of length t.length()
        int left = 0;
        for (int right = tLength - 1; right < s.length(); right++) {
            // Add the rightmost character of the window
            sMap.put(s.charAt(right), sMap.getOrDefault(s.charAt(right), 0) + 1);
            
            // Compare the maps
            if (sMap.equals(tMap)) {
                answer++;
            }
            
            // Remove the leftmost character of the window
            sMap.put(s.charAt(left), sMap.get(s.charAt(left)) - 1);
            if (sMap.get(s.charAt(left)) == 0) {
                sMap.remove(s.charAt(left));
            }
            left++;
        }
        
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        String t = scanner.nextLine();
        System.out.println(findAnagrams(s, t));
    }
}
