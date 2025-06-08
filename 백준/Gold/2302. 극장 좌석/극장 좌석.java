import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 전체 좌석 수
        int M = sc.nextInt(); // 고정석 개수

        // 고정석 리스트
        List<Integer> fixed = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            fixed.add(sc.nextInt());
        }

        // 미리 피보나치 수열을 dp 배열에 채워놓기 (최대 N까지)
        int[] dp = new int[N + 1];
        dp[0] = 1; // 0자리일 때도 1가지 경우
        dp[1] = 1;
        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        int result = 1; // 곱셈 초기값
        int prev = 0; // 이전 고정석 위치 (0부터 시작)

        for (int i = 0; i < M; i++) {
            int current = fixed.get(i);
            int length = current - prev - 1; // 고정석 사이의 가변 구간 길이
            result *= dp[length];
            prev = current;
        }

        // 마지막 고정석 뒤에 남은 구간 처리
        result *= dp[N - prev];

        System.out.println(result);
    }
}
