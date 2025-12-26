import java.util.Scanner;

public class repet7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i, entrada;
        int soma = 0;
        System.out.println("Digite 10 números:");
        for (i = 0; i < 10; i++) {
            do {
                entrada = scanner.nextInt();
                if (entrada < 0) {
                    System.out.println("Digite um número positivo!");
                }
            } while (entrada < 0);

            soma = soma + entrada;

        }
        int media = soma / i;
        System.out.println("O total dos números positivos válidos é: " + soma + " e sua média é: " + media);
        scanner.close();
    }
}
