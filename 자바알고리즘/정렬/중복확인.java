import java.util.*;

public class Main{
  
  public static String solution(int n, int[] arr){
    String answer = "U";
    Arrays.sort(arr);
    for(int i=0; i<n-1; i++){
      if(arr[i] == arr[i+1]) return "D";
    }
    return answer;
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int[] arr = new int[n];
    

    for(int i=0; i<n; i++){
      arr[i] = in.nextInt();
    }

    System.out.print(solution(n, arr));
  }
}