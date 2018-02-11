class Solution {
    public String complexNumberMultiply(String a, String b) {
        int[] La = new int[2];
        int[] Lb = new int[2];
        int signed = 1, start = 0;
        La = getNumber(a);
        Lb = getNumber(b);
        int newa = La[0] * Lb[0] - La[1] * Lb[1];
        int newb = La[0] * Lb[1] + La[1] * Lb[0];
        StringBuilder Bstrs = new StringBuilder();
        Bstrs.append(newa);
        Bstrs.append('+');
        Bstrs.append(newb);
        Bstrs.append('i');
        
        return Bstrs.toString();
    }
    
    private int[] getNumber(String a){
        int[] La = new int[2];
        int signed = 1, start = 0;
        for(int i = 0; i < a.length(); i++){
            char c = a.charAt(i);
            if(c == '-'){
                signed = -1;
                start = i+1;
            }
            if(c == '+'){
                La[0] = Integer.valueOf(a.substring(start, i)) * signed;
                signed = 1;
                start = i+1;
            }
            if(c == 'i'){
                La[1] = Integer.valueOf(a.substring(start, i)) * signed;
            }
        }
        return La;
    }
}
