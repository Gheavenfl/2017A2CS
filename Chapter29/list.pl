lastitem(X,[X]).
lastitem(X, [_|T]) :-
    lastitem(X, T).

lastoneitem(X,[X,_]).
lastoneitem(X,[_|T]):-
    lastoneitem(X,T).

kelement(X , [X|_], 1).
kelement(X , [_|T], Y) :-
    Z is Y-1,
    kelement(X,T,Z).

number(0,[]).
number(X,[_|T]):-
    number(L,T),
    X is L+1.

add1([],[]).
add1([A|B], [C|D]):-
    add1(B,D),
    C is A+1.

reverse([],[]).
reverse([H|A],[B|H]):-
    reverse([A],[B]).









































