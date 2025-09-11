from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pre_case = ['()']

        for _ in range(1, n):
            created_case = set()

            for case in pre_case:

                stack_right = deque(list(case))
                stack_left = deque([])
                
                while stack_right:
                    created_case.add(''.join([ ''.join(stack_left), '()', ''.join(stack_right)]))

                    l = deque.popleft(stack_right)
                    deque.append(stack_left, l)

                created_case.add(''.join([ ''.join(stack_right), '()', ''.join(stack_left)]))

            pre_case = created_case

        return list(pre_case)


# 백트래킹
def generateParenthesis(self, n: int) -> List[str]:
  result = []


  def backtrack(current, open_count, close_count):
      if (len(current) == 2 * n):
          result.append(current)
          return

      if open_count < n:
          backtrack(current + '(', open_count + 1, close_count)
        
      if close_count < open_count:
          backtrack(current + ')', open_count, close_count + 1)
  
  backtrack('', 0, 0)

  return result