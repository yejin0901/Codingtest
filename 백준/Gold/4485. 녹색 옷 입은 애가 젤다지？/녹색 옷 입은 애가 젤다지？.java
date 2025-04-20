import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int problemNum = 1;
        
        while (true) {
            N = Integer.parseInt(br.readLine());
            if (N == 0) break;
            
            map = new int[N][N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            
            int result = dijkstra();
            System.out.println("Problem " + problemNum++ + ": " + result);
        }
    }
    
    static int dijkstra() {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int[][] dist = new int[N][N];
        
        // 거리 배열 초기화
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        
        // 시작점 설정
        dist[0][0] = map[0][0];
        pq.offer(new Node(0, 0, dist[0][0]));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int x = current.x;
            int y = current.y;
            
            // 목적지에 도달한 경우
            if (x == N-1 && y == N-1) {
                return current.cost;
            }
            
            // 이미 처리된 노드인 경우
            if (current.cost > dist[x][y]) {
                continue;
            }
            
            // 4방향 탐색
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 범위 체크
                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }
                
                // 새로운 비용 계산
                int newCost = dist[x][y] + map[nx][ny];
                
                // 더 짧은 경로 발견한 경우
                if (newCost < dist[nx][ny]) {
                    dist[nx][ny] = newCost;
                    pq.offer(new Node(nx, ny, newCost));
                }
            }
        }
        
        return dist[N-1][N-1];
    }
    
    static class Node implements Comparable<Node> {
        int x, y, cost;
        
        public Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
}