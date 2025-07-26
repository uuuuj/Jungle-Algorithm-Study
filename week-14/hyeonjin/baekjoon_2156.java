package y25_07_04.P2667;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] wine = new int[n];
        for (int i = 0; i < n; i++) {
            wine[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[n];

        // 초기 조건
        if (n == 1) {
            System.out.println(wine[0]);
            return;
        } else if (n == 2) {
            System.out.println(wine[0] + wine[1]);
            return;
        }

        dp[0] = wine[0];
        dp[1] = wine[0] + wine[1];
        dp[2] = Math.max(dp[1], Math.max(wine[0] + wine[2], wine[1] + wine[2]));

        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(
                    // i-1, i 마시는 경우
                    dp[i - 1], Math.max(
                            dp[i - 2] + wine[i],// i번째 잔만 마시는 경우
                            dp[i - 3] + wine[i - 1] + wine[i]   // i-1, i 마시는 경우
                    )
            );
        }
        System.out.println(dp[n - 1]);
    }
}