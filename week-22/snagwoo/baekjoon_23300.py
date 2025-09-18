import sys
from collections import deque

input = sys.stdin.readline

def go_backward(cache):
  if not cache['backward']:
    return cache

  cache['forward'].append(cache['current'])
  cache['current'] = cache['backward'].pop()

  return cache

def go_forward(cache):
  if not cache['forward']:
    return cache
  
  cache["backward"].append(cache['current'])
  cache['current'] = cache['forward'].pop()

  return cache

def access(new_page, cache):
  cache['forward'] = []

  if cache['current']:
    cache["backward"].append(cache['current'])

  cache['current'] = new_page
  return cache


def compress(cache):
  compressed = []

  for value in cache["backward"]:
    if not compressed or compressed[-1] != value:
      compressed.append(value)

  cache["backward"] = compressed

  return cache



N, Q = map(int,input().split())

cache = {
  'forward': [],
  'backward': [],
  'current': 0,
}

for _ in range(Q):
  action = input().rstrip()

  command = action[0]

  if command == 'B':
    cache = go_backward(cache=cache)
    continue

  if command == 'F':
    cache = go_forward(cache=cache)
    continue
  
  if command == 'A':
    new_page_index = action.split()[1]
    cache = access(new_page=new_page_index, cache=cache)
    continue

  if command == 'C':
    cache = compress(cache=cache)
    continue

print(cache['current'])
print(' '.join(reversed(cache['backward'])) if cache['backward'] else -1)
print(' '.join(reversed(cache['forward'])) if cache['forward'] else -1)
