class Solution {
    /*
    nums = [3,1,5,4,2]    nums = [3,1,5,4,2]    nums = [3,1,5,4,2]      nums = [3,1,5,4,2]
                    ^                   ^                   ^                     ^        
    add 2                 dont add 4                 dont add 5         add 1 -> size of set == k 
    */  
    public int minOperations(List<Integer> nums, int k) {
        HashSet<Integer> set = new HashSet<>();
        int i=nums.size()-1;
        for(; i >= 0 && set.size() != k; i--){
            if(nums.get(i) <= k){
                set.add(nums.get(i));
            }
        }

        return nums.size() -i -1;
    }
}