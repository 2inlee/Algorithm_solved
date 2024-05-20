import java.util.*;
  
public class Main {
  
  public static int[] solution(int n){
    int[] result = new int[n];
    
    result[0] = 1;
    result[1] = 1;

    for(int i=2; i<n; i++){
      result[i] = result[i-1] + result[i-2];
    }

    return result;
  }


  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    int num = in.nextInt();

    
    int[] result = solution(num);
    for (int i = 0; i < result.length; i++) {
      if (i > 0) {
        System.out.print(" ");
      }
      System.out.print(result[i]);
    }
  }
}