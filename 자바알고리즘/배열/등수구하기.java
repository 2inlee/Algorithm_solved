import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 학생 수 입력 받기
        int n = scanner.nextInt();
        int[] scores = new int[n];

        // 점수 입력 받기
        for (int i = 0; i < n; i++) {
            scores[i] = scanner.nextInt();
        }

        // solution 함수 호출하여 등수 계산
        int[] ranks = solution(n, scores);

        // 결과 출력
        for (int rank : ranks) {
            System.out.print(rank + " ");
        }
    }

    public static int[] solution(int n, int[] scores) {
        int[] ranks = new int[n];

        // 각 학생의 등수를 계산
        for (int i = 0; i < n; i++) {
            int rank = 1; // 초기 등수는 1등
            for (int j = 0; j < n; j++) {
                if (scores[j] > scores[i]) {
                    rank++;
                }
            }
            ranks[i] = rank;
        }

        return ranks;
    }
}
