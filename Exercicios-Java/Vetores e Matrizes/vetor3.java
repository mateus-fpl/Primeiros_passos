import java.util.Scanner;
public class vetor3 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int i = 0;
        System.out.println("Digite os valores da matriz A:");
        for (i=0;i<10;i++){
            a[i] = scanner.nextInt();
        }
        System.out.println("O quadrados dos seguintes valores são:");
        for(i=0;i<10;i++){
            b[i]= a[i] * a[i];
        System.out.println(b[i]);
        }
        scanner.close();
    }
}
