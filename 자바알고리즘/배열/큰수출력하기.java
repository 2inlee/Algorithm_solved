import java.util.*;
  
public class Main {
  public static ArrayList<Integer> solution(int n, int[] arr) {
    ArrayList<Integer> answer = new ArrayList<>();
    answer.add(arr[0]);
    for(int i=1; i<n; i++){
      if(arr[i] > arr[i-1]) answer.add(arr[i]); 
    }

    return answer;
  }
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    int n = in.nextInt();
    int[] arr = new int[n];

    for(int i=0; i<n; i++){
      arr[i]=in.nextInt();
    }
    for(int x : solution(n, arr)){
      System.out.print(x+" ");
    }
    return ;
  }
}