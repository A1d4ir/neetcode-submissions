class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        ans_sum = 0
        while len(operations) > 0:
            operation = operations.pop(0)

            try:
                value = int(operation)
                ans.append(value)
                ans_sum += value
            except ValueError:
                n = len(ans) - 1
                if operation == '+':
                    value = ans[n] + ans[n - 1]
                    ans.append(value)
                    ans_sum += value
                elif operation == 'D':
                    value = ans[n] * 2
                    ans.append(value)
                    ans_sum += value
                elif operation == 'C':
                    value = ans.pop()
                    ans_sum -= value
        
        return ans_sum