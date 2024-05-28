import java.util.*;

public class Main {
    static int n, m, answer = Integer.MAX_VALUE;
    static Integer[] arr;

    public void DFS(int L, int sum) {
        if (sum > m) return; // 이미 sum이 m보다 큰 경우 cut-edge
        if(L>answer) return;
        if (sum == m) {
            answer = Math.min(answer, L);
        } else {
            for (int i = 0; i < n; i++) {
                DFS(L + 1, sum + arr[i]);
            }
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        
        arr = new Integer[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        Arrays.sort(arr, Collections.reverseOrder()); // 내림차순 정렬
        m = in.nextInt();
        T.DFS(0, 0);
        System.out.println(answer);
    }
}
