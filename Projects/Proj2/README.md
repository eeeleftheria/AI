
*Q1: Reflex Agent*
The evaluation function is based on these basic features of a state:
 - distance from food pellets
 - distance from ghosts
 - distance from power capsules
 - scared times of ghosts (time where pacman can chase them)
 - stopping time

As suggested in the project, Ι calculate the reciprocates of the above
values and return their sum as the value of the evaluation function for the
specific successive state. Specifically, since we need low distances to
food to mean better states, the 1/distance is higher and thus preferable
than 1/dist' where dist is greater. Similarly, the distances from the
ghosts should have a negative weight, since the closer a ghost is to pacman
the more danger it is in. The power capsules are taken into consideration
the same way as food pellets, but with slightly lower weights since they
are not that important to eat as food pellets. The basic idea for these
three features is that we calculate the manhattan distance to each food
capsule/ghost from the state where pacman can go taking the action given.
After that, we keep the minimum distance for each type and depending on how
close or not it is to pacman we give the appropriate weight. If it is
within 0 distance, it means than the next state has a food/capsule/ghost
which is the best or worst case respectively.

The stopping penalty is enforced if the action is 'STOP'.

When the ghosts are "scared", meaning pacman can chase and eat them, the
reciprocal of the ghosts are multiplied by -3 so they have a positive
effect in the end, since this situation is preferable.

Finallly, the result also takes into consideration the score of the
successor state of pacman through successorGameState.getScore(), so all of
the eaten food, capsules and additional data has also an effect on which
successor state will be chosen.

*Q2: Minimax*
Consits of five helpers function:
 - terminalTest: checks if the given state is a terminal state or the
    maximum depth has been reached.

 - getUtility: returns the value of the evaluation function for the state.

 - minimaxDecision: calls the maxValue() method for agent 0 = pacman
    and returns a tuple (value, action) which corresponds to the best action
    that can be taken my pacman.

 - maxValue: checks if the state is terminal, if not it initializes a value 
    to -infinity and for each successive state of pacman for a legal action
    a it calculates recursively its minValue for the first ghost with
    agent index 1. Finally, it stores the best value and its corresponding
    action and returns it.

 - minValue: it checks if it is a terminal state, if not for each legal
    action a ghost can make, it gets the successive state and continues
    with finding the minimum value recursively. If the current ghost is the 
    last one, then the next action is taken by pacman so maxValue is called.
    In this case, depth is incremented by one, since pacman and all ghosts
    have finished playing this round.
    If, there are more ghosts left, it calculates the minimum value of all
    results of the next ghost's turn calling minValue with agentIndex
    incremented by one.


*Q3:*

*Q4:*

*Q5:*

