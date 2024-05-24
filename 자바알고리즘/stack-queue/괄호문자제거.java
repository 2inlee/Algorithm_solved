import java.util.*;

public class Main {
  public static String solution(String str) {
    StringBuilder answer = new StringBuilder();
    Stack<Character> stack = new Stack<>();
    
    for (char x : str.toCharArray()) {
      if (x == '(') {
        stack.push(x);
      } else if (x == ')') {
        while (stack.pop() != '('); // 여는 괄호를 만날 때까지 팝하고, 여는 괄호도 팝
      } else {
        if (stack.isEmpty()) {
          answer.append(x); // 스택이 비어 있을 때만 문자를 추가
        }
      }
    }
    return answer.toString();
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String str = in.next();
    System.out.print(solution(str));
  }
}
