import sys
from collections import defaultdict

input = sys.stdin.readline

def build_char_positions(text):
    char_positions = defaultdict(list)
    
    for index, char in enumerate(text):
      char_positions[char].append(index)
    
    return char_positions


def find_substring_length(position, K):
    if len(position) < K:
      return None

    lengths = []
    for i in range(len(position) - K + 1):
      cur = position[i]
      next = position[i + K - 1]
      length = next - cur + 1
      lengths.append(length)

    return max(lengths), min(lengths)

def solve_case(W, K):
  char_positions = build_char_positions(W)

  all_lengths = []

  for positions in char_positions.values():
    result = find_substring_length(positions, K)

    if result:
      min_length, max_length = result
      all_lengths.append(min_length)
      all_lengths.append(max_length)

  
  if not all_lengths:
    return -1

  return min(all_lengths), max(all_lengths)

T = int(input())

for _ in range(T):
  W = input().rstrip()
  K = int(input())

  result = solve_case(W, K)

  if result == -1:
    print(result)
  else:
    print(*result)


