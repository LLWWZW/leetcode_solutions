class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for str_ in n_str:
                new_num += int(str_)**2
            n = new_num
            if n == 1:
                return True
        return False