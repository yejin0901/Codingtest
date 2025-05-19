import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스 수
        sc.nextLine(); // 개행 문자 처리

        while (T-- > 0) {
            String W = sc.nextLine();
            int K = sc.nextInt();
            sc.nextLine(); // 개행 문자 처리

            // 각 문자의 인덱스를 저장할 리스트 배열
            List<Integer>[] charIndex = new ArrayList[26];
            for (int i = 0; i < 26; i++) {
                charIndex[i] = new ArrayList<>();
            }

            // 각 문자 위치 저장
            for (int i = 0; i < W.length(); i++) {
                charIndex[W.charAt(i) - 'a'].add(i);
            }

            int minLen = Integer.MAX_VALUE;
            int maxLen = Integer.MIN_VALUE;

            // 모든 알파벳에 대해 검사
            for (int i = 0; i < 26; i++) {
                List<Integer> indices = charIndex[i];
                if (indices.size() < K) continue;

                // 슬라이딩 윈도우 방식으로 길이 비교
                for (int j = 0; j <= indices.size() - K; j++) {
                    int len = indices.get(j + K - 1) - indices.get(j) + 1;
                    minLen = Math.min(minLen, len);
                    maxLen = Math.max(maxLen, len);
                }
            }

            if (minLen == Integer.MAX_VALUE || maxLen == Integer.MIN_VALUE) {
                System.out.println(-1);
            } else {
                System.out.println(minLen + " " + maxLen);
            }
        }

        sc.close();
    }
}
