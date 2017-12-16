# Chapter 25 EOF Questions

1(a). Iteration uses a loop inside the function, recursion does not use any loop. Recursion function contains a base case. Recursion calls itself again and again until the base case is reached.

 (b). advantage: we do not need any loop in our code. disadvantage: it may take a lot of storage space.

2(a) A function which would call itself while running.

(b) 

Call Number | Procedure Call | Exponent=0 | Return
--- | --- | --- | ---
1 | *X(2,4)* | *False* | |
2 | *X(2,3)* | *False* | |
3 | *X(2,2)* | *False* | |
4 | *X(2,1)* | *False* | |
5 | *X(2,0)* | *True* | 1 |
(4) | *X(2,1)* | *False* | 2 |
(3) | *X(2,2)* | *False* | 4 |
(2) | *X(2,3)* | *False* | 8 |
(1) | *X(2,4)* | *False* | 16 |


(c) To store all the values from the recursive steps

pseudocode
FUNCTION Power(Base: INTEGER, Exponent: INTEGER) RETURNS INTEGER
	a=1
	WHILE Exponent <> 0
		a=a*Base
		Exponent=Exponent-1
	ENDWHILE

f(1) Because it uses less storage space.
 
 (2) Because it uses the same function.



3.(1) Line 02 to 04 is the base case.
  (2) Line 05 to 06 is the general case.

(b)

Call Number | Procedure Call | Exponent=0 | Return
--- | --- | --- | ---
1 | Fibonacci(4) | *False* | |
2 | Fibonacci(3) | *False* | |
3 | Fibonacci(2) | *False* | |
4 | Fibonacci(2) | *False* | |
5 | Fibonacci(1) | *True* | 1 |
6 | Fibonacci(1) | *True* | 1 |
7 | Fibonacci(0) | *True* | 1 |
8 | Fibonacci(1) | *True* | 1 |
9 | Fibonacci(0) | *True* | 1 | 
(4) | Fibonacci(2) | *False* | 1 |
(3) | Fibonacci(3) | *False* | 2 |
(2) | Fibonacci(2) | *False* | 1 |
(1) | Fibonacci(4) | *False* | 3 |



		



