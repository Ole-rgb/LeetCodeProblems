class Solution {
    public boolean isFascinating(int n) {
        String concatedNumbers = Integer.toString(n) + Integer.toString(2*n)+ Integer.toString(3*n);
        HashSet<Integer> numbers = new HashSet<>();
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
        System.out.println(concatedNumbers);
        System.out.println(numbers);
        return true;
    }
}