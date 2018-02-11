class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder Bstrs = new StringBuilder();
        for(int i = 0; i < words.length; i++){
            StringBuilder wordB = new StringBuilder();
            wordB = wordB.append(words[i]).reverse();
            Bstrs.append(wordB.toString());
            Bstrs.append(" ");
        }
        Bstrs.delete(Bstrs.length()-1,Bstrs.length());
        return Bstrs.toString();
    }
}
