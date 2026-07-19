class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            greatest = 0
            for j in range(i + 1, len(arr)):
                print(f'arr[j]: {arr[j]}')
                if arr[j] > greatest:
                    greatest = arr[j]
            arr[i] = greatest
        
        arr[len(arr) - 1] = -1
        return arr