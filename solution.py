#User function Template for python3
import numpy 
from math import sqrt
class Solution:
        def isPrime(self,n):
            limit=int(n**0.5)
            if n<2:
                return False
            if n==2:
                return True
            if n%2==0:
                return False
            for i in range(3,limit+1,2):
                if n % i==0:
                    return False
       
            return True
        def primeProduct(self, l,r):
            prod=1
            if l <=2:
                prod=2
            if l%2==0:
                l+=1
            for i in range(l,r+1,2):
                if not self.isPrime(i):
                    continue
                prod=prod*i
           
            return prod % 1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.primeProduct(L, R))
# } Driver Code Ends
