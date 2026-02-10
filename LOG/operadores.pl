:- op(800, xfx, <>).
:- op(690, xfy, v).
:- op(600, xfy, &).
:- op(500, fy, not).

% Define the rule as a fact using an atom, not a variable
not(A & B) <> (not A v not B).



eval(A,_,_,a,A).
eval(_,B,_,b,B).
eval(_,_,C,c,C).

eval(A,B,C, not K, 0)  :- eval(A,B,C, K, 1).
eval(A,B,C, not K, 1)  :- eval(A,B,C, K, 0).


% AND
eval(A,B,C, F & G, 0)  :- eval(A,B,C, G, 0); eval(A,B,C, F, 0).
eval(A,B,C, F & G, 1)  :- eval(A,B,C, F, 1), eval(A,B,C, G,1).

% OR
eval(A,B,C, F v G, 0)  :- eval(A,B,C, F, 0), eval(A,B,C, G,0).
eval(A,B,C, F v G, 1)  :- eval(A,B,C, F, 1); eval(A,B,C, G,1).


% Hacer el implica sin tabla de verdad