/* Predicado extensional*/
padre(juancarlos,felipe).
padre(juancarlos,cristina).
padre(juancarlos,elena).
padre(felipe,leonor).
padre(felipe,sofia).


madre(sofia,felipe).
madre(sofia,cristina).
madre(sofia,elena).
madre(letizia,leonor).
madre(letizia,sofia).
madre(paloma,letizia).



nacio(juancarlos, f(5,1,1938)).
nacio(felipe, f(30,1,1968)).
nacio(sofia, f(2,11,1938)).
nacio(letizia, f(15,9,1972)).


mujer(leonor). mujer(cristina). mujer(elena). mujer(cristina).

% Predicado intensional 
mujer(X) :- madre(X,_).
hermana(X,Y) :- progenitor(Z,X) , progenitor(Z,Y), mujer(X), X \= Y.
% Abuela 
abuela(X,Z) :- madre(X,Y), progenitor(Y,Z).
% Progenitor usando OR 
progenitor(X,Y) :- padre(X,Y) ;  madre(X,Y).





% Regla recursiva
antepasado(X,Y) :- progenitor(X,Y).
antepasado(X,Z) :- progenitor(X,Y), antepasado(Y,Z).



% 2
%antepasado(X,Z) :- progenitor(Y,Z), antepasado(X,Y).

