import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n]; // 원래 수열
        int[] dp = new int[n];  // LIS 길이 저장
        int[] prev = new int[n]; // LIS 경로 저장

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            dp[i] = 1;       // 최소 LIS 길이는 1
            prev[i] = -1;    // 이전 경로 초기화
        }

        // LIS 알고리즘 (O(N^2))
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j; // 경로 저장
                }
            }
        }

        // 최댓값 및 인덱스 찾기
        int maxLength = 0;
        int endIndex = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] > maxLength) {
                maxLength = dp[i];
                endIndex = i;
            }
        }

        // LIS 수열 역추적
        Stack<Integer> stack = new Stack<>();
        while (endIndex != -1) {
            stack.push(arr[endIndex]);
            endIndex = prev[endIndex];
        }

        // 출력
        System.out.println(maxLength);
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
    }
}
