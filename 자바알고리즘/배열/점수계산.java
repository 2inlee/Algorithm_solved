import java.util.*;

public class Main {
  
  public static int solution(int n, int[] arr) {
    int score = 0;
    int cnt = 0;
    for(int i=0; i<n; i++){
      if(arr[i] == 1){
        cnt++;
        score += cnt;
      }else{
        cnt = 0;
      }
    }

    return score;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] arr = new int[n];
    for(int i=0; i<n; i++){
      arr[i] = in.nextInt();
    }

    System.out.println(solution(n, arr));
  }
}
