import java.util.Scanner;

public class Main {

  public static String solution(String str) {
    String answer = "";
    int m = Integer.MIN_VALUE;

    String[] words = str.split(" ");
    for (String word : words) {
      int len = word.length();
      if (len > m) {
        m = len;
        answer = word;
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    String str = kb.nextLine();
    System.out.println(solution(str));
    kb.close();
  }
}
