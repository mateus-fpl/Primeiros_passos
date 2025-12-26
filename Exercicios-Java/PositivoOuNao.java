//Ler se um número é positivo ou não
import java.util.Scanner;

public class PositivoOuNao {

    public static void main (String[] ars){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número: ");
        double numero = scanner.nextDouble();
        if (numero > 0) {
            System.out.println(numero + " é positivo");
        }
        else {
            System.out.println(numero + "não é positivo");
        }
        scanner.close();
    }
    
}
