import java.util.Scanner;

public class Main{
  public static String solution(String str){
    String answer = "YES";
    str = str.toUpperCase();
    int len = str.length();
    for(int i=0; i<len/2; i++){
      if(str.charAt(i) != str.charAt(len-i-1)) return "NO";
    }
    return answer;
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String str = in.next();
    
    System.out.println(solution(str));
    return ;
  }
}
