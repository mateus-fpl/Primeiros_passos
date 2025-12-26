import javax.swing.JOptionPane;

public class LeituraCaracteres {
    public static void main (String [] args){
        String s;
        s = JOptionPane.showInputDialog("digite uma palavra");
        char letra1 = s.charAt(0);
        JOptionPane.showMessageDialog(null,"a primeira letra e " + letra1);
        JOptionPane.showMessageDialog(null, "o tamanho da palavra e " + s.length());

        int posicao = Integer.parseInt(JOptionPane.showInputDialog("escolha uma posicao"));

        if (posicao <= s.length() && posicao > 0){
        char outraLetra = s.charAt(posicao-1);
        JOptionPane.showMessageDialog(null, "a letra da posicao " + posicao + " e " + outraLetra);
        }
        else {
            JOptionPane.showMessageDialog(null,"posicao fora dos limites", "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }
    
}