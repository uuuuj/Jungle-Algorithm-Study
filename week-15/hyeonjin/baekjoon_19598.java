package y25_07_05;
// baekjoon 19598 최소 회의실 개수
// https://www.acmicpc.net/problem/19598

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class baekjoon_19598 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] times = new int[n][2];  // 회의 시작시간, 종료시간 저장

        // 회의 시간 입력받기
        for (int i = 0; i < n; i++) {
            times[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        // 회의 시작시간 기준 오름차순 정렬
        Arrays.sort(times, Comparator.comparingInt(t -> t[0]));

        // 종료시간 우선순위 큐 (가장 빨리 끝나는 회의실부터 확인)
        PriorityQueue<Integer> endTimes = new PriorityQueue<>();

        for (int[] time : times) {
            int start = time[0];
            int end = time[1];

            // 가장 빨리 끝나는 회의실의 종료시간이 현재 회의 시작시간보다 작거나 같으면 → 해당 회의실 재사용
            if (!endTimes.isEmpty() && endTimes.peek() <= start) {
                endTimes.poll();  // 회의실 비우기
            }

            // 현재 회의 종료시간 추가 (새 회의실 또는 재사용)
            endTimes.offer(end);
        }

        // 우선순위 큐에 남아있는 종료시간 수 = 사용된 회의실 수
        System.out.println(endTimes.size());
    }
}
