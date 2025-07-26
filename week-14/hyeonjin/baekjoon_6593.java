// 공통 baekjoon 6593 상범 빌딩
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    // 3차원 빌딩 구조 (층, 행, 열)
    static char[][][] building;

    // 시작 위치 좌표 (층, 행, 열)
    private static int start_x = 0;
    private static int start_y = 0;
    private static int start_z = 0;

    // 빌딩 크기 (층 수 l, 행 r, 열 c)
    private static int l = 0;
    private static int r = 0;
    private static int c = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 여러 테스트 케이스 처리
        while (true) {
            // 층(L), 행(R), 열(C) 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            l = Integer.parseInt(st.nextToken());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            // 입력 종료 조건 (0 0 0)
            if (l == 0 && r == 0 && c == 0)
                break;

            // 빌딩 구조 초기화
            building = new char[l][r][c];

            // 층별로 입력
            for (int z = 0; z < l; z++) {
                for (int x = 0; x < r; x++) {
                    String temp = br.readLine();
                    for (int y = 0; y < c; y++) {
                        building[z][x][y] = temp.charAt(y);

                        // 시작 지점 저장
                        if (temp.charAt(y) == 'S') {
                            start_z = z;
                            start_x = x;
                            start_y = y;
                        }
                    }
                }
                // 층 사이의 공백 라인 제거
                br.readLine();
            }

            // BFS 실행 후 결과 출력
            int count = escape();
            if (count == 0)
                System.out.println("Trapped!"); // 도달 불가
            else
                System.out.println("Escaped in " + count + " minute(s)."); // 탈출 성공
        }
    }


    private static int escape() {
        // 6방향 이동 (동, 서, 남, 북, 위, 아래)
        int[] dx = {0, 0, 1, -1, 0, 0};
        int[] dy = {1, -1, 0, 0, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};

        // 이동 거리 기록용 배열
        int[][][] dist = new int[l][r][c];

        // 시작 위치 큐에 삽입
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{start_z, start_x, start_y});

        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int z = temp[0], x = temp[1], y = temp[2];

            // 탈출 지점 도달 시 종료
            if (building[z][x][y] == 'E') {
                return dist[z][x][y];
            }

            // 6방향 탐색
            for (int i = 0; i < 6; i++) {
                int nz = z + dz[i];
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 범위 체크
                if (nx < 0 || ny < 0 || nz < 0 || nx >= r || ny >= c || nz >= l) continue;

                // 벽이거나 이미 방문한 곳 제외
                if (building[nz][nx][ny] == '#' || dist[nz][nx][ny] != 0) continue;

                // 다음 위치 큐에 추가하고 거리 갱신
                q.offer(new int[]{nz, nx, ny});
                dist[nz][nx][ny] = dist[z][x][y] + 1;
            }
        }

        // 끝까지 도달하지 못했을 경우
        return 0;
    }
}
