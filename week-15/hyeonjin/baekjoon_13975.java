package y25_07_04;
// baekjoon 13975 파일 합치기 3
// https://www.acmicpc.net/problem/13975

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;;

public class baekjoon_13975 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        while (testCase-- > 0) {
            int k = Integer.parseInt(br.readLine());
            PriorityQueue<Long> pq = new PriorityQueue<>();
            Arrays.stream(br.readLine().split(" "))
                    .forEach(s -> pq.offer(Long.parseLong(s)));

            long result = 0;
            while (pq.size() > 1) {
                long sizeA = pq.poll();
                long sizeB = pq.poll();
                result += (sizeA + sizeB);
                pq.offer(sizeA + sizeB);
            }
            System.out.println(result);
        }
    }
}