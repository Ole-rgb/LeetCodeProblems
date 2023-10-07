class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> greatesCandies = new ArrayList<>();
        int maxCandies = 0;

        for(int candy : candies) {
            if(maxCandies<candy){
                maxCandies=candy;
            }
        } 

        for(int candy : candies){
            greatesCandies.add(candy + extraCandies >= maxCandies);
        }

        return greatesCandies;
    }
}