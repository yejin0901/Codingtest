import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 도시 갯수, 연결여부, 여행계획






public class Main {
    static int[] parent;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        parent = new int[n+1];

        for(int i =1; i<=n; i++) parent[i] = i;

        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j <=n; j++){
                int connected = Integer.parseInt(st.nextToken());
                if(connected == 1) union(i,j);
            }
        }

        int[] plan = new int[m];
        st = new StringTokenizer(br.readLine());


        for(int i =0; i<m; i++){
            plan[i] = Integer.parseInt(st.nextToken());
        }

        boolean possible = true;
        int root = find(plan[0]);
        for(int i =0; i<m; i++){
            if(root != find(plan[i])){
                possible = false;
                break;
            }
        }

        System.out.println(possible ? "YES" : "NO");










    }


    static int find(int x){
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int a, int b){
        int ra = find(a);
        int rb = find(b);
        if(ra!=rb) parent[rb] = ra;
    }






}