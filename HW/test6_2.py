import numpy as np


class Solution(object):

    def	prob6_2(self,a,b,c):
        p	=	len(a)
        q	=	len(b)
        r	=	len(c)
        #Init
        Memo	=	np.zeros((p,q,r+1),dtype=bool)
        Memo[0][0][r]	=	True
        #base	case
        for	k	in	range(r - 1, - 1, - 1):
            for	i	in	range(p):
                for	j	in	range(q):
                    if	i	<	p - 1	and	j<	q- 1:
                        Memo[i][j][k]	=	(Memo[i+1][j][k+1]	and	(c[k]	==	a[i]))	or	(Memo[i][j+1][k+1]	and	c[k]==b[j])
                    if	i	==	p- 1	and	j<q - 1:
                        Memo[i][j][k]	=	(Memo[0][j][k+1]	and	(c[k]	==	a[i]))	or	(Memo[i][j+1][k+1]	and	c[k]==b[j])
                    if	i	<	p - 1	and	j	==	q - 1:
                        Memo[i][j][k]	=	(Memo[i+1][j][k+1]	and	(c[k]	==	a[i]))	or	(Memo[i][0][k+1]	and	c[k]==b[j])
                    if	i	==	p- 1	and	j	==	q - 1:
                        Memo[i][j][k]	=	(Memo[0][j][k+1]	and	(c[k]	==	a[i]))	or	(Memo[i][0][k+1]	and	c[k]==b[j])
        return	Memo[0][0][0]
solver	=	Solution()	
a	=	'111' 	
b	=	'100' 	
c	=	 '111010111001'	
print	solver.prob6_2(a,b,c)	