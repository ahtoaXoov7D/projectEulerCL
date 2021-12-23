

public class ass2
{

  public static void main(String[] args) {
    int a=8;
    int x=0;
    x=a++ + ++a +a++;
    System.out.println(x+','+a);//28,11
    a=8;
    System.out.println(a++ +','+ ++a +','+ a++);//8,10,10
    System.out.println(--a+','+ a +','+ a--);//10,10,10
  }
   
}
