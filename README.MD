# HOW TO USE
 I wrote programs in python3, so you have to run by using python 3. I'm using this following command to run...
```
python3 example.py
```
## letterFrequencyAnalysis
This is letter frequency analysis program. Once you enter cipher text, it will show you letter frequency of that cipher text compare to letter frequency from Introduction to modern cryptography book and from website that I forgot to bookmark (if I found, I will update here).

First you have to enter your cipher text
```
Enter Cipher Text
    cat is funny
```
then it will show letter frequency like this
```
Ciphertext
    cat is funny

Decrypt Message 1
    ats in oheer

Decrypt Message 2
    ath ni oseer

sample     real1      real2              sample     real1      real2
n 20.00%   e 12.70%   e 12.60%           h  0.00%   m  2.40%   m  2.53% 
a 10.00%   t  9.00%   t  9.37%           j  0.00%   w  2.40%   w  2.34% 
c 10.00%   a  8.20%   a  8.34%           k  0.00%   f  2.20%   y  2.04% 
f 10.00%   o  7.50%   o  7.70%           l  0.00%   g  2.00%   f  2.03% 
i 10.00%   i  7.00%   n  6.80%           m  0.00%   x  2.00%   g  1.92% 
s 10.00%   n  6.70%   i  6.71%           o  0.00%   p  1.90%   p  1.66% 
t 10.00%   s  6.30%   h  6.11%           p  0.00%   b  1.50%   b  1.54% 
u 10.00%   h  6.10%   s  6.11%           q  0.00%   v  1.00%   v  1.06% 
y 10.00%   r  6.00%   r  5.68%           r  0.00%   k  0.80%   k  0.87% 
b  0.00%   d  4.20%   l  4.24%           v  0.00%   j  0.10%   j  0.23% 
d  0.00%   l  4.00%   d  4.14%           w  0.00%   q  0.10%   x  0.20% 
e  0.00%   c  2.80%   u  2.85%           x  0.00%   y  0.10%   q  0.09% 
g  0.00%   u  2.80%   c  2.73%           z  0.00%   z  0.10%   z  0.06% 
```
as you can see if your ciphertext is plaintext, the decrypt message should exacly equals your input, i.e. your cipher text. For example it should be...
```
Ciphertext
    cat is funny

Decrypt Message 1
    cat is funny

Decrypt Message 2
    cat is funny
```
because the length of ciphertext isn't long enough. Now you can edit your decrypt message by typing command like this...
```
1a=c
-----------------------------------------------------------------------------
Ciphertext
    cat is funny

Decrypt Message 1
    cts in oheer

Decrypt Message 2
    cth ni oseer

sample     real1      real2              sample     real1      real2
n 20.00%   e 12.70%   e 12.60%           h  0.00%   m  2.40%   m  2.53% 
a 10.00%   t  9.00%   t  9.37%           j  0.00%   w  2.40%   w  2.34% 
c 10.00%   c  2.80%   c  2.73%           k  0.00%   f  2.20%   y  2.04% 
f 10.00%   o  7.50%   o  7.70%           l  0.00%   g  2.00%   f  2.03% 
i 10.00%   i  7.00%   n  6.80%           m  0.00%   x  2.00%   g  1.92% 
s 10.00%   n  6.70%   i  6.71%           o  0.00%   p  1.90%   p  1.66% 
t 10.00%   s  6.30%   h  6.11%           p  0.00%   b  1.50%   b  1.54% 
u 10.00%   h  6.10%   s  6.11%           q  0.00%   v  1.00%   v  1.06% 
y 10.00%   r  6.00%   r  5.68%           r  0.00%   k  0.80%   k  0.87% 
b  0.00%   d  4.20%   l  4.24%           v  0.00%   j  0.10%   j  0.23% 
d  0.00%   l  4.00%   d  4.14%           w  0.00%   q  0.10%   x  0.20% 
e  0.00%   a  8.20%   u  2.85%           x  0.00%   y  0.10%   q  0.09% 
g  0.00%   u  2.80%   a  8.34%           z  0.00%   z  0.10%   z  0.06% 
```
you will see that the letter 't' form decrypt message 1 changed to letter 'c', and also decrypt message 2. The '1' from '1a=c' means the decrypt message 1, and 'a=c' means change all letter 'a' to letter 'c'. so '1a=c' means change all letter 'a' form decrypt message 1 to letter 'c'. But you will notice that the decrypt message 2 is also affected. 

And if you type '2s=u', you will see this...
```
2s=u
-----------------------------------------------------------------------------
Ciphertext
    cat is funny

Decrypt Message 1
    cts in oueer

Decrypt Message 2
    cth ni oueer
```
and if you type 'q' or 'Q', the program will quit. Now you understand how this program work so you can try to enter different ciphertext and different command. Or you can study my code - that's not very clean because this is my first serious python program I wrote.
