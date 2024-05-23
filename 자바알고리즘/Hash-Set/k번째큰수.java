import java.util.*;

public class Main {
    public static int findKthLargestSum(int n, int k, int[] cards) {
        // TreeSet을 사용하여 중복을 제거하고 자동으로 정렬 (내림차순)
        TreeSet<Integer> set = new TreeSet<>(Collections.reverseOrder());
        
        // 모든 가능한 3장의 카드 조합을 찾아 합을 구함
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int l = j + 1; l < n; l++) {
                    set.add(cards[i] + cards[j] + cards[l]);
                }
            }
        }

        // TreeSet의 값을 Iterator로 접근하여 K번째 값을 찾음
        int count = 0;
        for (int sum : set) {
            count++;
            if (count == k) {
                return sum;
            }
        }
        
        // K번째 값이 존재하지 않으면 -1 반환
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // N과 K 입력
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        
        // 카드 값 입력
        int[] cards = new int[n];
        for (int i = 0; i < n; i++) {
            cards[i] = scanner.nextInt();
        }
        
        // 결과 출력
        System.out.println(findKthLargestSum(n, k, cards));
    }
}
