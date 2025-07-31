package y25_07_05;
// baekjoon 1654 랜선 자르기
// https://www.acmicpc.net/problem/1654

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_1654 {

    private static int k;
    private static int n;
    private static int[] lanLines;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] lan = br.readLine().split(" ");
        k = Integer.parseInt(lan[0]);
        n = Integer.parseInt(lan[1]);

        lanLines = new int[k];
        long end = 0;

        for (int i = 0; i < k; i++) {
            int lanLength = Integer.parseInt(br.readLine());
            lanLines[i] = lanLength;
            end = Math.max(end, lanLength);
        }

        System.out.println(findMaxLength(end));

    }

    private static long findMaxLength(long end) {
        long result = 0;
        long start = 1;

        while (start <= end) {
            long mid = (start+end) / 2;
            int count = 0;
            for (int j = 0; j < k; j++) {
                count += lanLines[j] / mid;
            }
            if (count >= n) {
                result = mid;
                start = mid + 1;
            } else {
                end = mid -1;
            }
        }
        return result;
    }
}