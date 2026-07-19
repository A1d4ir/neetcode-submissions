class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr

        k = 0;
        n = len(arr) # 2
        i = 1
        arr[k] = arr[i]

        while k < n - 1:
            if i == n:
                k += 1
                i = k + 1
                if i < n:
                    arr[k] = arr[i]
                else:
                    arr[n - 1] = -1
                    
            elif arr[k] < arr[i]:
                arr[k] = arr[i]
                i += 1
            else:
                i += 1

        return arr