import java.util.Scanner;

public class vetor15 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int i, j;
        int contador;

        System.out.println("Digite os números do arranjo:");
        for (i = 0; i < 10; i++) {
            a[i] = scanner.nextInt();
        }

        System.out.println("Lista sem os números repetidos:");

        for (i = 0; i < 10; i++) {

            contador = 0;  // reinicia o contador

            // conta quantas vezes o valor aparece
            for (j = 0; j < 10; j++) {
                if (a[i] == a[j]) {
                    contador++;
                }
            }

            // se aparecer mais de 1 vez, pula
            if (contador > 1) {
                continue;
            }

            // senão, imprime (pois é único)
            System.out.println(a[i]);
        }

        scanner.close();
    }
}