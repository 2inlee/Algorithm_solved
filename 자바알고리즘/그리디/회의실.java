import java.util.*;

class Time implements Comparable<Time>{
  public int s, e;
  Time(int s, int e){
    this.s = s;
    this.e = e;
  }
  @Override
  public int compareTo(Time o){
    if(this.e==o.e) return this.s - o.s;
    else return this.e - o.e;
  }
}

class Main{
  public int solution(ArrayList<Time> arr, int n){
    int cnt = 0;
    Collections.sort(arr);
    int et = 0;
    for(Time ob : arr){
      if(ob.s >= et){
        cnt++;
        et = ob.e;
      }
    }
    return cnt;
  }

  public static void main(String[] args){
    Main T = new Main();
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    ArrayList<Time> arr = new ArrayList<>();
    for(int i=0; i<n; i++){
      int x = in.nextInt();
      int y = in.nextInt();
      arr.add(new Time(x,y));
    }
    System.out.println(T.solution(arr, n));
  }
}