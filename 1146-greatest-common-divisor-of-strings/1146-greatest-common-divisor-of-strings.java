class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) return "";

        int endIndex = gcd(str1.length(), str2.length());
        return str1.substring(0, endIndex);
    }

    private int gcd(int a, int b) {
        if (a == 0) return b;

        while (b != 0) {
            if (a > b)
                a = a - b;
            else
                b = b - a;
        }

        return a;
    }
}