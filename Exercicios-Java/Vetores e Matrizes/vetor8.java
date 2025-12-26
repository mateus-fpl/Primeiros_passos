import java.util.Scanner;

public class vetor8 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[6];
        int i = 0;
        System.out.println("Digite os valores da vetor A:");

        for (i=0; i<6; i++){
            a[i]= scanner.nextInt();
        }

        for (i= a.length - 1;i>=0 ;i--){            
            System.out.println("O valor da posição " + i + " é: " + a[i]);
            }
        scanner.close();
            
    }    
}
