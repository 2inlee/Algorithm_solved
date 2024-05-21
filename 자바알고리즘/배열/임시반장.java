import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 학생 수 입력 받기
        int N = scanner.nextInt();
        int[][] classes = new int[N][5];

        // 각 학생의 반 정보 입력 받기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 5; j++) {
                classes[i][j] = scanner.nextInt();
            }
        }

        // 임시 반장 계산 및 출력
        int tempPresident = findTempPresident(N, classes);
        System.out.println(tempPresident);
    }

    public static int findTempPresident(int N, int[][] classes) {
        int maxCount = 0;
        int president = 0;

        // 각 학생별로 같은 반이었던 학생 수 계산
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (i != j) { // 자기 자신은 제외
                    for (int k = 0; k < 5; k++) {
                        if (classes[i][k] == classes[j][k]) {
                            count++;
                            break;
                        }
                    }
                }
            }
            // 가장 많은 학생과 같은 반이었던 학생을 임시 반장으로 선정
            if (count > maxCount) {
                maxCount = count;
                president = i + 1; // 학생 번호는 1부터 시작
            }
        }

        return president;
    }
}
