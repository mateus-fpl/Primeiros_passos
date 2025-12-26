//ler um número inteiro n, calcular e mostrar a tabuada do 0 ao 10

import java.util.Scanner;

public class tabuada {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número:");
        for (int numero = 1; numero <= 10; numero++) {
            System.out.println("\nTabuada do " + numero);
            for (int multiplicador = 0; multiplicador <= 10; multiplicador++) {
                System.out.println(numero + " x " + multiplicador + " = " + (numero * multiplicador));
            }
            System.out.println("\n");
        }
        scanner.close();
    }

}
