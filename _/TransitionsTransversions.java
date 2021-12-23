public class TransitionsTransversions {
  public static void main( String[] args ) {
    String s1 = "TCAGGCAAAGCAGTGTCGACGGCCCGTTGTTCCCTAGCTTCTGCTCTGCACGGACCATAGGTCAAGTACTTTCTGCAGCAAACTCTAGCCCACACAACACAAATAGTGTAGCAGCTGGACTTTGCAATCTCACCAAGCAATGTCGCCGTATCGGTACACGAGCCCGCATAAGGCCAGTGAAGAGAACTGCATGAAAATCATACGTAGGTCAGCAGTTGTGAACAAGGAAAGTTATTATGGGGGGCAGTAGACTTGATATCTTACCAGCTACCTTGTGGCTTCTCCCTATCTCGACATAACAGCATTCCGGATCCGGCTCAATCTGAGGCTGATCCGTGTCTTATGGGCCAGCCATAAGACTTTATAAGTTCAGTGAGCGGAGGAAACTAGAACCGTTCAAGTCCATTGGCTCTACATCGTTTTATTAGGAAACGCAGGCTAAGACGTGCCTGCGCAGCACGTCCTACACACATGAATCAATCAGGAGAATGCAGCACCAAGGTTTAAGGCGTGCGACTAGGTGTAAATTCCAAATGCGGCTCAACGTATTGCGAGGTTTTCATCTCGCCAAACTTGTGGTGGTGGAGTGCAGTTCACGTAACGGGTATAGCGACCGTTCGTTGTAATGGCGTCGAGCGCGTGACCAGCTTTTACTAGCGCTAACAATATAGGAGCCTGGGAAGCTTAAAGGACGCGGGCTTCTTAGACAAAAACGGAATGCCGAGTAAGAGATGTACCAAAATCTATTTGTCGACGCAAAAGAGGTAAACGATCTCGCCCCGGATCGCTTGGAGCGCCATGCCTGGGCCGCCTCCTCCTTATCTACATACAAGTTTAGTTTACCTCGAAACAAACATGAAAGCCCTCGCGTTATGAAGGAATTACTGTTAGCGTGTACCGGCTTGAGTTGTCTGCCGTTCATCGATACTAAGTCGTACAATCTCATGCGGGTTCTGTTATTTCTTCTTCGCGGCTTGGCGC";
    String s2 = "TAAGGCAAAGCGGTGTCGATGGCTCCTAGTCCCCTAACTCTCGCACTGCTCGCCCGATAAGTCGAGGACTTTCTGCGGCAAGCCCAGGCCCATCGAGCACAAATAGCATCGCGTCCGGGCCCTGGAGTTTCGTCAAAAGGTATTGCTGTATCAGTACAGGAGTTCTCATATGGTCAGTGAAGAGTGCCGCGTAAAGATCGTACGTAGGCCCGCAGATCTGAACAGGGAAAGTTACTGTGGGGGGTACTGGCCTTGCCCTCTGATCGGTCACCTTGTGGGCTCTCCCTATCTTGCCATAATAACGATCCAGATTCTGCTCAAACCGGGGTTGGTGTGTGTTTTATGGACCGGCCGTAAGACTTAAGAGATTCAGTAAGCGAAGGAAACAAGAACTGTTCGAGCCCATGCACTCTACACCGTTTTGTCAGGAAACGCAGGCTAAAGGGTGTTCGTACTGCACATCCCACATATATGGACTTACCAGGGATAAGCGGTATTAAAATATACTGCGTGCGACCAGGCGTGGACGCCAGGTGCAGCTCAACGAATTGCGGCGCCTTCGTCCTGCCCACCTTGTAGGTACGGAGTGCCGCTCATGTAACGGCTATAGTAACTGTTTGTTGTATGGGGGTCAAAGGTGTGGCTAGCTTTAACTAACGCTGATATTACGGAAGTTTGACAAGTTCAGATGACGCAGGCTACTTAGATAAAGATAGAATGCCAAGTAGGGGATGAACGTAAACTCACTTGTCGAACCAAGAAAGGAAGGTCGTCTCGCCCCAGGTCGCCTGGGGCGCCATGCTTTGATCTTCCCCTCCTCAGCCGCATACAGGTCAAGTTCGCCTCGAACACAACATCAAACCCCTCGTGTTTTGAGAGATTGACTATTAGCCGGTATTGACTCGGGGAGCCTGTCTTTTATCGATACTAAATCGTACAATATCATGAGTGTTCTGTCATTATTATGTCGCGGCCTGGCGT";
    System.out.println(transitionTransversionRatio(s1,s2));
  }
  
  public static double transitionTransversionRatio( String s1, String s2 ) {
    int transitions = 0;
    int transversions = 0;
    for(int i = 0; i < s1.length(); ++i) {
      char c1 = s1.charAt(i);
      char c2 = s2.charAt(i);
           if(c1 == 'A' && c2 == 'G') { ++transitions; }
      else if(c1 == 'G' && c2 == 'A') { ++transitions; }
      else if(c1 == 'C' && c2 == 'T') { ++transitions; }
      else if(c1 == 'T' && c2 == 'C') { ++transitions; }
      else if(c1 == 'A' && c2 == 'C') { ++transversions; }
      else if(c1 == 'A' && c2 == 'T') { ++transversions; }
      else if(c1 == 'C' && c2 == 'A') { ++transversions; }
      else if(c1 == 'C' && c2 == 'G') { ++transversions; }
      else if(c1 == 'G' && c2 == 'C') { ++transversions; }
      else if(c1 == 'G' && c2 == 'T') { ++transversions; }
      else if(c1 == 'T' && c2 == 'A') { ++transversions; }
      else if(c1 == 'T' && c2 == 'G') { ++transversions; }
    }
    return (double)transitions / (double)transversions;
  }
}