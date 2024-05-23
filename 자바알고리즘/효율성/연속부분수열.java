import java.util.*;

public class Main {
  public static int solution(int n, int m, int[] arr) {
    int answer=0, sum=0, lt=0;
    for(int rt=0; rt<n; rt++){
      sum+=arr[rt];
      if(sum==m) answer++;
      while(sum >m){
        sum-=arr[lt++];
        if(sum == m) answer++;
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int m = in.nextInt();
    int[] arr = new int[n];
    for(int i=0; i<n; i++){
      arr[i] = in.nextInt();
    }

    System.out.println(solution(n,m,arr));
    
  }
}
