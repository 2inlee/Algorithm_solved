import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // N 입력 받기
        int N = scanner.nextInt();
        int[][] grid = new int[N][N];

        // 격자판 입력 받기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid[i][j] = scanner.nextInt();
            }
        }

        // 최대 합 계산 및 출력
        int maxSum = findMaxSum(N, grid);
        System.out.println(maxSum);
    }

    public static int findMaxSum(int N, int[][] grid) {
        int maxSum = 0;

        // 각 행의 합 계산
        for (int i = 0; i < N; i++) {
            int rowSum = 0;
            for (int j = 0; j < N; j++) {
                rowSum += grid[i][j];
            }
            if (rowSum > maxSum) {
                maxSum = rowSum;
            }
        }

        // 각 열의 합 계산
        for (int j = 0; j < N; j++) {
            int colSum = 0;
            for (int i = 0; i < N; i++) {
                colSum += grid[i][j];
            }
            if (colSum > maxSum) {
                maxSum = colSum;
            }
        }

        // 첫 번째 대각선의 합 계산 (좌상단에서 우하단)
        int diag1Sum = 0;
        for (int i = 0; i < N; i++) {
            diag1Sum += grid[i][i];
        }
        if (diag1Sum > maxSum) {
            maxSum = diag1Sum;
        }

        // 두 번째 대각선의 합 계산 (우상단에서 좌하단)
        int diag2Sum = 0;
        for (int i = 0; i < N; i++) {
            diag2Sum += grid[i][N - 1 - i];
        }
        if (diag2Sum > maxSum) {
            maxSum = diag2Sum;
        }

        return maxSum;
    }
}
