import java.util.Scanner;

public class Main{
  public static String solution(String s){
    String answer = "NO";
    s=s.toUpperCase().replaceAll("[^A-Z]", "");
    String tmp = new StringBuilder(s).reverse().toString();
    if(s.equals(tmp)) answer ="YES";
    return answer;
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String str = in.nextLine();
    
    System.out.println(solution(str));
    return ;
  }
}
