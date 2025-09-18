// https://school.programmers.co.kr/learn/courses/30/lessons/42578
package y25_09_03;

import java.util.*;

public class programmers_42578 {
    public static int solution(String[][] clothes) {
        Map<String, Integer> clothMap = new HashMap<>();
        for (String[] cloth : clothes) {
            String kind = cloth[1];
            clothMap.put(kind, clothMap.getOrDefault(kind, 0) + 1);
        }

        int answer = 1;
        for (int count : clothMap.values()) {
            answer *= (count + 1); // 해당 종류에서 "입지 않는 경우"까지 포함한 선택지 수
        }
        return answer - 1; // 모든 종류에서 아무것도 입지 않는 경우 제외
    }

    public static void main(String[] args) {
//        String[][] test = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};;
        String[][] test = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
        int res = solution(test);
        System.out.println(res);

    }

}
