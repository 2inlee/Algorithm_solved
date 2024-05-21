import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 학생 수 N과 테스트 횟수 M 입력 받기
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[][] tests = new int[M][N];

        // 테스트 결과 입력 받기
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                tests[i][j] = scanner.nextInt();
            }
        }

        // 멘토링 가능한 경우의 수 계산 및 출력
        int count = countMentoringPairs(N, M, tests);
        System.out.println(count);
    }

    public static int countMentoringPairs(int N, int M, int[][] tests) {
        int count = 0;

        // 모든 학생 쌍 (i, j)에 대해 멘토링 가능한지 확인
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i != j) {
                    boolean canMentor = true;
                    for (int k = 0; k < M; k++) {
                        int rankI = 0, rankJ = 0;
                        for (int s = 0; s < N; s++) {
                            if (tests[k][s] == i) rankI = s;
                            if (tests[k][s] == j) rankJ = s;
                        }
                        if (rankI > rankJ) {
                            canMentor = false;
                            break;
                        }
                    }
                    if (canMentor) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}
