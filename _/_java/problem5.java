public class problem5
{
    public static void main(String args[])
    {
        int count=1;
        int num=11;
      while(count!=20)
      {
          for(int i = 1;i<=20;i++)
          {
              if((num%i)==0)
              {
                  count+=1;
                 // System.out.println(num);
                }
                else
                {
                    count=0;
                }
            }
            num+=1;
        }
        System.out.println(num-1);
    }
}
//OUTPUT
//232792560
