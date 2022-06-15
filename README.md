# Electron-electron Greens Function Feynman Diagrams

In the interaction picture of an electron-electron Hamiltonian. Imposing a one-particle greens function for times a and b, then expanding out and applying Wicks theorem. An expression can be obtained for the full greens function of the interaction in terms of combinations of operators. This full greens function depends on the correction 'n' and contains (2n+1)! diagrams, which summised depending on amount of loops in the diagram, constitute the full greens function.

From this expression, this code generates all possible diagrams for any given correction. Removes all fully and partially disconnected diagrams. Then reduces them into their topologically inequivalent forms.

Given these topologically inequivalent connected diagrams, Feynman diagrams are then graphically generated, enabling us to see the Hartree terms and therefore the individual distinct self-energy contributions for said diagram.

WARNING: given the relationship between the correction and number of diagrams generated is (2n+1)!, increasing increments of n take longer to produce outputs.
