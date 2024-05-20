import java.util.*;

public class Main {
  public static int solution(int n, int[] arr) {
    int largest = arr[0]; // 첫 번째 학생의 키로 초기화
    int cnt = 1; // 첫 번째 학생은 항상 보임

    for (int i = 1; i < n; i++) {
      if (arr[i] > largest) {
        largest = arr[i]; // 새로운 가장 큰 키로 업데이트
        cnt++; // 보이는 학생 수 증가
      }
    }
    return cnt;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = in.nextInt();
    }
    System.out.println(solution(n, arr));
  }
}
