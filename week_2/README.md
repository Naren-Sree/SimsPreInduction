Question 1. Why does the swap grid start as a copy of the current state, rather than being
filled with zeros? What would happen to a grain that does not move if G′ started empty?

Because most cells don't move on a given frame, only sand/water that has somewhere to go actually changes but not the ones that have already settled down. If G′ started empty, every cell that didn't move would just vanish.So starting empty would basically erase the whole grid every frame except for the few cells that moved.
This would result in all the grains which settle down to vanish in the next frame.

Q2: Fixed left-to-right order instead of random — what happens to the pile?

The pile stops being symmetric and leans to one side and since the question asked for ltr, the pile of sand starts towards the right. This happens because whenever a sand grain has both diagonals free, it's supposed to pick one randomly, but with a fixed scan order, the column that gets processed first always goes to its preset diagonal before the other columns even get checked. So, instead of a symmetric triangular pile we get a lopsided one that slopes off to the right side.

I tried doing the extar challenges as well but i could only  do rock due to the time constraint.
Rock was the easiest one since there was literally no physics attatched to it, we just needed to define it.
