class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1 = defaultdict()
        dict_nums2 = defaultdict()

        for i in nums1:
            if i not in dict_nums1:
                dict_nums1[i] = 1
            else:
                dict_nums1[i] += 1
        for i in nums2:
            if i not in dict_nums2:
                dict_nums2[i] = 1
            else:
                dict_nums2[i] += 1
        
        res = []
        for key,val in dict_nums1.items():
            if key in dict_nums2.keys():
                res.append(key)
        return res