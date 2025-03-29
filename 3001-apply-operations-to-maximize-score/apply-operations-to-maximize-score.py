class Solution:
    MOD = 10**9 + 7
    def maximumScore(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def prime_list(nums):
            MAXN = max(nums)
            spf = [1] * (MAXN + 1)
            
            def sieve():
                spf[0] = 0
                for i in range(2, MAXN + 1):
                    if spf[i] == 1: 
                        for j in range(i, MAXN + 1, i):
                            if spf[j] == 1:  
                                spf[j] = i

            def getFactorization(x):
                ret = list()
                while (x > 1):
                    if spf[x] not in ret:
                        ret.append(spf[x])
                    x = x // spf[x]  
                return ret   
            sieve()
            prime=[]
            for num in nums:
                prime.append(len(getFactorization(num)))

            return prime
        

        prime=prime_list(nums)

        print(prime)
        
        
        def greater_prime(nums,prime,n):
            right=[n for i in range(n)]
            left=[-1 for i in range(n)]
            stack=[0]
            for i in range(1,n):
                curr=nums[i]
                while stack and prime[stack[-1]]<prime[i]:
                    ind=stack.pop()
                    right[ind]=i
                if stack:
                    left[i]=stack[-1]
                stack.append(i)
            return right,left
        right,left=greater_prime(nums,prime,n)

        print(left)
        print(right)
        #ranges
        ranges=[0 for i in range(n)]
        for i in range(n):
            ranges[i]=(i - left[i]) * (right[i] - i)
        print(ranges)


        processing_queue = []

        # Push each number and its index onto the priority queue
        for index in range(n):
            heapq.heappush(processing_queue, (-nums[index], index))

        score = 1

        # Helper function to compute the power of a number modulo MOD
        def _power(base, exponent):
            res = 1

            # Calculate the exponentiation using binary exponentiation
            while exponent > 0:
                # If the exponent is odd, multiply the result by the base
                if exponent % 2 == 1:
                    res = (res * base) % self.MOD

                # Square the base and halve the exponent
                base = (base * base) % self.MOD
                exponent //= 2

            return res

        while k > 0:
            # Get the element with the maximum value from the queue
            num, index = heapq.heappop(processing_queue)
            num = -num  # Negate back to positive

            # Calculate the number of operations to apply on the current element
            operations = min(k, ranges[index])

            # Update the score by raising the element to the power of operations
            score = (score * _power(num, operations)) % self.MOD

            # Reduce the remaining operations count
            k -= operations

        return score
    
        