import java.util.*;

public class Main{
  
  public static int[] solution(int size, int n, int[] arr){
    int[] cache = new int[size];
    for(int x : arr){
      int pos = -1;
      for(int i=0; i<size; i++) if(x == cache[i]) pos=i;
      if(pos==-1){
        for(int i=size-1; i>=1; i--){
          cache[i] = cache[i-1];
        }
        cache[0]=x;
      }
      else{
        for(int i=pos; i>=1; i--){
          cache[i] = cache[i-1];
        }
        cache[0]=x;
      }
    }
    return cache;
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);

    int s = in.nextInt();
    int n = in.nextInt();
    int[] arr = new int[n];
    

    for(int i=0; i<n; i++){
      arr[i] = in.nextInt();
    }

    for(int x : solution(s, n, arr)){
      System.out.print(x + " ");
    }
  }
}