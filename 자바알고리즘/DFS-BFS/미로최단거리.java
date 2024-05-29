import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    private static int[][] board;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    
    public static void main(String[] args) {
        Main T = new Main();
        Scanner in = new Scanner(System.in);
        board = new int[8][8];

        for(int i = 1; i < 8; i++){
            for(int j = 1; j < 8; j++){
                board[i][j] = in.nextInt(); // 배열에 값 입력
            }
        }

        int result = T.bfs(1, 1);
        System.out.println(result);
    }

    private int bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[8][8];
        
        // 시작점 초기화
        queue.offer(new int[] {x, y, 0}); // {x, y, 이동 거리}
        visited[x][y] = true;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int dist = current[2];
            
            // 도착점에 도달한 경우
            if (x == 7 && y == 7) {
                return dist;
            }
            
            // 네 방향으로 이동
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 미로 범위 내에 있고, 도로(0)이며, 방문하지 않은 경우
                if (nx >= 1 && nx <= 7 && ny >= 1 && ny <= 7 && board[nx][ny] == 0 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx, ny, dist + 1});
                }
            }
        }
        
        // 도착점에 도달하지 못한 경우
        return -1;
    }
}
