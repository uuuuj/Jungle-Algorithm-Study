// https://www.acmicpc.net/problem/9663 공통문제

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_9663 {
    static int answer = 0;
    static int N;

    // 퀸이 공격할 수 있는지 체크하는 배열들
    static boolean[] visited1;     // 세로(열) 체크용
    static boolean[] visited2;     // 오른쪽 아래 대각선 (row + col)
    static boolean[] visited3;     // 왼쪽 아래 대각선 (row - col + (N - 1))

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());      // 체스판 크기 입력

        // 초기화
        visited1 = new boolean[N];
        visited2 = new boolean[2 * N - 1];
        visited3 = new boolean[2 * N - 1];

        backtracking(0);                  // 0번째 행부터 퀸 놓기 시작
        System.out.println(answer);               // 가능한 퀸 배치 방법의 수 출력
    }

    // 백트래킹 함수: 현재 행(row)을 position이라고 가정
    private static void backtracking(int position) {
        // 퀸을 N개 모두 놓았을 경우
        if (position == N) {
            answer++;
            return;
        }

        // 현재 행에서 모든 열(col)에 대해 시도
        for (int idx = 0; idx < N; idx++) {
            if (!visited1[idx] && !visited2[position + idx] && !visited3[position - idx + (N - 1)]) {

                // 퀸을 놓았다고 표시
                visited1[idx] = true;
                visited2[position + idx] = true;
                visited3[position - idx + (N - 1)] = true;

                // 다음 행으로 퀸 놓으러 가기
                backtracking(position + 1);

                // 퀸을 제거하고 상태 되돌리기
                visited1[idx] = false;
                visited2[position + idx] = false;
                visited3[position - idx + (N - 1)] = false;
            }
        }
    }
}
