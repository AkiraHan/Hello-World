class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> result = new ArrayList<Integer>();
        HashMap<Character, Integer> HS = new HashMap<Character, Integer>();
        for(int i = 0; i < S.length(); i++){
            if(!HS.containsKey(S.charAt(i)))
                HS.put(S.charAt(i),i+1);
            else
                HS.replace(S.charAt(i),i+1);
        }
        int curLen = HS.get(S.charAt(0));
        int left = 0;
        for(int i = 0; i < S.length(); i++){
            if(HS.get(S.charAt(i)) > curLen)
                curLen = HS.get(S.charAt(i));
            if(i == curLen-1){
                result.add(curLen - left);
                left = curLen;
            }
        }
        return result;
    }
}
