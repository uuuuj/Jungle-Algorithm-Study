// https://school.programmers.co.kr/learn/courses/30/lessons/42583
import java.util.LinkedList;
import java.util.Queue;

public class programmers_42583 {

    class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {
            Queue<Integer> bridge = new LinkedList<>();
            // 다리 위를 모두 빈 칸(0)으로 초기화
            for (int i = 0; i < bridge_length; i++) bridge.add(0);

            int time = 0;           // 경과 시간(초)
            int totalWeight = 0;    // 다리 위 총 하중
            int idx = 0;            // 다음에 올릴 트럭 인덱스

            while (idx < truck_weights.length) {
                time++;
                totalWeight -= bridge.poll(); // 한 칸 전진(맨 앞 칸 내려감)

                int nextTruckWeight = truck_weights[idx];
                if (totalWeight + nextTruckWeight <= weight) {
                    // 트럭 올릴 수 있음
                    bridge.add(nextTruckWeight);
                    totalWeight += nextTruckWeight;
                    idx++;
                } else {
                    // 못 올리면 빈 칸 흘리기
                    bridge.add(0);
                }
            }

            // 마지막 트럭이 올리는 동시에, 반복문 종료 -> 누적 시간 + 다리 길이
            return time + bridge_length;
        }
    }

}
