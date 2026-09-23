class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"@#"+i
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j:j+2]!="@#":
                j+=1
            length=int(s[i:j])
            word=s[j+2:j+2+length]
            result.append(word)
            i=j+2+length
        return result


