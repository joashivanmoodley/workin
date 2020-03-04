'''
1. 754
2. O(1)
3. KISS - keep it simple stupid.
4. O(N)
'''
def nterm(n): 
    if n <2:  
        return 2
    else: 
    	return nterm(n-1)+nterm(n-2)
  
counter = 0
while counter > -1:
	print nterm(counter)
	counter += 1