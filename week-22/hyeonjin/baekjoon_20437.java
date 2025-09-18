// https://www.acmicpc.net/problem/20437 (공통문제)
package y25_09_02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class baekjoon_20437 {
    public static void main(String[] args) throws IOException {
        // 빠른 입력 처리를 위한 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 최종 출력 결과를 모아둘 StringBuilder
        StringBuilder result = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim()); // 테스트 케이스 개수 입력

        while (T-- > 0) {
            String W = br.readLine().trim();            // 입력 문자열
            int K = Integer.parseInt(br.readLine().trim());  // 정확히 포함되어야 할 문자 개수 K

            // 알파벳 소문자 26개 각각에 대한 등장 인덱스를 저장할 배열
            // pos[0] → 'a', pos[1] → 'b', ..., pos[25] → 'z'
            List<Integer>[] pos = new ArrayList[26];
            for (int i = 0; i < 26; i++) pos[i] = new ArrayList<>();

            // 문자열 W의 각 문자 위치를 pos 배열에 기록
            for (int i = 0; i < W.length(); i++) {
                char ch = W.charAt(i);
                pos[ch - 'a'].add(i);  // 문자 'a'~'z'를 0~25로 매핑
            }

            int minLen = Integer.MAX_VALUE; // 조건을 만족하는 최소 길이 초기화
            int maxLen = -1;                // 조건을 만족하는 최대 길이 초기화

            // 각 알파벳별로 등장 인덱스 리스트를 확인
            for (int alpha = 0; alpha < 26; alpha++) {
                List<Integer> idxs = pos[alpha];      // 해당 알파벳의 등장 인덱스 리스트
                int idxSize = idxs.size();            // 등장 횟수

                if (idxSize < K) continue;            // K번 이상 등장하지 않은 문자는 무시

                // 슬라이딩 윈도우: 크기 K로 윈도우를 이동하며 확인
                // idxs.get(endIdx - K + 1) ~ idxs.get(endIdx)가 포함된 구간이 K개의 해당 문자를 포함
                for (int endIdx = K - 1; endIdx < idxSize; endIdx++) {
                    int start = idxs.get(endIdx - K + 1); // K개 중 첫 번째 등장 위치
                    int end   = idxs.get(endIdx);         // K개 중 마지막 등장 위치
                    int len   = end - start + 1;          // 부분 문자열의 길이 계산

                    // 가장 짧은 부분 문자열 길이 갱신
                    if (len < minLen) minLen = len;
                    // 가장 긴 부분 문자열 길이 갱신
                    if (len > maxLen) maxLen = len;
                }
            }

            // 결과 처리
            if (maxLen == -1) result.append("-1\n");
            else result.append(minLen).append(' ').append(maxLen).append('\n');
        }
        System.out.print(result);
    }
}
