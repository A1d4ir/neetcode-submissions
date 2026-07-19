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
                print(f'val: {val}')
                print(f'ans: {ans}')
            elif op == 'D':
                val = values[values_len] * 2
                values.append(val)
                ans += val
                print(f'val: {val}')
                print(f'ans: {ans}')
            elif op == 'C':
                val = values.pop()
                ans -= val
                print(f'val: {val}')
                print(f'ans: {ans}')
            else:
                val = int(op)
                values.append(val)
                ans += val
                print(f'val: {val}')
                print(f'ans: {ans}')
        
        return ans