class Solution {
    public boolean isFascinating(int n) {
        String concatedNumbers = Integer.toString(n) + Integer.toString(2*n)+ Integer.toString(3*n);
        HashSet<Integer> numbers = new HashSet<>();
    
       if(concatedNumbers.contains("0")) {
            return false;
       }

        for(char number : concatedNumbers.toCharArray()){

             if(!numbers.add(Integer.parseInt(String.valueOf(number)))){
                return false;
            }
        }

        if(numbers.size() == 9){
            return true;
        }
        
        return false;
    }
}