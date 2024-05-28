import java.util.*;

class Main {
  static String answer = "NO";
  static int n, total = 0;
  boolean flag = false;

  public void DFS(int L, int sum, int[] arr){
    if(flag) return;
    if(sum > total / 2) return;
    if(L == n){
      if((total - sum) == sum){
        answer = "YES";
        flag = true;
      }
    } else {
      DFS(L + 1, sum + arr[L], arr); // 여기서 sum을 직접 더해서 새로운 값으로 넘김
      DFS(L + 1, sum, arr); // 기존 sum 값 그대로 넘김
    }
  }

  public static void main(String[] args){
    Main T = new Main();
    Scanner in = new Scanner(System.in);
    n = in.nextInt(); // static 변수를 초기화해야 함
    int[] arr = new int[n];

    for(int i = 0; i < n; i++){
      arr[i] = in.nextInt();
      total += arr[i]; // total 값을 계산
    }
    T.DFS(0, 0, arr);
    System.out.println(answer);
  }
}
