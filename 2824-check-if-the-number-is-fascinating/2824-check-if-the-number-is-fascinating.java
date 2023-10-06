class Solution {
    public boolean isFascinating(int n) {
        String concatedNumbers = Integer.toString(n) + Integer.toString(2*n)+ Integer.toString(3*n);
        HashSet<Integer> numbers = new HashSet<>();
    
       if(concatedNumbers.contains("0")) return false;
       if(concatedNumbers.length()>9) return false;

        for(char number : concatedNumbers.toCharArray()){
            if(number == '0'){
                return false;
            }
            else if(!numbers.add(Integer.parseInt(String.valueOf(number)))){
                return false;
            }
        }

        for(int i = 1; i<10; i++){
            if(!numbers.contains(i)){
                return false;
            }
        }
        
        return true;
    }
}