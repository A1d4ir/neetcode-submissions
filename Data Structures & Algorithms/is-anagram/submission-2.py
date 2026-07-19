class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sList = list(s)
        tList = list(t)
        
        for letter in sList:
            if letter not in tList:
                print('Is not an anagram', tList);
                return False
            else:
                tList.remove(letter)
        
        return True