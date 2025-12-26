import java.util.Scanner;
public class vetor6 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int i = 0;
            System.out.println("Digites os valores do vetor A:");
        for(i=0;i<10;i++){
            a[i]=scanner.nextInt();
        }

        int maiorValor = a[0];
        int posicaoMaior = 0;
        int menorValor = a[0];
        int posicaoMenor = 0;

        for (i=0; i < a.length; i++){
            if (a[i]> maiorValor){
                maiorValor = a[i];
                posicaoMaior = i;
            }

            if (a[i]< menorValor){
                menorValor = a[i];
                posicaoMenor = i;
            }
        }
        scanner.close();
        System.out.println("O maior valor é " + maiorValor + ", enquanto o menor valor é " + menorValor + ".");
    }
}
