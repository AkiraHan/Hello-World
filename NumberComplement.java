class Solution {
    public int findComplement(int num) {
        if(num == 0) return 1;
        int result = 0;
        int digit = 1;
        while(num > 0){
            int s = (num % 2 == 0) ? 1 : 0;
            result += s * digit;
            digit *= 2;
            num /= 2;
        }
        return result;
    }
}
