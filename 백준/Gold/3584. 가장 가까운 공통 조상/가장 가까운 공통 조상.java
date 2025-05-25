import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int[] depth;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            parent = new int[N + 1];
            depth = new int[N + 1];
            
            // 부모-자식 관계 입력 및 루트 노드 찾기
            boolean[] isChild = new boolean[N + 1];
            for (int i = 0; i < N - 1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int p = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                parent[c] = p;
                isChild[c] = true;
            }
            
            // 루트 노드 찾기 (부모가 없는 노드)
            int root = 0;
            for (int i = 1; i <= N; i++) {
                if (!isChild[i]) {
                    root = i;
                    break;
                }
            }
            
            // 깊이 계산
            calculateDepth(root);
            
            // 공통 조상을 찾을 두 노드 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            System.out.println(findLCA(a, b));
        }
    }
    
    // 각 노드의 깊이 계산
    static void calculateDepth(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        depth[node] = 1;
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            
            for (int i = 1; i < parent.length; i++) {
                if (parent[i] == current && depth[i] == 0) {
                    depth[i] = depth[current] + 1;
                    queue.add(i);
                }
            }
        }
    }
    
    // 최소 공통 조상 찾기
    static int findLCA(int a, int b) {
        // 두 노드의 깊이를 맞춤
        while (depth[a] > depth[b]) {
            a = parent[a];
        }
        while (depth[b] > depth[a]) {
            b = parent[b];
        }
        
        // 같은 깊이에서 공통 조상 찾기
        while (a != b) {
            a = parent[a];
            b = parent[b];
        }
        
        return a;
    }
}