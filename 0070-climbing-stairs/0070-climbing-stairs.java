class Solution {
    public int climbStairs(int n) {
        if(n == 1) return 1; //1
        if(n == 2) return 2; //1+1, 2

        int a=1;
        int b=2;
        int ans=0;

        for(int i = 0; i< n-2; i++){
            ans = a+b;
            a=b;
            b=ans;
        }
        return ans;
    }
}