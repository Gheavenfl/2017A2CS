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


grandson(X,Y):-
    parent(Z,Y),
    parent(X,Z),
    male(Y)

granddaughter(X,Y):-
    parent(Z,Y),
    parent(X,Z),
    female(Y)

married(X,Y):-
    parent(X,Z),
    parent(Y,Z)

sibling(X,Y):-
    parent(Z,X),
    parent(Z,Y)





