package bits;

class SumOfTwoIntegers{
    public int getSum(int a, int b) {
        
        while ( b != 0){
            // temp is to calculate before a is altered
            int temp = (a & b) << 1; 
            a = a ^ b;
            b = temp;
        }

        return a;
    }
    /*
     * Some things of note, aparrently even if there
     * is not for loop, bitwise operators already work on
     * all bits automatically without being explicitly called to
     * do so. This is also why we did not need to trasnform them into
     * bits which is interesting
     */
}