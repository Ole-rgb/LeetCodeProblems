class Solution {
    /*
        Runtime 0(n)
        Idea:   (Seen in simular two pointers problem) -> one pointer moves over the entire array (i) and one pointer (index) only moves from the start, if condition is met (in this case even number found) and copies the number to the index
                [3,1,2,4]   [3,1,2,4]   [3,1,2,4]   [2,1,3,4]   [2,1,3,4]   [2,4,3,1]
        i        ^             ^             ^             ^           ^
        index    ^           ^           ^  ^          ^           ^
                 
    */
    public int[] sortArrayByParity(int[] nums) {
        int index = 0;
        for(int i = 0; i<nums.length; i++){
            //if even 
            if(nums[i] % 2 == 0){
                int tmp = nums[i];
                nums[i] = nums[index];
                nums[index] = tmp;
                
                index++;
            }
        }
        return nums;
    }
}