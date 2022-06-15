# Electron-electron Greens Function Feynman Diagrams

In the interaction picture, imposing a one-particle greens function for times a and b, expanding out and applying Wicks theorem, an expression can be obtained for the full greens function of the interaction. This full greens function depends on the correction 'n' and contains n! diagrams constituting the full greens function.

From this expression this code generates all possible diagrams for the given correction, removes all fully and partially disconnected diagrams, then reduces them into their topologically inequivalent forms, following the (2^n)*n! relation for number of topologically inequivalent diagrams.

Given these topologically inequivalent connected diagrams, Feynman diagrams are then graphically generated, enabling us to see the Hartree terms and therefore the self-energies of the given diagrams.

WARNING: given the relationship between the correction and number of diagrams generated is (2n+1)!, increasing increments of n take longer to produces outputs.
