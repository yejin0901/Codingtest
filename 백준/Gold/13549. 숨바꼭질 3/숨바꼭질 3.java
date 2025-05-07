import java.util.*;
import java.io.*;

public class Main {
    static final int MAX = 200000;
    static int[] time = new int[MAX + 1];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken()); // 수빈이 위치
        int K = Integer.parseInt(st.nextToken()); // 동생 위치
        
        Arrays.fill(time, -1);
        Deque<Integer> deque = new ArrayDeque<>();
        deque.offer(N);
        time[N] = 0;
        
        while (!deque.isEmpty()) {
            int now = deque.poll();
            
            if (now == K) {
                System.out.println(time[now]);
                return;
            }
            
            // 순간이동 (0초)
            int next = now * 2;
            if (next <= MAX && time[next] == -1) {
                time[next] = time[now];
                deque.addFirst(next); // 우선순위 높음
            }
            
            // 걷기 (1초)
            for (int move : new int[]{now - 1, now + 1}) {
                if (move >= 0 && move <= MAX && time[move] == -1) {
                    time[move] = time[now] + 1;
                    deque.addLast(move); // 우선순위 낮음
                }
            }
        }
    }
}