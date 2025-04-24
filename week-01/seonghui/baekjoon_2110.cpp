// 공통문제
// https://www.acmicpc.net/problem/2110

#include <iostream>
#include <algorithm>

using namespace std;

int count_home;

bool isAvailable(int *arr, int x, int count){
	int temp = arr[0] + x;
	
	for (int i = 0; i < count_home; i++) {
		if (arr[i] >= temp) {
			count -= 1;
			temp = arr[i] + x;
			
			if (count == 0) {
				// 맨 뒤 거리도 기준에 충족하는지 확인
				if (arr[count_home - 1] - arr[i] < x) return false;
				return true;
			}
		}
		
    }
	
	return false;
}

int main(void){
	int count_router;
	int distance, standard;
	
	cin >> count_home >> count_router;
	
	// int 배열
	int locations[count_home];
	
	for (int i = 0; i < count_home; i++) {
		cin >> locations[i];
    }
	// 좌표가 정렬되어 들어오지 않음
	sort(locations, locations + count_home);
	
	distance = locations[count_home-1] - locations[0];
	standard = distance / 2;
	
	count_router -= 2;
	if (count_router == 0) {
		cout << distance;
		return 0;
	}

	while (!isAvailable(locations, standard, count_router)){
		distance = standard;
		standard = distance / 2;
	}
	while (distance - standard != 1 && isAvailable(locations, (distance + standard) / 2, count_router)){
		standard = (distance + standard) / 2;
	}
	
	cout << standard;
	
	return 0;
}
