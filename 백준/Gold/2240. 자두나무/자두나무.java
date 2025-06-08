import java.io.*;
import java.util.*;

public class Main {
    static int T, W;
    static int[] tree; // 자두가 떨어지는 나무 위치
    static int[][] dp; // dp[t][w] = t초에 w번 이동했을 때 최대로 받은 자두 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken()); // 초
        W = Integer.parseInt(st.nextToken()); // 최대 이동 횟수
        tree = new int[T + 1];
        dp = new int[T + 1][W + 1];

        for (int i = 1; i <= T; i++) {
            tree[i] = Integer.parseInt(br.readLine()); // 자두가 떨어지는 나무 번호
        }

        for (int t = 1; t <= T; t++) {
            for (int w = 0; w <= W; w++) {
                // 현재 위치 = 1번 나무 if w 짝수, 2번 나무 if w 홀수
                int currentPos = (w % 2 == 0) ? 1 : 2;

                // 전 상태 중 큰 값을 이어받는다
                if (w == 0) {
                    dp[t][w] = dp[t - 1][w]; // 이동 안했으면 이전 값 유지
                } else {
                    dp[t][w] = Math.max(dp[t - 1][w], dp[t - 1][w - 1]);
                }

                // 현재 위치에 자두가 떨어지면 +1
                if (tree[t] == currentPos) {
                    dp[t][w]++;
                }
            }
        }

        // 최대값 찾기
        int answer = 0;
        for (int w = 0; w <= W; w++) {
            answer = Math.max(answer, dp[T][w]);
        }

        System.out.println(answer);
    }
}
