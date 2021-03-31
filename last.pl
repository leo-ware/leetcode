% https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/

% whether X is the last element of a list Y
my_last(X, Y) :- [X|[]] = Y.
my_last(X, Y) :-
    [_|Z] = Y,
    my_last(X, Z).

% X is the second to last element of a list Y
second_last(X, Y) :- [X|[_]] = Y.
second_last(X, Y) :-
    [_|Z] = Y,
    second_last(X, Z).
