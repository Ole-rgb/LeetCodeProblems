class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> greatesCandies = new ArrayList<>();
        int maxCandies = 0;

        //get the maxCandies
        for(int candy : candies){
            maxCandies = Math.max(maxCandies, candy);
        }

        //is candies[i] + extracCandies > maxCandies
        for(int candy : candies){
            greatesCandies.add(candy + extraCandies >= maxCandies);
        }

        return greatesCandies;
    }
}