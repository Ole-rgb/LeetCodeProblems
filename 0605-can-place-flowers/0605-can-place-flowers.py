class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        we can place a flower if the square before and after are also zero
        [1,0,0,0,1], n = 1
         ^ ^        
        [1,0,0,0,1], n = 1
         ^ ^ ^        
        [1,0,0,0,1], n = 1
           ^ ^ ^
        [1,0,0,0,1], n = 1
             ^ ^ ^
        [1,0,0,0,1], n = 1
               ^ ^
        usually check all three spots -> before, current, after  flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0

        edge cases -> BEGINNING(i=0) and END(i=len(flowerbed)-1)
        
        always check current index flowerbed[i] == 0
        if i == 0 dont check previous 
        if i == len(flowerbed)-1 dont check following 
        '''

        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
                
            # check the current square if its the first index dont check the one before and if its the last index dont check the one after
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1] ==0) and (i == len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n-=1
            
                if n == 0:
                    return True


        return 