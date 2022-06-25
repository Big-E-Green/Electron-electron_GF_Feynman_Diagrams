# Electron-electron Greens function Feynman diagrams

Given the case of an electron-electron interaction in the interaction picture of a one-particle greens function. On application of Wicks theorem, an expression for the full greens function of the system can be found. This expression consists of interactions and g-naughts, which constitute the building blocks of Feynman diagrams. These obtained Feynman diagrams can then be summated, leading to the full greens function result.

This code sets out to generate all of these diagrams for any given order of correction. i.e. for any n amount of interactions (for which there are (2n+1)! possible diagrams). From here there are rules on connected diagrams and topologically inequivalent diagrams, which widdle the number of diagrams of each type to (2^n)*n!. Given all of these topologically inequivalent diagrams, the code then graphically generates these in the form of Feynman diagrams. 

Of note in terms of the physics behind these. Hartree terms can be discerned and hence self-energy contributions identified.

WARNING: given the relationship between the correction and number of diagrams generated is (2n+1)!, increasing increments of n take longer to produce outputs.
