#test script to reduce integer dimension

Usage:
-run it one of the following: 1-command line, 2-ipython or jupyter
	e.g: run digit_simplicity.py -arg 1 -arg 2
-Argument definitions:
	arg 1: Required, Multiple-digit integer entry to be lowered
	arg 2: Optional, to visualize the iterations and final product /
			 any entry will be true

Example:
run digits_implicity.py 77 tr
entered number is  77
Final product is  8
Number of iteration is  4

[preview an example](https://cloud.githubusercontent.com/assets/10050249/22581983/c2238a8e-e998-11e6-839e-6de666070ad3.png)


Error checksums:
	1-Has to be an integer entry:
	2-Integer must require min 2 digits, but more is optional
	3-Whenever product comes '0', cycle is terminated as a final product!

