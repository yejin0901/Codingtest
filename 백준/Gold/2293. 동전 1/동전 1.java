import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// coin
// dp[금액] -> 만들 수 있는 수
// dp[0] = 1

public class Main {
    static int[] parent;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 동전 종류 수
        int K = sc.nextInt(); // 만들고자 하는 금액

        int[] coins = new int[N];
        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        int[] dp = new int[K + 1];
        dp[0] = 1; // 0원을 만드는 경우의 수는 1


        for(int i =0; i< N; i++){
            int coin = coins[i];

            for(int j = coin; j<=K; j++){
                dp[j] += dp[j-coin];
            }
        }


        System.out.println(dp[K]);





    }







}