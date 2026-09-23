class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result=[]
        for i in nums:
            count[i]=count.get(i,0)+1  #<- in place of this we can also write like this ->if i not in count(as dictionry):
            #                count[i]=0 else:count+=1

        result=sorted(count,key=count.get,reverse=True)
        return result[:k]

            