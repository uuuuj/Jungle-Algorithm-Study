// https://school.programmers.co.kr/learn/courses/30/lessons/42577
import java.util.*;

public class programmers_42557 {
    public static boolean solution(String[] phone_book) {
        Set<String> phoneSet = new HashSet<>();
        for (String phone : phone_book) {
            // 중복 번호가 있다면 바로 false
            if (!phoneSet.add(phone)) {
                return false;
            }
        }

        // 접두사 체크
        for (String phone : phone_book) {
            StringBuilder prefix = new StringBuilder();
            // 전화번호 길이의 -1 까지만 검증 및 추가
            for (int i = 0; i < phone.length() - 1; i++) {
                prefix.append(phone.charAt(i));
                if (phoneSet.contains(prefix.toString())) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String[] phone_book = {"123","456","789"};
        boolean result = solution(phone_book);
        System.out.println("result = " + result);


    }
}
