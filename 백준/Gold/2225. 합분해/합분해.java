import java.util.*;

// 순열
// 한개의 수를 여러 번 쓸 수 있음
// k개

import java.util.*;

public class Main {
    static final int MOD = 1000000000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[][] dp = new int[K+1][N+1];

        // 초기화
        for (int i = 0; i <= K; i++) dp[i][0] = 1;
        for (int j = 1; j <= N; j++) dp[1][j] = 1;

        // DP 테이블 채우기
        for (int i = 2; i <= K; i++) {
            for (int j = 1; j <= N; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }

        System.out.println(dp[K][N]);
    }
}