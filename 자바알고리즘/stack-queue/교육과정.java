import java.util.*;

public class Main {
    public static String solution(String required, String plan) {
        Queue<Character> queue = new LinkedList<>();
        for (char c : required.toCharArray()) {
            queue.offer(c);
        }

        for (char c : plan.toCharArray()) {
            if (!queue.isEmpty() && c == queue.peek()) {
                queue.poll();
            }
        }

        if (queue.isEmpty()) {
            return "YES";
        } else {
            return "NO";
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        // 필수과목 순서 입력
        String required = in.nextLine();
        
        // 수업설계 입력
        String plan = in.nextLine();
        
        // 결과 출력
        System.out.println(solution(required, plan));
    }
}
