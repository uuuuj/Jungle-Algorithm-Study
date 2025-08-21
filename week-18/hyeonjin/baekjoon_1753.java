package y25_08_03;
// baekjoon 1753 최단경로
// https://www.acmicpc.net/problem/1753

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_1753 {

    static class Edge {
        final int toNode;
        final int weight;
        Edge(int toNode, int weight) { this.toNode = toNode; this.weight = weight; }
    }

    static class Node {
        final int node;
        final long dist;
        Node(int node, long dist) { this.node = node; this.dist = dist; }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int nodeCount = Integer.parseInt(st.nextToken());
        int edgeCount = Integer.parseInt(st.nextToken());

        int startNode = Integer.parseInt(br.readLine().trim());

        // 인접 리스트
        List<Edge>[] graph = new ArrayList[nodeCount + 1];
        for (int i = 1; i <= nodeCount; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < edgeCount; i++) {
            st = new StringTokenizer(br.readLine());
            int fromNode = Integer.parseInt(st.nextToken());
            int toNode = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph[fromNode].add(new Edge(toNode, weight));
        }

        long[] dist = dijkstra(graph, startNode);

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= nodeCount; i++) {
            if (dist[i] == INF) sb.append("INF\n");
            else sb.append(dist[i]).append('\n');
        }
        System.out.print(sb.toString());
    }

    static final long INF = Long.MAX_VALUE / 4;

    static long[] dijkstra(List<Edge>[] graph, int start) {
        int n = graph.length - 1;
        // start 에서 i 번 정점까지의 최단 거리
        long[] dist = new long[n + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a.dist));
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int curNode = cur.node;
            long curDist = cur.dist;

            if (curDist != dist[curNode]) continue;

            for (Edge edge : graph[curNode]) {
                int nextNode = edge.toNode;
                long newDist  = curDist + edge.weight;
                if (newDist  < dist[nextNode]) {
                    dist[nextNode] = newDist ;
                    pq.offer(new Node(nextNode, newDist));
                }
            }
        }
        return dist;
    }


}
