import java.util.*;

public class Main {
  public static int solution(int n, int k, int[] sales) {
    int maxSales = 0;
    int windowSum = 0;

    // 초기 윈도우의 합 계산
    for (int i = 0; i < k; i++) {
      windowSum += sales[i];
    }
    maxSales = windowSum;

    // 슬라이딩 윈도우
    for (int i = k; i < n; i++) {
      windowSum += sales[i] - sales[i - k];
      if (windowSum > maxSales) {
        maxSales = windowSum;
      }
    }

    return maxSales;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int k = in.nextInt();
    int[] sales = new int[n];
    for (int i = 0; i < n; i++) {
      sales[i] = in.nextInt();
    }

    System.out.println(solution(n, k, sales));
  }
}
