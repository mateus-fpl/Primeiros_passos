//Ler um número e dizer se ele é positivo, negativo ou neutro

import java.util.Scanner;

public class PositivoNegativoNeutro {
    
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número qualquer:");
        double numero = scanner.nextDouble();
        if (numero > 0) {
            System.out.println(numero + " é positivo");
        }
        else if (numero < 0){
            System.out.println(numero + " é negativo");
        }
        else {
            System.out.println(numero + " é neutro");
        }
        scanner.close();
    }

}
