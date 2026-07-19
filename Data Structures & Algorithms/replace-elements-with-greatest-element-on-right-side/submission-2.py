class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                continue
            max_right_element = max(arr[i + 1:len(arr)])
            arr[i] = max_right_element
            
        arr[len(arr) - 1] = -1
        return arr