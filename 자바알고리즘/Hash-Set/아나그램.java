import java.util.*;

public class Main {
  public static String solution(String s1, String s2) {
    String answer ="YES";
    HashMap<Character, Integer> map = new HashMap<>();
    for (char x : s1.toCharArray()) {
      map.put(x, map.getOrDefault(x, 0) + 1); // map에 x라는 key가 있으면, key의 해당하는 value를 리턴하고, 없으면 0을 리턴
    }
    for (char x : s2.toCharArray()) {
      if(!map.containsKey(x) || map.get(x) ==0) return "NO";
      map.put(x, map.get(x) - 1);
    }
    
    return answer;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String a = in.next();
    String b = in.next();
    System.out.println(solution(a, b));
  }
}
