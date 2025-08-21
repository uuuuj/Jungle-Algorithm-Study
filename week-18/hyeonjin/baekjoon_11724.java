package y25_08_03;
// baekjoon 11724 연결 요소의 개수
// https://www.acmicpc.net/problem/11724

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class baekjoon_11724 {
    private static ArrayList<Integer>[] nodes;
    private static boolean[] visited;
    private static int N;
    private static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nodes = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            nodes[i] = new ArrayList<Integer>();
        }

        for (int j = 0; j < M; j++) {
            st = new StringTokenizer(br.readLine());
            int startNode = Integer.parseInt(st.nextToken());
            int endNode = Integer.parseInt(st.nextToken());
            nodes[startNode].add(endNode);
            nodes[endNode].add(startNode);
        }
        int count = 0;
        visited = new boolean[N+1];

        for (int node = 1; node <= N; node++) {
            if (!visited[node]) {
                count++;
                DFS(node);
            }
        }
        System.out.println(count);

    }

    private static void DFS(int startNode) {
        if (visited[startNode]) {
            return;
        }
        visited[startNode] = true;
        for (int nextNode : nodes[startNode]) {
            if (!visited[nextNode]) {
                DFS(nextNode);
            }
        }
    }
}
