import java.util.Scanner;

public class BuscaSimples {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] v = new int[5];
        int i, x; // i é o contador e x é o valor que vai ser procurado
        boolean achou = false;

        System.out.print("Digite os 5 valores para o vetor:");
        for (i = 0; i < 5; i++) {
            v[i] = scanner.nextInt();
        }
        System.out.println("Digite o valor para a busca:");
        x = scanner.nextInt();
        for (i = 0; i < 5 && !achou; i++) {
            if (v[i] == x) {
                achou = true;
            }
        }

        if (achou) {
            System.out.println(x + " esta no vetor");
        } else {
            System.out.println(x + " Nao esta no vetor");
        }

        // verificar quais elementos possuem um estoque acima de 20
        i = 0;
        while (i < 5) {
            if (v[i] > 20) {
                System.out.println("O produto " + i + " tem estoque " + v[i]);
            }
            i++;
        }
        scanner.close();
    }

}
