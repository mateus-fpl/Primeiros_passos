import java.util.Scanner;

public class vetor13 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[5];
        int i=0;
        int maiorValor, menorValor;
        int posicaoDoMaior = 0;
        int posicaoDoMenor = 0;
        System.out.println("Digite 5 valores para o arranjo:");
        a[0] = scanner.nextInt();
        maiorValor = a[0];
        menorValor = a[0];
        for (i=1; i<5; i++){
            a[i] = scanner.nextInt();

            if (a[i] > maiorValor){
                maiorValor = a[i];
                posicaoDoMaior = i;
            }

            if (a[i] < menorValor){
                menorValor = a[i];
                posicaoDoMenor=i;
            }
        }
        System.out.println("O maior valor é " + maiorValor + " e se encontra na posição " + (posicaoDoMaior + 1));
        System.out.println("O menor valor é " + menorValor + " e se encontra na posição " + (posicaoDoMenor + 1));
        scanner.close();
    }
}
