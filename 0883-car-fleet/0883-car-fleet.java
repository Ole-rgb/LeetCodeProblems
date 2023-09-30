class Solution {
    //Monotonic stack 
    public int carFleet(int target, int[] position, int[] speed) {
        if (position.length == 1) return 1;

        //stack, holds the time it takes for a car/fleet to reach the target
        Stack<Double> stack = new Stack<>();
        //map with position and speed
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i<position.length; i++){
            map.put(position[i], speed[i]);
        }
        Arrays.sort(position);


        for(int i = position.length-1; i>=0; i--){
            //calculates the time it takes for the car to arrive at the target
            double arrival =(double) (target-position[i])/map.get(position[i]);
            stack.push(arrival);

            if(stack.size() < 2){
                continue;
            }

            double arrivalLeft = stack.pop();
            double arrivalRight = stack.peek();
            //if the right car needs less time to arrive at the end, the left car will not catch up and they will not 
            //create a fleet. Therefore the left car needs to be added again
            if(arrivalRight < arrivalLeft){
                stack.push(arrivalLeft);
            }
        }
        
        return stack.size();
    }
}