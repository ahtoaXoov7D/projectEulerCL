
public class Question9{
    public static void main(String args[]){
        
        for(int i = 0; i < 1000; ++i){
            for(int j = i+1; j < 1000; ++j){
                int k = 1000 - j - i;
                if(i!=k && j!=k && i!=j && i*i + j*j == k*k){
                    System.out.println(i*j*k);
                }
            }
        }
    }
}