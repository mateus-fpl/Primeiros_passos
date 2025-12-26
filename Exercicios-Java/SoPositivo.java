// Ler um número qualquer e dizer se o número é positivo

import java.util.Scanner;

public class SoPositivo {

    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número: ");
        double numero = scanner.nextDouble();
        if (numero > 0){
            System.out.println(numero + " positivo ");
        }
        scanner.close();

    }
    
}
