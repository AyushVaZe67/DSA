class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        pattern = re.compile(r'^[a-zA-Z0-9_]+$')

        valid = []
        for i in range(len(code)):
            if code[i] and pattern.match(code[i]) and businessLine[i] in order and isActive[i]:
                valid.append((code[i], businessLine[i]))
            
        valid.sort(key=lambda x: (order[x[1]], x[0]))
        return [coupon[0] for coupon in valid]