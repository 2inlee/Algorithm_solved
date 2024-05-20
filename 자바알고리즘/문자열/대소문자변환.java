import java.util.Scanner;
  
public class Main {

  public static String swapCase(String str) {
    StringBuilder result = new StringBuilder();
    
    for (char x : str.toCharArray()) {
      if (Character.isUpperCase(x)) {
        result.append(Character.toLowerCase(x));
        } else {
          result.append(Character.toUpperCase(x));
        }
    }
    return result.toString();
  }

  public static void main(String[] args){
    Main T = new Main();
    Scanner kb = new Scanner(System.in);
    String str = kb.next();

    System.out.println(swapCase(str));
    return ;
  }
}