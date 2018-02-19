class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<String>();
        if(S.length() == 0){ 
            result.add(S);
            return result;
        }
        getAllCase(S, result, 0, new StringBuilder());
        return result;
    }
    
    private void getAllCase(String S, List<String> result, int index, StringBuilder Bstrs){
        if(index == S.length() - 1){
            if(S.charAt(index) >= '0' && S.charAt(index) <= '9'){
                Bstrs.append(S.charAt(index));
                result.add(Bstrs.toString());
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
            }
            else{
                Bstrs.append(S.toLowerCase().charAt(index));
                result.add(Bstrs.toString());
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
                Bstrs.append(S.toUpperCase().charAt(index));
                result.add(Bstrs.toString());
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
            }
        }
        else{
            if(S.charAt(index) >= '0' && S.charAt(index) <= '9'){
                Bstrs.append(S.charAt(index));
                getAllCase(S, result, index+1, Bstrs);
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
            }
            else{
                Bstrs.append(S.toLowerCase().charAt(index));
                getAllCase(S, result, index+1, Bstrs);
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
                Bstrs.append(S.toUpperCase().charAt(index));
                getAllCase(S, result, index+1, Bstrs);
                Bstrs.delete(Bstrs.length()-1, Bstrs.length());
            }
        }
    }
}
