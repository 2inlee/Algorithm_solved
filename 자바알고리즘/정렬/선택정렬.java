import java.util.Scanner;

public class Main {
  public static void solution(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
      int minIndex = i;
      for (int j = i + 1; j < n; j++) {
        if (arr[j] < arr[minIndex]) {
          minIndex = j;
        }
      }
      // Swap the found minimum element with the first element
      int temp = arr[minIndex];
      arr[minIndex] = arr[i];
      arr[i] = temp;
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int[] numbers = new int[N];
    for (int i = 0; i < N; i++) {
        numbers[i] = scanner.nextInt();
    }

    // 선택 정렬 수행
    solution(numbers);

    // 결과 출력
    for (int i = 0; i < N; i++) {
        System.out.print(numbers[i] + " ");
    }
  }
}
