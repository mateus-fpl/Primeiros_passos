import java.util.Scanner;

public class vetor17 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[]= new int [10];
        System.out.println("Digite dez valores:");
        for (int i=0; i<10; i++){
            System.out.print("Posição " + i + ": ");
            a[i] = scanner.nextInt();
             if (a[i]<0){
                a[i]=0;
            }
        }
        System.out.print("Elementos: ");
        
        for (int valor : a) {
            System.out.print(valor + " ");
        }
        System.out.println();
        scanner.close();
    }    
}
