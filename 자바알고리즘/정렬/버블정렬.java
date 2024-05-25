import java.util.*;

public class Main{
  
  public static int[] solution(int n, int[] arr){
    int tmp = 0;
    for(int i=0; i<n-1; i++){
      for(int j=i+1; j<n; j++){
        if (arr[j] < arr[i]){
          tmp = arr[i];
          arr[i] = arr[j];
          arr[j] = tmp;
        }

      }
    }
    return arr;
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int[] arr = new int[n];

    for(int i=0; i<n; i++){
      arr[i] = in.nextInt();
    }

    for(int x : solution(n, arr)){
      System.out.print(x + " ");
    }
  }
}