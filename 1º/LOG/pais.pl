frontera(es,fr). frontera(fr,es).
frontera(es,pt). frontera(pt,es).
frontera(fr,de). frontera(de,fr).
frontera(fr,it). frontera(it,fr).


frontera(ca,us). frontera(us,ca).
frontera(ca,mx). frontera(mx,ca).
frontera(us,mx). frontera(mx,us).


llegar(X,Y) :- frontera(X,Y).
llegar(X,Y) :- frontera(X,Z), llegar(Z,Y), X\=Y.