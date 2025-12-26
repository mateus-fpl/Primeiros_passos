import java.util.Scanner;

public class LeAteDigitar0 {
    public static void main (String[] args){
        int numero;
        Scanner scanner = new Scanner(System.in);
        do {
         System.out.println("Digite sua sequencia de numeros, 0 encerra:"); 
         numero = scanner.nextInt();
        } while (numero !=0);
        scanner.close();
    }
}
