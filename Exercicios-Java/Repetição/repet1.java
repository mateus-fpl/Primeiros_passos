import java.util.Scanner;

public class repet1 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int contador = 0;
        
        for(int i = 1; contador<5; i++){
            if (i%3==0){

                contador++;

                System.out.println(i + " é o " + contador + "º múltiplo de três.");
           }
                      
        }
        scanner.close();
    }
}