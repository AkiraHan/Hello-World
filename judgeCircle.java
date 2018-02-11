class Solution {
    public boolean judgeCircle(String moves) {
        int Up = 0, Do = 0, Le = 0, Ri = 0;
        for(int i = 0; i < moves.length(); i++){
            char c = moves.charAt(i);
            switch(c){
                case 'U': Up++;
                    break;
                case 'D': Do++;
                    break;
                case 'L': Le++;
                    break;
                case 'R': Ri++;
                    break;
            }
        }
        
        return (Up == Do) && (Le == Ri);
    }
}
