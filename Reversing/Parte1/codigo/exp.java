public class exp {
    public static void main(String[] args){
        int[] posiciones = {0, 29, 4, 2, 23, 3, 17, 1, 7, 10, 5, 9, 11, 15, 8, 12, 20, 14, 6, 24, 18, 13, 19, 21, 16, 27, 30, 25, 22, 28, 26, 31};
        char[] valoresEsperados = {'d', '3', 'r', '5', 'r', 'c', '4', '3', 'b', '_', '4', '3', 't', 'c', 'l', 'H', 'c', '_', 'm', '5', 'r', '3', '4', 'T', 'H', 'f', 'b', '_', '3', '6', 'f', '0'};

        for (int i = 0; i < posiciones.length; i++) {
            for(int j = 0; j < posiciones.length; j++) {
                if(i == posiciones[j]) {
                System.out.print(valoresEsperados[j]);
                }
            }
        }
    }
    
}
