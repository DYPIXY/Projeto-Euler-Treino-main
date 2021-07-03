import javax.swing.*;
import java.util.*;
import static java.lang.Math.sqrt;

public class Função_Quadrática
{


//teste

    static void GUI()
    {
        String coluna[] = {"se", "no", "de"};   
        JFrame f;
        
            f = new JFrame();
            JTable func= new JTable();
            func.setBounds(30,40,200,300);
        
        System.out.println("worked");        
    
    }


    public static void main(String[] args)
    {

        int x1, x2;

        Scanner scan = new Scanner(System.in);
        //a
        System.out.print("valor de a: ");
        int a = scan.nextInt();
        if(a==0)
        {
            System.out.println("'a' não pode ser zero");
            return;
        }
        //b
        System.out.print("valor de b: ");
        int b = scan.nextInt();
        //c
        System.out.print("valor de c: ");
        int c = scan.nextInt();


        //não existe número real como resultado de raiz negativa, então se delta for menor que zero o conjunto solução (x1 e x2) será vazio.
        //delta

        double delta = b*b -4*a*c;
        if(delta<0)
        {
            System.out.println("delta resultou em um número negativo");
            return;
        }


        //bhaskara

        double raizDelta = sqrt(delta);

        x1 = (int) ((double)-b + raizDelta) / (2*a);
        x2 = (int) ((double)-b - raizDelta) / (2*a);


        //construção da parábola
        List<Integer> xvalores = new ArrayList<Integer>();
        List<Integer> yvalores = new ArrayList<Integer>();
        
        for(int x = -10 ; x<10 ; x++)
        {
            
            xvalores.add(x);
            
            //função quadrática para obter o y
            int y = a*(x*x) + b*x +c;
            
            yvalores.add(y);

        }


        //vértice
        int xv = -b/(2*a);
        int yv = (int)-delta/(4*a);


        //ponto máximo ou mínimo
        String ponto;
        if(a>0)
        {
            ponto = "mínimo";
        }
        else
        {
            ponto = "máximo";
        }
    }
}
/*
public class Graficos()
{


}
*/




