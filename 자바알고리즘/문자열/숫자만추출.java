import java.util.Scanner;

public class Main{
  public static int solution(String str){
    String answer = "";

    for(char x : str.toCharArray()){
      if (Character.isDigit(x)) answer+= x;
    }
    return Integer.parseInt(answer);
  }
 

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String str = in.next();
    
    System.out.println(solution(str));
    return ;
  }
}