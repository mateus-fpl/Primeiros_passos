import java.util.Scanner;
public class vetor7 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int [] a = new int[10];
        int maiorNumero = 0, posicaoDoMaior = 0;
        System.out.println("Digite dez valores");
        for(int i=0; i<10; i++){
            System.out.print("Posição " + i +":");
            a[i] = scanner.nextInt();
           
            if (a[i] > maiorNumero){
                maiorNumero = a[i];
                posicaoDoMaior = i;
            }            
        }
        System.out.println("O maior número é " + maiorNumero + " e está na posição " + posicaoDoMaior);
        scanner.close();
    }
}
