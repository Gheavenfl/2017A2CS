# Chapter 28 EOF



1.a To run AND two binary things together .

b #AND 00001111

c
IN
AND Mask
LSL #4
STO R
IN
AND Mask
OR R
STO R
END

2.
LDR #0
LOOP: IN
STO  STRING
INC   IX
CMP #33
JPN  Loop
END





