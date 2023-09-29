class Solution {
    /*
        Runtime O(n)
    */

    public boolean isMonotonic(int[] nums) {
        if(nums.length<2){
            return true;
        }
        boolean isIncreasing = true;
        boolean isDecreasing = true; 

        for(int i = 1; i<nums.length; i++ ){
            if(nums[i-1] > nums[i] ){
                isIncreasing = false;
            }
        }

        for(int i = 1; i<nums.length; i++){
            if(nums[i-1] < nums[i]){
                isDecreasing = false;
            }
        }

        return isIncreasing || isDecreasing; 
    }
}