import java.util.*;

class Main {
  public void DFS(int n){
    if(n == 0){
      return ;
    }
    else{
      System.out.println(n);
      DFS(n-1);
    }
  }

  public static void main(String[] args){
    Main T = new Main();
    T.DFS(3);
  }
}