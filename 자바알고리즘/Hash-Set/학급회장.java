import java.util.*;

public class Main {
  public static char solution(int n, String s) {
    char answer = ' ';
    HashMap<Character, Integer> map = new HashMap<>();
    for (char x : s.toCharArray()) {
      map.put(x, map.getOrDefault(x, 0) + 1); // map에 x라는 key가 있으면, key의 해당하는 value를 리턴하고, 없으면 0을 리턴
    }
    int max = 0; // Integer.MIN_VALUE 대신 0으로 초기화
    for (char x : map.keySet()) { // keySet -> 존재하는 key들을 전부 탐색
      if (map.get(x) > max) {
        max = map.get(x);
        answer = x;
      }
    }
    return answer;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    String str = in.next();
    System.out.println(solution(n, str));
  }
}
