import java.util.*;

public class Main {
    public static int findKthLargestSum(int n, int k, int[] cards) {
        // TreeSet을 사용하여 중복을 제거하고 자동으로 정렬
        TreeSet<Integer> set = new TreeSet<>(Collections.reverseOrder());
        
        
        // 모든 가능한 3장의 카드 조합을 찾아 합을 구함
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int l = j + 1; l < n; l++) {
                    set.add(cards[i] + cards[j] + cards[l]);
                }
            }
        }

        // set의 값을 리스트로 변환하여 접근
        ArrayList<Integer> list = new ArrayList<>(set);
        
        // k번째로 큰 값을 찾음 (k는 1부터 시작하므로 index는 k-1)
        if (k - 1 < list.size()) {
            return list.get(k - 1);
        } else {
            return -1; // K번째 값이 존재하지 않으면 -1 반환
        }
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
