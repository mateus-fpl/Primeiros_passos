import java.util.Scanner;

public class Vetores {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] a = new int[5];
        int[] b = new int[5];
        int[] c = new int[5];

        System.out.println("Digite os valores do primeiro vetor:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Posicao " + i + ": ");
            a[i] = scanner.nextInt();
        }

        System.out.println("Digite os valores do segundo vetor:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Posicao " + i + ": ");
            b[i] = scanner.nextInt();
        }

        System.out.println("A soma dos vetores é:");
        for (int i = 0; i < 5; i++) {
            c[i] = a[i] + b[i];
            System.out.println(c[i]);
        }

        scanner.close();
    }

}
