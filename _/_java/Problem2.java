public class problem2
{
    public static void main(String args[]) 
    {
        long num1=0,num2=1,temp,sum=0;
        long num = 4000000;
        while(num2<num)
        {
          temp=num2;
          num2=num1+num2;
          num1=temp;
         
          if(num2%2==0)
          {
              sum=sum+num2;
            }
        }
        System.out.print(sum);
    }
}
