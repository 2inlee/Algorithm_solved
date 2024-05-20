import java.util.Scanner;
import java.util.HashSet;

public class Main {
  public static String solution(String str){
    HashSet<Character> seen = new HashSet<>();
    StringBuilder result = new StringBuilder();

    for(char c : str.toCharArray()){
      if(!seen.contains(c)){
        seen.add(c);
        result.append(c);
      }
    }
    
    return result.toString();
  }

  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    String str = in.next();
    
    System.out.println(solution(str));
    return ;
  }
}
