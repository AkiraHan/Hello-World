class Solution {
    public int numJewelsInStones(String J, String S) {
        if(J.length()==0) return 0;
        int total = 0;
        for(int i = 0; i < S.length(); i++){
            String letter = S.substring(i,i+1);
            if(J.contains(letter))
                total++;
        }
        return total;
    }
}
