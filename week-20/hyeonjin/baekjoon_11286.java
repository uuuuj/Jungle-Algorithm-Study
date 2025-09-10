// https://www.acmicpc.net/problem/11286
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class baekjoon_11286 {
    static class Element implements Comparator<Integer> {

        @Override
        public int compare(Integer num1, Integer num2) {
            int absNum1 = Math.abs(num1);
            int absNum2 = Math.abs(num2);

            return absNum1 == absNum2 ? num2-num1 : absNum2-absNum1;
            /* 결과 값
             * 양수 : n1 을 뒤로 보낸다. => 내림차순 (3-2-1)
             * 음수 : n1 를 앞에 둔다. => 오름차순 (1-2-3)
             * 0 : 순서 유지
             */
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>(new Element());

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(br.readLine());
            if (number != 0) {
                queue.offer(number);
            } else if (queue.isEmpty()) {
                result.append(0).append("\n");
            } else {
                result.append(queue.poll()).append("\n");
            }
        }
        System.out.println(result);
    }
}
