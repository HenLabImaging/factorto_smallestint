import sys
import math
import matplotlib.pyplot as plt
import numpy as np
#conditions for user entries to calculate single digit number from iterativeself-multiplications	

def mainf(user_,figs=False):
    try:
	num_digits = int(math.log10(user_))+1
	original_n=user_
	print "entered number is ", user_
	c=0
	while num_digits>1:
		#print "N of digits:", num_digits
		#print "number:", user_      #enter if you like to monitor each iteration
	
		if figs:
			plt.bar(c,user_,color='black')
		user_=self_fact(user_)
		if user_==0:
			print " 0 is detected "
			break
		else:
			num_digits=int(math.log10(user_))+1
			c+=1
			
	if figs:
		plt.bar(c,user_,color='r',alpha=0.75)
		plt.plot(np.ones(c+2)*10,'r--')
		plt.axis([0 ,c+0.5,num_digits,original_n+1])
		plt.xlabel('N Iterations')
		plt.ylabel('Value')
		plt.show()
	print "Final product is ", user_
	print "Number of iteration is ", c
    except:
        print "usage: Enter an integer"
        sys.exit(1)   # Error checksum for the entry	



def self_fact(var):
    str_num=str(var)
    prod=1
    for ii in str_num:
	prod*=int(ii)

    return prod

if __name__ == "__main__":
    user_num=int(sys.argv[1])
    try:
	    fig_entry=sys.argv[2]
	    mainf(user_num,True)
    except:
	    "No fig entered"
	    mainf(user_num)



