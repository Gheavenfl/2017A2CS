## Chapter 29 works
29.01
/*Facts*/
capitalcity(paris) .
capitalCity (berlin).
capitalCity(cairo).

29.02
Already tested

29.03
male(yyk).
male(jake).
male(chen).

female(mary).
female(elisabeth).
female(lina).

parent(mary,yyk).
parent(yyk,jake).
parent(yyk,elisabeth).
parent(lina,jake).
parent(elizebeth,chen).

29.04
father(X,Y):-
    parent(X,Y),
    male(X).


ancestor(A, jack):- parent(A,B).
    parent(A,X),
    ancestor(X,B).

29.05
factorial(O, 1).
factorial (N, Result):-
    M is N - 1,
    factorial (M, PartResult),
    Result is PartResult * N.

get a anser of 120

29.06

writeList ([]).
writeList([H|T):-
    write(H),
    nl,
    writeList(T).




























