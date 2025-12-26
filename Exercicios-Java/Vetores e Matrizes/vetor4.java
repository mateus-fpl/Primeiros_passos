import java.util.Scanner;
import java.util.Random;

public class vetor4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int a[] = new int[8];
        int i = 0;
        System.out.println("Digite oito valores para o vetor:");
        for (i = 0; i < 8; i++) {
            a[i] = scanner.nextInt();
        }
        int indice1 = random.nextInt(8);
        int indice2 = random.nextInt(8);
        int soma = indice1 + indice2;
        System.out.println("A soma do valor " + indice1 + " + " + indice2 + " é: " + soma);
        scanner.close();
    }
}
