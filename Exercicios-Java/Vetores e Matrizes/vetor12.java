import java.util.Scanner;

public class vetor12 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[5];
        int soma = 0;
        int media;
        int maiorValor;
        int menorValor;

        System.out.println("Digite 5 números para o arranjo:");

        a[0] = scanner.nextInt();
        soma = a[0];

        maiorValor = a[0];
        menorValor = a[0];

       for (int i = 1; i < 5; i++){
            a[i] = scanner.nextInt();
            soma = soma + a[i];

            if (a[i] > maiorValor){
                maiorValor = a[i];
            }
            if (a[i] < menorValor){
                menorValor = a[i];
            }
        }

        media = soma / a.length;

        System.out.println("----------Resultados:-----------");
        for (int i = 0; i < 5; i++){
            System.out.println("Os números do arranjo são: " + a[i]);
        }

        System.out.println("O maior número é " + maiorValor + " e o menor número é " + menorValor);
        System.out.println("A média dos números é: " + media);
        scanner.close();
    }
}