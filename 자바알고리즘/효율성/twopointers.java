import java.util.*;

public class Main {
  public static ArrayList<Integer> solution(int num1, int num2, int[] a, int[] b){
    ArrayList<Integer> answer = new ArrayList<>();
    int p1 = 0, p2 = 0;
    while (p1 < num1 && p2 < num2) {
      if (a[p1] < b[p2]) answer.add(a[p1++]);
      else answer.add(b[p2++]);
    }
    while (p1 < num1) answer.add(a[p1++]);
    while (p2 < num2) answer.add(b[p2++]);
    return answer;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int num1 = in.nextInt();
    int[] a = new int[num1];
    for (int i = 0; i < num1; i++) {
      a[i] = in.nextInt();
    }
    int num2 = in.nextInt();
    int[] b = new int[num2];
    for (int i = 0; i < num2; i++) {
      b[i] = in.nextInt();
    }
    for (int x : solution(num1, num2, a, b)) System.out.print(x + " ");
  }
}
