class Solution {
    public boolean checkStraightLine(int[][] coordinates) {

        if(coordinates.length<=2){
            return true;
        }
        int x0= coordinates[0][0];
        int y0= coordinates[0][1];
        int x1=coordinates[1][0];
        int y1= coordinates[1][1];

        for(int i = 2; i<coordinates.length; i++){
            int xi=coordinates[i][0];
            int yi= coordinates[i][1];
 
            /*
                slope=(py2-py1)/(px2-x1) between the first two points 
                compare that slope to other slopes (between point 0 and the ith point)

                (y2-y1)/(x2-x1) = (yi-py1)/(xi-x1)
                
                Possible error (xi-x1) == 0

                therefor multiply by (x2-x1) and (xi-x1)
                ->(y2-y1) * (xi-x1) = (yi-y1) * (x2-x1)
                
                indent indices
            */
        if((y1-y0)*(xi-x0) != (yi-y0)*(x1-x0)) return false;
        }

        return true;
    }

}