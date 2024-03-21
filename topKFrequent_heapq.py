import heapq
import collections
def topKFrequent(nums, k):
    # dict_={}
    # for i in range(len(nums)):
    #     dict_[nums[i]]=dict_.get(nums[i],0)+1
    dict_ = collections.Counter(nums)
    
    temp_heap=[]
    print(dict_)
    for key,value in dict_.items():
        heapq.heappush(temp_heap,(key,value))
        if len(temp_heap)>k:
            heapq.heappop(temp_heap)
    res=[]
    while temp_heap:
        res.append(heapq.heappop(temp_heap)[1])
    print(res)
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))
    # for i in range(k):
