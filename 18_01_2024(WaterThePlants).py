#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here (StaringPoints)
        v = []
    
        for i in range(n):
            if gallery[i] != -1:
                v.append((i - gallery[i], i + gallery[i]))
    
        m = len(v)
        v.sort()
        target, i, ans = 0, 0, 0
    
        while target < n and i < m:
            if v[i][0] > target:
                return -1
    
            maxi = v[i][1]
            i += 1
    
            while i < m and v[i][0] <= target:
                maxi = max(maxi, v[i][1])
                i += 1
    
            target = maxi + 1
            ans += 1
    
        if target < n - 1:
            return -1
        else:
            return ans
        
         # Ending Points

