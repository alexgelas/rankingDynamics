#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt

q11=0.7; # Probability choose item 1, when item 1 is ahead
q21=0.4; # Probability choose item 1, when item 2 is ahead
q01=0.55; # Probability choose item 1, when the two items are tied

q12=1-q11;
q22=1-q21;
q02=1-q01;

s_p=q12/q11;
s_m=q21/q22;
s1=q01*(1-s_p);
s2=q02*(1-s_m);
def proba1win(x):
    if x<=0:
        return s1/(s1+s2)*s_p**(-x);
    else:
        return 1-s2/(s1+s2)*s_m**x;

x=range(-10,10);
y=list(proba1win(z) for z in x);

fig, ax = plt.subplots()
ax.scatter(x, y)

ax.set(xlabel='Difference Item 1 vs Item 2', ylabel='Probability item 1 wins',
       title='Two items')
ax.grid()

plt.show()



