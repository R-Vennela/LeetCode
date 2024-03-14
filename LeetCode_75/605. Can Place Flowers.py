class Solution:
    def canPlaceFlowers(self, flowerbed, n) :
        length = len(flowerbed)
        i = 0
        
        while i < length:
            if flowerbed[i] == 0:
                # Check the next plot (flowerbed[i+1])
                next_ = flowerbed[i + 1] if i < length - 1 else 0
                
                if next_ == 0:
                    n -= 1
                    i += 2  # Skip the next plot as it cannot have a flower**
                else:
                    i += 1  # Move to the plot after the next one**
                if n == 0:
                    return True #No need to check the entire array, if all the required plants plotted
            else:
                i += 2  # Skip the current plot as it already has a flower**
        
        return n <= 0 