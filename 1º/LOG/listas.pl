% LISTAS


% CASO BASE
miembro(X, [X|_]).


miembro(X, [Y|Cola]) :- miembro(X,Cola), Y\=X.



anexa([], L, L1).

anexa([X|L], L2, [X|L3]) :- anexa(L1,L2,L3).

% -----------------

busca(X,A,P) :-

append([P|_], [U], L). % Primero y ultimo
append([U|L], [P], L2 ).
append(_, [ A, X , Z|_], L2).


%-------------------