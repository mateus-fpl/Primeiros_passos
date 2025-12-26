import java.util.Scanner;

public class vetor19 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[50];
        int i;
        for (i=0;i<50;i++){
             a[i] = (i + 5 * i) % (i+ 1);
             System.out.print(a[i] + " ");
        }
        scanner.close();

    }
}
