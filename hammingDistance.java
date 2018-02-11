class Solution {
    public int hammingDistance(int x, int y) {
        int compare = 1;
        int count = 0;
        if((x >= 0 && y < 0) || (y >= 0 && x < 0)) count++;
        for(int i = 0; i < 31; i++){
            if((x & compare) != (y & compare))
                count ++;
            compare = compare << 1;
        }
        return count;
    }
}
