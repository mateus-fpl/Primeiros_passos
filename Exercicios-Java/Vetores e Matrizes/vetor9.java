import java.util.Scanner;

public class vetor9 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[6];
        int i = 0;
        System.out.println("Digite números pares para o arranjo:");
        for (i=0; i<6; i++){
            int entrada;
            do {
                entrada = scanner.nextInt();

                if (entrada % 2 != 0){
                    System.out.println("ERRO! Digite um número par.");
                }
            } while (entrada % 2!=0);

            a[i] = entrada;
        }

        for (i= a.length -1; i>=0; i--){
            System.out.println("O valor da posição " + i + " é: " + a[i]);
        }
        scanner.close();
    }
}
