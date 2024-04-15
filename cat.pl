%prolog
likes(Ziggy,fish).
cat(Ziggy).
eats(X,Y):-cat(X),likes(X,Y).
