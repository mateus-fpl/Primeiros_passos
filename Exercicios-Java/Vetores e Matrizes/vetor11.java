import java.util.Scanner;

public class vetor11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int i = 0;
        int soma = 0;
        int contNeg = 0;
        System.out.println("Digite os números do arranjo:");
        for (i = 0; i < 10; i++) {
            a[i] = scanner.nextInt();
            if (a[i] < 0) {
                contNeg++;
                
            } else {
                soma = soma + i;
            }
        }
        System.out.println("Quantidade de números negativos: " + contNeg);
        System.out.println("O resultado da somados números positivos é: " + soma);
        scanner.close();
    }
}
