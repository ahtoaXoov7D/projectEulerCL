#!/usr/bin/sed -nf

b main

:start

# Stop if done
/^[0-9]*$/ {
  s/^0\+\([0-9]\)/\1/g
  b main
}

# Parentheses which house a single number can be removed
s#(\([0-9]\+\))#\1#g
t start

# 0 + x = x
s#(0\++\([0-9]\+\))#(\1)#g
t start

# x + 0 = x
s#(\([0-9]\+\)+0\+)#(\1)#g
t start

# Manuever the carry bit
s/0c/1/g
t start
s/1c/2/g
t start
s/2c/3/g
t start
s/3c/4/g
t start
s/4c/5/g
t start
s/5c/6/g
t start
s/6c/7/g
t start
s/7c/8/g
t start
s/8c/9/g
t start
s/9c/c0/g
t start
s/(c/(1/g
t start
s/+c/+1/g
t start
s/^c/1/g
t start

# If we ran out of digits, fix it
s#(+#(0+#g
t start
s#+)#+0)#g
t start

# Manuever the end digits
s#(\([0-9]*\)0+\([0-9]*\)0)#(\1+\2)0#g
t start
s#(\([0-9]*\)0+\([0-9]*\)1)#(\1+\2)1#g
t start
s#(\([0-9]*\)0+\([0-9]*\)2)#(\1+\2)2#g
t start
s#(\([0-9]*\)0+\([0-9]*\)3)#(\1+\2)3#g
t start
s#(\([0-9]*\)0+\([0-9]*\)4)#(\1+\2)4#g
t start
s#(\([0-9]*\)0+\([0-9]*\)5)#(\1+\2)5#g
t start
s#(\([0-9]*\)0+\([0-9]*\)6)#(\1+\2)6#g
t start
s#(\([0-9]*\)0+\([0-9]*\)7)#(\1+\2)7#g
t start
s#(\([0-9]*\)0+\([0-9]*\)8)#(\1+\2)8#g
t start
s#(\([0-9]*\)0+\([0-9]*\)9)#(\1+\2)9#g
t start
s#(\([0-9]*\)1+\([0-9]*\)0)#(\1+\2)1#g
t start
s#(\([0-9]*\)1+\([0-9]*\)1)#(\1+\2)2#g
t start
s#(\([0-9]*\)1+\([0-9]*\)2)#(\1+\2)3#g
t start
s#(\([0-9]*\)1+\([0-9]*\)3)#(\1+\2)4#g
t start
s#(\([0-9]*\)1+\([0-9]*\)4)#(\1+\2)5#g
t start
s#(\([0-9]*\)1+\([0-9]*\)5)#(\1+\2)6#g
t start
s#(\([0-9]*\)1+\([0-9]*\)6)#(\1+\2)7#g
t start
s#(\([0-9]*\)1+\([0-9]*\)7)#(\1+\2)8#g
t start
s#(\([0-9]*\)1+\([0-9]*\)8)#(\1+\2)9#g
t start
s#(\([0-9]*\)1+\([0-9]*\)9)#(\1+\2)c0#g
t start
s#(\([0-9]*\)2+\([0-9]*\)0)#(\1+\2)2#g
t start
s#(\([0-9]*\)2+\([0-9]*\)1)#(\1+\2)3#g
t start
s#(\([0-9]*\)2+\([0-9]*\)2)#(\1+\2)4#g
t start
s#(\([0-9]*\)2+\([0-9]*\)3)#(\1+\2)5#g
t start
s#(\([0-9]*\)2+\([0-9]*\)4)#(\1+\2)6#g
t start
s#(\([0-9]*\)2+\([0-9]*\)5)#(\1+\2)7#g
t start
s#(\([0-9]*\)2+\([0-9]*\)6)#(\1+\2)8#g
t start
s#(\([0-9]*\)2+\([0-9]*\)7)#(\1+\2)9#g
t start
s#(\([0-9]*\)2+\([0-9]*\)8)#(\1+\2)c0#g
t start
s#(\([0-9]*\)2+\([0-9]*\)9)#(\1+\2)c1#g
t start
s#(\([0-9]*\)3+\([0-9]*\)0)#(\1+\2)3#g
t start
s#(\([0-9]*\)3+\([0-9]*\)1)#(\1+\2)4#g
t start
s#(\([0-9]*\)3+\([0-9]*\)2)#(\1+\2)5#g
t start
s#(\([0-9]*\)3+\([0-9]*\)3)#(\1+\2)6#g
t start
s#(\([0-9]*\)3+\([0-9]*\)4)#(\1+\2)7#g
t start
s#(\([0-9]*\)3+\([0-9]*\)5)#(\1+\2)8#g
t start
s#(\([0-9]*\)3+\([0-9]*\)6)#(\1+\2)9#g
t start
s#(\([0-9]*\)3+\([0-9]*\)7)#(\1+\2)c0#g
t start
s#(\([0-9]*\)3+\([0-9]*\)8)#(\1+\2)c1#g
t start
s#(\([0-9]*\)3+\([0-9]*\)9)#(\1+\2)c2#g
t start
s#(\([0-9]*\)4+\([0-9]*\)0)#(\1+\2)4#g
t start
s#(\([0-9]*\)4+\([0-9]*\)1)#(\1+\2)5#g
t start
s#(\([0-9]*\)4+\([0-9]*\)2)#(\1+\2)6#g
t start
s#(\([0-9]*\)4+\([0-9]*\)3)#(\1+\2)7#g
t start
s#(\([0-9]*\)4+\([0-9]*\)4)#(\1+\2)8#g
t start
s#(\([0-9]*\)4+\([0-9]*\)5)#(\1+\2)9#g
t start
s#(\([0-9]*\)4+\([0-9]*\)6)#(\1+\2)c0#g
t start
s#(\([0-9]*\)4+\([0-9]*\)7)#(\1+\2)c1#g
t start
s#(\([0-9]*\)4+\([0-9]*\)8)#(\1+\2)c2#g
t start
s#(\([0-9]*\)4+\([0-9]*\)9)#(\1+\2)c3#g
t start
s#(\([0-9]*\)5+\([0-9]*\)0)#(\1+\2)5#g
t start
s#(\([0-9]*\)5+\([0-9]*\)1)#(\1+\2)6#g
t start
s#(\([0-9]*\)5+\([0-9]*\)2)#(\1+\2)7#g
t start
s#(\([0-9]*\)5+\([0-9]*\)3)#(\1+\2)8#g
t start
s#(\([0-9]*\)5+\([0-9]*\)4)#(\1+\2)9#g
t start
s#(\([0-9]*\)5+\([0-9]*\)5)#(\1+\2)c0#g
t start
s#(\([0-9]*\)5+\([0-9]*\)6)#(\1+\2)c1#g
t start
s#(\([0-9]*\)5+\([0-9]*\)7)#(\1+\2)c2#g
t start
s#(\([0-9]*\)5+\([0-9]*\)8)#(\1+\2)c3#g
t start
s#(\([0-9]*\)5+\([0-9]*\)9)#(\1+\2)c4#g
t start
s#(\([0-9]*\)6+\([0-9]*\)0)#(\1+\2)6#g
t start
s#(\([0-9]*\)6+\([0-9]*\)1)#(\1+\2)7#g
t start
s#(\([0-9]*\)6+\([0-9]*\)2)#(\1+\2)8#g
t start
s#(\([0-9]*\)6+\([0-9]*\)3)#(\1+\2)9#g
t start
s#(\([0-9]*\)6+\([0-9]*\)4)#(\1+\2)c0#g
t start
s#(\([0-9]*\)6+\([0-9]*\)5)#(\1+\2)c1#g
t start
s#(\([0-9]*\)6+\([0-9]*\)6)#(\1+\2)c2#g
t start
s#(\([0-9]*\)6+\([0-9]*\)7)#(\1+\2)c3#g
t start
s#(\([0-9]*\)6+\([0-9]*\)8)#(\1+\2)c4#g
t start
s#(\([0-9]*\)6+\([0-9]*\)9)#(\1+\2)c5#g
t start
s#(\([0-9]*\)7+\([0-9]*\)0)#(\1+\2)7#g
t start
s#(\([0-9]*\)7+\([0-9]*\)1)#(\1+\2)8#g
t start
s#(\([0-9]*\)7+\([0-9]*\)2)#(\1+\2)9#g
t start
s#(\([0-9]*\)7+\([0-9]*\)3)#(\1+\2)c0#g
t start
s#(\([0-9]*\)7+\([0-9]*\)4)#(\1+\2)c1#g
t start
s#(\([0-9]*\)7+\([0-9]*\)5)#(\1+\2)c2#g
t start
s#(\([0-9]*\)7+\([0-9]*\)6)#(\1+\2)c3#g
t start
s#(\([0-9]*\)7+\([0-9]*\)7)#(\1+\2)c4#g
t start
s#(\([0-9]*\)7+\([0-9]*\)8)#(\1+\2)c5#g
t start
s#(\([0-9]*\)7+\([0-9]*\)9)#(\1+\2)c6#g
t start
s#(\([0-9]*\)8+\([0-9]*\)0)#(\1+\2)8#g
t start
s#(\([0-9]*\)8+\([0-9]*\)1)#(\1+\2)9#g
t start
s#(\([0-9]*\)8+\([0-9]*\)2)#(\1+\2)c0#g
t start
s#(\([0-9]*\)8+\([0-9]*\)3)#(\1+\2)c1#g
t start
s#(\([0-9]*\)8+\([0-9]*\)4)#(\1+\2)c2#g
t start
s#(\([0-9]*\)8+\([0-9]*\)5)#(\1+\2)c3#g
t start
s#(\([0-9]*\)8+\([0-9]*\)6)#(\1+\2)c4#g
t start
s#(\([0-9]*\)8+\([0-9]*\)7)#(\1+\2)c5#g
t start
s#(\([0-9]*\)8+\([0-9]*\)8)#(\1+\2)c6#g
t start
s#(\([0-9]*\)8+\([0-9]*\)9)#(\1+\2)c7#g
t start
s#(\([0-9]*\)9+\([0-9]*\)0)#(\1+\2)9#g
t start
s#(\([0-9]*\)9+\([0-9]*\)1)#(\1+\2)c0#g
t start
s#(\([0-9]*\)9+\([0-9]*\)2)#(\1+\2)c1#g
t start
s#(\([0-9]*\)9+\([0-9]*\)3)#(\1+\2)c2#g
t start
s#(\([0-9]*\)9+\([0-9]*\)4)#(\1+\2)c3#g
t start
s#(\([0-9]*\)9+\([0-9]*\)5)#(\1+\2)c4#g
t start
s#(\([0-9]*\)9+\([0-9]*\)6)#(\1+\2)c5#g
t start
s#(\([0-9]*\)9+\([0-9]*\)7)#(\1+\2)c6#g
t start
s#(\([0-9]*\)9+\([0-9]*\)8)#(\1+\2)c7#g
t start
s#(\([0-9]*\)9+\([0-9]*\)9)#(\1+\2)c8#g
t start

:main
N
/\n0\+$/ {
  b end
}
s/\n/+/g
s/^.*$/(&)/g
b start

:end
s/\n.*$//g
s/^\([0-9]\{,10\}\).*$/\1/
p