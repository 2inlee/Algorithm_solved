import java.util.*;


class Main{
  public static ArrayList<String> solution(int n, String[] str){
    ArrayList<String> answer = new ArrayList<>(); 
    for(String x : str){
      // String은 불변이기때문에, 값이 변할 때 마다 객체가 생성되어 메모리낭비가 발생함
      // StringBuilder로 만들게 되면, 객체를 하나만 생성해서 사용하기 때문에 메모리낭비가 발생하지 않음. 동적배열(Dynamic array base)로 초기메모리가 전부 사용되면 더블링하고 옮겨담음
      String tmp = new StringBuilder(x).reverse().toString();
      answer.add(tmp);
    }

    return answer;
  }

  public static void main(String[] args){
    Scanner kb = new Scanner(System.in);
    int n = kb.nextInt();
    String[] str = new String[n];

    for(int i=0; i<n; i++){
      str[i] = kb.next();
    }

    for(String x : solution(n, str)){
      System.out.println(x);
    }
  }
}

