import java.util.*;

public class Main {
    static class Patient {
        int index;
        int risk;

        public Patient(int index, int risk) {
            this.index = index;
            this.risk = risk;
        }
    }

    public static int solution(int n, int m, int[] risks) {
        Queue<Patient> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            queue.offer(new Patient(i, risks[i]));
        }

        int count = 0;
        while (!queue.isEmpty()) {
            Patient current = queue.poll();
            boolean hasHigherRisk = false;

            for (Patient patient : queue) {
                if (patient.risk > current.risk) {
                    hasHigherRisk = true;
                    break;
                }
            }

            if (hasHigherRisk) {
                queue.offer(current);
            } else {
                count++;
                if (current.index == m) {
                    return count;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] risks = new int[n];
        for (int i = 0; i < n; i++) {
            risks[i] = in.nextInt();
        }
        System.out.print(solution(n, m, risks));
    }
}
