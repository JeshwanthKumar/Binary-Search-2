#Time_Complexity: O(log n)
#Space_Complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0     #Initialize low to 0
        high = len(nums)-1  #Initialize high to length of nums -1
        
        while low <= high: #Continue the loop until low is less than or equal to high
            mid = low + (high-low)//2   #Calculationg mid by floor dividing low+high by 2
            
            if ((mid == 0 or nums[mid] > nums[mid-1]) and (mid ==len(nums)-1 or nums[mid] > nums[mid+1])):
                return mid  #If the mid is 0 or the middle element is greater than the element previous to the middle and mid is at the last or the mid is greater than the next element to the middle, then return the mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                high = mid -1   #Else if mid is greater than 0 and the previous element to the mid is greater than the mid then move the high pointer to mid -1
            else:
                low = mid +1    #Else move the low pointer to mid + 1, because the next element is greater than the mid
             
        return -1      #If there is no peak in the array then return -1