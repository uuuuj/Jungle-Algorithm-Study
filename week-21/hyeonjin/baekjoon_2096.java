// https://www.acmicpc.net/problem/2096 공통문제
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_2096 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int inputCol1, inputCol2, inputCol3;

        int prevMaxCol1=0, prevMaxCol2=0, prevMaxCol3=0;
        int prevMinCol1=0, prevMinCol2=0, prevMinCol3=0;

        int curMaxCol1, curMaxCol2, curMaxCol3;
        int curMinCol1, curMinCol2, curMinCol3;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            inputCol1 = Integer.parseInt(st.nextToken());
            inputCol2 = Integer.parseInt(st.nextToken());
            inputCol3 = Integer.parseInt(st.nextToken());

            if (i == 0) {
                prevMaxCol1 = prevMinCol1 = inputCol1;
                prevMaxCol2 = prevMinCol2 = inputCol2;
                prevMaxCol3 = prevMinCol3 = inputCol3;
            } else {
                // max
                curMaxCol1 = Math.max(prevMaxCol1, prevMaxCol2) + inputCol1;
                curMaxCol3 = Math.max(prevMaxCol2, prevMaxCol3) + inputCol3;
                curMaxCol2 = Math.max(Math.max(prevMaxCol1, prevMaxCol2), prevMaxCol3) + inputCol2;
                // min
                curMinCol1 = Math.min(prevMinCol1, prevMinCol2) + inputCol1;
                curMinCol3 = Math.min(prevMinCol2, prevMinCol3) + inputCol3;
                curMinCol2 = Math.min(Math.min(prevMinCol1, prevMinCol2), prevMinCol3) + inputCol2;

                // prev 재설정
                prevMaxCol1 = curMaxCol1; prevMaxCol2 = curMaxCol2; prevMaxCol3 = curMaxCol3;
                prevMinCol1 = curMinCol1; prevMinCol2 = curMinCol2; prevMinCol3 = curMinCol3;
            }
        }

        // i == 0 조건문에 의해 최종 값은 prevCol 값으로 출력해야 한다.
        int maximum = Math.max(Math.max(prevMaxCol1, prevMaxCol2), prevMaxCol3);
        int minimum = Math.min(Math.min(prevMinCol1, prevMinCol2), prevMinCol3);
        System.out.println(maximum + " " + minimum);
    }
}