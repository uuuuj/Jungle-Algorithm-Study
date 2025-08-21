package y25_08_03;
// baekjoon 11399 ATM
// https://www.acmicpc.net/problem/11399

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_11399 {
    private static int[] nums;
    private static int N;
    private static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        nums = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        selectionSort();
        System.out.println(result);
    }

    private static void selectionSort() {
        int waitTime = 0;
        for (int i = 0; i < N; i++) {
            int minIndex = i;
            for (int j = i; j < N; j++) {
                if (nums[j] < nums[minIndex]) {
                    minIndex = j;
                }
            }
            waitTime += nums[minIndex];
            nums[minIndex] = nums[i];
            result += waitTime;
        }
    }
}