import java.util.Scanner;

public class vetor10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[15];
        int i = 0;
        int soma = 0;
        System.out.println("Digite as notas dos alunos:");
        for (i = 0; i < 15; i++) {
            a[i] = scanner.nextInt();
            soma = soma + a[i];
        }

        for (i = 0; i < 15; i++) {
            System.out.println("A nota do " + (i + 1) + "º aluno(a) é: " + a[i]);
        }

        double media = (double) soma / a.length;

        System.out.println("O total das notas é: " + soma);
        System.out.printf("A média das notas é: %.2f%n ", media);
        scanner.close();
    }
}
