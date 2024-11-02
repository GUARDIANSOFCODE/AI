% Facts
isa(dog, animal).
isa(cat, animal).
has_property(animal, can_breathe).
has_property(dog, can_bark).
has_property(cat, can_meow).

% Rules for inheritance
inherits_property(X, Y) :- isa(X, Z), has_property(Z, Y).
inherits_property(X, Y) :- has_property(X, Y).

% Query Example
% inherits_property(dog, can_breathe). % This would return true because dog is an animal, and animals can breathe.
