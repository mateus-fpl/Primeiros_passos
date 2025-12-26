import java.util.Scanner;

public class vetor16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[5];
        int i = 0;
        int opcao;
        System.out.println("Digite os números do arranjo:");
        for (i = 0; i < 5; i++) {
            a[i] = scanner.nextInt();
        }
        System.out.println("Escolha a opção 0, 1 ou 2:");
        opcao = scanner.nextInt();
        System.out.println("\n");
        switch (opcao) {
            case 1:
                for (i = 0; i < 5; i++) {
                    System.out.println("Ordem direta: " + a[i]);
                }
                break;

            case 2:
                for (i = a.length - 1; i >= 0; i--) {
                    System.out.println("Ordem contrária: " + a[i]);
                }
                break;

            case 3:
                if (opcao != 1 && opcao != 2) {
                    System.out.println("Programa encerrado!");
                }
        }

        scanner.close();

    }
}
