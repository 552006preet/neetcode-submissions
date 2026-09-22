class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
    
        if n!=m:
            return False
            
        countS=Counter(s)
        countT=Counter(t)
        if countS==countT:
            return True
        return False

        