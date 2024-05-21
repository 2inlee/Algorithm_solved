import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // N 입력 받기
        int N = scanner.nextInt();
        int[][] grid = new int[N + 2][N + 2]; // 가장자리를 0으로 초기화 하기 위해 +2 크기로 생성

        // 격자판 입력 받기 (가장자리는 0으로 유지)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                grid[i][j] = scanner.nextInt();
            }
        }

        // 봉우리의 개수 계산 및 출력
        int peakCount = findPeakCount(N, grid);
        System.out.println(peakCount);
    }

    public static int findPeakCount(int N, int[][] grid) {
        int count = 0;

        // 각 격자에 대해 상하좌우와 비교하여 봉우리 여부 확인
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (grid[i][j] > grid[i - 1][j] && 
                    grid[i][j] > grid[i + 1][j] && 
                    grid[i][j] > grid[i][j - 1] && 
                    grid[i][j] > grid[i][j + 1]) {
                    count++;
                }
            }
        }

        return count;
    }
}
