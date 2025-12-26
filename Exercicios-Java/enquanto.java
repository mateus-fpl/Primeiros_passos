import java.util.Scanner;

public class enquanto {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
       var name="";
        while(!name.equals("exit")){
            System.out.println("Informe um nome:");
            name = scanner.next();
                      
       } 
       scanner.close();
    }
    
}
