import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 상담 기간과 금액 배열
        int[] T = new int[N + 1];
        int[] P = new int[N + 1];
        long[] dp = new long[N + 2]; // N+1일을 포함하기 위해 N+2 크기로 생성

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken()); // 상담 기간
            P[i] = Integer.parseInt(st.nextToken()); // 상담 수익
        }

        // DP 진행
        for (int i = 1; i <= N; i++) {
            // 현재까지 최대 수익 유지
            dp[i] = Math.max(dp[i], dp[i - 1]);

            // 상담이 퇴사 전까지 가능한 경우
            int endDay = i + T[i] - 1;
            if (endDay <= N) {
                dp[endDay] = Math.max(dp[endDay], dp[i - 1] + P[i]);
            }
        }

        // 마지막 날까지 중 최대 수익 출력
        long maxProfit = 0;
        for (int i = 1; i <= N + 1; i++) {
            maxProfit = Math.max(maxProfit, dp[i]);
        }

        System.out.println(maxProfit);
    }
}
