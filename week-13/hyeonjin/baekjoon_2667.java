// 공통 baekjoon 2667

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {
    private static int[][] map;
    private static int N;
    private static int count = 0;

    // 상, 하, 좌, 우 이동
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            map[i] = Arrays
                    .stream(br.readLine().split(""))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (map[x][y] == 1) {
                    count = 1;
                    map[x][y] = 0;
                    dfs(x, y);
                    result.add(count);
                }

            }
        }
        System.out.println(result.size());
        result.stream().sorted().forEach(System.out::println);
    }

    private static void dfs(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
            if (map[nx][ny] != 1) continue;

            map[nx][ny] = 0; // 방문 처리
            count++;
            dfs(nx, ny);
        }
    }
}