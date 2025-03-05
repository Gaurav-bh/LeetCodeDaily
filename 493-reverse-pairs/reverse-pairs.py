class Solution:
    def reversePairs(self, nums: List[int]) -> int:
       

        def merge(arr, low, mid, high):
    
            len1 = mid - low + 1;
            len2 = high - mid;
        
            first = [0]*len1;
            second = [0]*len2;
        
            k = low
            for i in range(0, len1):
                first[i] = arr[k]
                k+=1
        
            k = mid + 1;
            for i in range(0, len2):
                second[i] = arr[k]
                k+=1
        
            # Storing the elements in the arr
            # in sorted manner
            i = 0
            j = 0
            k = low
            while i < len1 and j < len2:
                if first[i] <= second[j]:
                    arr[k] = first[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = second[j];
                    k+=1
                    j+=1
        
            # Storing the left out elements
            # of first half
            while i < len1:
                arr[k] = first[i];
                k+=1
                i+=1
        
            # Storing the left out elements
            # of right half
            while j < len2:
                arr[k] = second[j]
                j+=1
                k+=1
        
        # Function to count the reverse pairs
        def countReversePairs(arr, low, mid, high):
            cnt = 0
            j = mid + 1
            for i in range(low, mid+1):
                #print(i,j)
                while j <= high and arr[i] > 2*arr[j]: 
                    #print("j:-",j)
                    j+=1
                    #print("j:-",j)
                cnt += (j - (mid + 1))
        
            return cnt
        
        def mergeSort(arr, low, high):
            cnt = 0;
            mid = low + (high - low) // 2;
            if low >= high:
                return cnt
        
            # Count the left half pairs
            cnt += mergeSort(arr, low, mid)
        
            # Count the right half pairs
            cnt += mergeSort(arr, mid + 1, high)
        
            # Function call to count the reverse pairs
            cnt += countReversePairs(arr, low, mid, high)
        
            # Merging the first and second half
            merge(arr, low, mid, high)
        
            return cnt
        return mergeSort(nums,0,len(nums)-1)
        