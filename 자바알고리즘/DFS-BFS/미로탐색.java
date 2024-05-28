import java.util.*;

public class Main {
    static int answer;
    static int[][] board;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    

    public void DFS(int x, int y){
        if(x==7 && y==7) answer++;
        else{
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx>=1 && nx<=7 && ny>=1 && ny<=7 && board[nx][ny] ==0){
                    board[nx][ny] = 1;
                    DFS(nx, ny);
                    board[nx][ny] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner in = new Scanner(System.in);
        board = new int[8][8];

        for(int i = 1; i < 8; i++){
            for(int j = 1; j < 8; j++){
                board[i][j] = in.nextInt(); // 배열에 값 입력
            }
        }
        board[1][1] = 1;
        T.DFS(1, 1);
        System.out.println(answer);
    }
}
