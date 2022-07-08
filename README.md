# Electron-electron Greens function Feynman diagrams

Given the case of an electron-electron interaction in the interaction picture of a one-particle greens function. On application of Wicks theorem, an expression for the full greens function of the system can be found. This expression consists of interactions, vertexes and g-naughts. When these components are put together and determinant for the g's are found, a linear combination of Feynman diagrams can be created. These obtained Feynman diagrams can then be summated, leading to the resultant full greens function.

This code sets out to generate all of these diagrams for any given order of correction. i.e. for any n amount of interactions (for which there are (2n+1)! possible diagrams). From here there are rules on connected diagrams and topologically inequivalent diagrams, which widdle the number of diagrams of each type to (2^n)*n!. Given all of these topologically inequivalent diagrams, the code then graphically generates these in the form of Feynman diagrams. 

After the topologically inequivilent connected diagrams are obtained, the self-energy can be found. This is done through the removal of all Hartree and Fock terms. Once the then resultant self-energy diagrams are generated, full green's function self-energy diagrams can be found. This time, through a more rigorous removal of disconnected Hartree and Fock terms. This leaves the fundamental self-energy diagrams with all possible insertions over the full greens functions.

WARNING: given the relationship between the correction and number of diagrams generated is (2n+1)!, increasing increments of n take longer to produce outputs.
