import java.util.Scanner;

public class Main {
    static int n, m, answer = 0;
    static int[][] arr;

    public void DFS(int L, int time, int score) {
        if (time > m) return;
        if (L == n) {
            answer = Math.max(answer, score);
        } else {
            DFS(L + 1, time + arr[L][1], score + arr[L][0]);  // 현재 문제를 푸는 경우
            DFS(L + 1, time, score);  // 현재 문제를 풀지 않는 경우
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        arr = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            arr[i][0] = in.nextInt();  // 점수
            arr[i][1] = in.nextInt();  // 시간
        }
        
        T.DFS(0, 0, 0);
        System.out.println(answer);
    }
}
