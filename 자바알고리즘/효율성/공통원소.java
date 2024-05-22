import java.util.*;

public class Main {
  public static ArrayList<Integer> solution(int num1, int num2, int[] a, int[] b) {
    ArrayList<Integer> answer = new ArrayList<>();
    
    // 배열을 정렬
    Arrays.sort(a);
    Arrays.sort(b);

    int p1 = 0, p2 = 0;

    // 두 배열을 투 포인터로 순회하면서 공통 원소를 찾음
    while (p1 < num1 && p2 < num2) {
      if (a[p1] == b[p2]) {
        answer.add(a[p1]);
        p1++;
        p2++;
      } else if (a[p1] < b[p2]) {
        p1++;
      } else {
        p2++;
      }
    }

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

    ArrayList<Integer> result = solution(num1, num2, a, b);
    for (int x : result) {
      System.out.print(x + " ");
    }
  }
}
