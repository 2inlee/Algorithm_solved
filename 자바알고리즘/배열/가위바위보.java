import java.util.Scanner;

public class Main {

    public static char solution(int a, int b){
        // 가위바위보 규칙에 따라 승자를 결정
        if (a == b) {
            return 'D'; // 비긴 경우
        } else if ((a == 1 && b == 3) || (a == 2 && b == 1) || (a == 3 && b == 2)) {
            return 'A'; // A가 이긴 경우
        } else {
            return 'B'; // B가 이긴 경우
        }
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int[] a = new int[n];
        int[] b = new int[n];

        for(int i = 0; i < n; i++){
            a[i] = in.nextInt();
        }

        for(int i = 0; i < n; i++){
            b[i] = in.nextInt();
        }

        for(int i = 0; i < n; i++){
            System.out.println(solution(a[i], b[i]));
        }
        
        in.close();
    }
}
