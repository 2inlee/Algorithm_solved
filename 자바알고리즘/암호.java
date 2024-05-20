import java.util.Scanner;

public class Main {

    public static String solution(int num, String str) {
        StringBuilder result = new StringBuilder();
        int fixLen = 7;

        for (int i = 0; i < num; i++) {
            String subStr = str.substring(i * fixLen, (i + 1) * fixLen);
            String binaryStr = subStr.replace('#', '1').replace('*', '0');
            int asciiValue = Integer.parseInt(binaryStr, 2);
            result.append((char) asciiValue);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        String str = in.next();
        
        System.out.println(solution(num, str));
    }
}
