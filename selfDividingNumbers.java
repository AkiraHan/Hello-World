class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<Integer>();
        for(int i = left; i <= right; i++){
            int num = i;
            while(num > 0){
                int digit = num % 10;
                if(digit == 0) break;
                if(i % digit != 0) break;
                num /= 10;
                if(num == 0) result.add(i);
            }
        }
        return result;
    }
}
