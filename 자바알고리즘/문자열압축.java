import java.util.Scanner;

public class Main {

  public static String solution(String str) {
    StringBuilder result = new StringBuilder();
    int cnt = 1;

    for (int i = 0; i < str.length(); i++) {
      if (i == 0) {
        result.append(str.charAt(i));
      } else {
        if (str.charAt(i) == str.charAt(i - 1)) {
          cnt++;
        } else {
         if (cnt > 1) {
          result.append(cnt);
        }
        result.append(str.charAt(i));
        cnt = 1;
        }
      }
  }

  if (cnt > 1) {
    result.append(cnt);
  }

  return result.toString();
  }

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    String str = kb.next();
    System.out.println(solution(str));
  }
}
