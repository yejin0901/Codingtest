import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[] original = br.readLine().toCharArray();
        char[] target = br.readLine().toCharArray();

        // 첫 번째 스위치를 누르지 않는 경우
        int result1 = solve(N, original, target, false);
        
        // 첫 번째 스위치를 누르는 경우
        int result2 = solve(N, original, target, true);

        // 두 경우 중 최소값 선택 (불가능한 경우 제외)
        if (result1 == -1 && result2 == -1) {
            System.out.println(-1);
        } else if (result1 == -1) {
            System.out.println(result2);
        } else if (result2 == -1) {
            System.out.println(result1);
        } else {
            System.out.println(Math.min(result1, result2));
        }
    }

    static int solve(int N, char[] original, char[] target, boolean pressFirst) {
        // 원본 배열 복사
        char[] current = Arrays.copyOf(original, N);
        int count = 0;

        // 첫 번째 스위치 처리
        if (pressFirst) {
            pressSwitch(current, 0);
            count++;
        }

        // 두 번째 전구부터 순차적으로 처리
        for (int i = 1; i < N; i++) {
            if (current[i-1] != target[i-1]) {
                pressSwitch(current, i);
                count++;
            }
        }

        // 마지막 전구 확인
        if (current[N-1] != target[N-1]) {
            return -1;
        }

        return count;
    }

    static void pressSwitch(char[] arr, int idx) {
        // 현재 위치 전구 토글
        arr[idx] = (arr[idx] == '0') ? '1' : '0';
        
        // 왼쪽 전구 토글 (인덱스 범위 확인)
        if (idx > 0) {
            arr[idx-1] = (arr[idx-1] == '0') ? '1' : '0';
        }
        
        // 오른쪽 전구 토글 (인덱스 범위 확인)
        if (idx < arr.length - 1) {
            arr[idx+1] = (arr[idx+1] == '0') ? '1' : '0';
        }
    }
}