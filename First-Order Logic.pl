% Facts
parent(john, mary).
parent(jane, mary).
parent(mary, alice).

% Rule: A grandparent is a parent of a parent
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Query Example
% grandparent(john, alice). % This would return true, as John is a grandparent of Alice.
