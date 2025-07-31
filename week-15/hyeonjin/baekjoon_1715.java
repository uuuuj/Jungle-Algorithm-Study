package y25_07_04;
// baekjoon 1715 카드 정렬하기
// https://www.acmicpc.net/problem/1715

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class baekjoon_1715 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pQ = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            pQ.offer(Integer.parseInt(br.readLine()));
        }

        int result = 0;

        while (!pQ.isEmpty()) {
            int cardA = pQ.poll();
            if (pQ.isEmpty()) {
                break;
            }
            int cardB = pQ.poll();
            pQ.offer(cardA + cardB);
            result += (cardA+cardB);

        }
        System.out.println(result);
    }

}