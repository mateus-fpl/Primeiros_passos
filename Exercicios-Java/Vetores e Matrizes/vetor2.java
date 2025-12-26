import java.util.Scanner;

public class vetor2 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[6];
        int i = 0;
        System.out.println("Digite seis valores para a matriz:");
        for(i=0;i<6;i++){
            a[i] = scanner.nextInt();
        }
        System.out.println("Os valores são:");
        for(i=0;i<6;i++){
           System.out.println(a[i]);
        }
        scanner.close();
    }
}
