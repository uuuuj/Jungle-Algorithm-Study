// https://school.programmers.co.kr/learn/courses/30/lessons/43165
package y25_09_03;

public class programmers_43165 {
    private static int targetValue;
    private static int[] numberList;

    public static int solution(int[] numbers, int target) {
        int answer = 0;
        targetValue = target;
        numberList = numbers;

        answer = dfs(0, 0);
        return answer;
    }

    private static int dfs(int idx, int result) {
        if (idx == numberList.length) {
            return result == targetValue ? 1 : 0;
        }

        int add = dfs(idx + 1, result + numberList[idx]);
        int subtract = dfs(idx + 1, result - numberList[idx]);

        return add + subtract;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;

        int res = solution(numbers, target);
        System.out.println(res);
    }
}
