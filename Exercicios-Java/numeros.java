import java.util.Scanner;

public class numeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número");
        int n = scanner.nextInt();
        int i = n;
        int soma = 0;
        while (i > 0) {
            soma = soma + i;
            i = i - 1;
            System.out.println(i);
         }
         double media = (double) soma/n;
         System.out.println("A soma dos números é:" + soma);
         System.out.println("A média é: " + media);
         scanner.close();
    }
}
