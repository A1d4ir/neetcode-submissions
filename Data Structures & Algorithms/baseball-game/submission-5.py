class Solution:
    def calPoints(self, operations: List[str]) -> int:
        values = []
        ans = 0

        while len(operations) > 0:
            op = operations.pop(0)
            values_len = len(values) - 1

            if op == '+':
                val = values[values_len] + values[values_len - 1]
                values.append(val)
                ans += val
            elif op == 'D':
                val = values[values_len] * 2
                values.append(val)
                ans += val
            elif op == 'C':
                val = values.pop()
                ans -= val
            else:
                val = int(op)
                values.append(val)
                ans += val
        
        return ans