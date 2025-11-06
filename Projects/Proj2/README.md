
*Q1: Reflex Agent*
The evaluation function is based on these basic features of a state:
 - distance from food pellets
 - distance from ghosts
 - stopping time

As suggested in the project, Ι calculate the reciprocates of the above
values and return their sum as the value of the evaluation function for the
specific successive state. Specifically, since we need low distances to
food to mean better states, the 1/distance is higher and thus preferable
than 1/dist' where dist is greater. Similarly, the distances from the
ghosts should have a negative weight, since the closer a ghost is to pacman
the more danger it is in.  The basic idea for these two features is that 
we calculate the manhattan distance to each food/ghost from the state 
where pacman can go taking the action given.
After that, we keep the minimum distance for each type and depending on how
close or not it is to pacman we give the appropriate weight. If it is
within 0 distance, it means than the next state has a food/ghost
which is the best or worst case respectively.

The stopping penalty is enforced if the action is 'STOP'.

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
For the alpha-beta algorithm i followed the pseudocode of the website
and changed accordingly the code of minimax.


*Q4:*
The expectimax algorithm is entirely based on the minimax algorithm but
instead of having a minValue method, I use a chanceValue method which
assigns an equal probability to each possible action and calculates
its expected average utility. 

*Q5:*
Initially, Q1 and Q5 were implemented the same way as I had used extra features
in the evaluation function of the Reflex agent, but I later simplified it.
Since, it evaluates states instead of actions, this evaluation function
tracks also two extra features that are essential for the evaluation of
the whole state and not just the action.

 - distance from power capsules
 - scared times of ghosts (time where pacman can chase them)

The power capsules are taken into consideration the same way as food pellets, 
but with slightly lower weights since they are not that important to eat as 
food pellets. They are important, since they award pacman with greater score
and give him the opportunity to chase the ghosts.

When the ghosts are "scared", meaning pacman can chase and eat them, the
reciprocal of the ghosts is multiplied by -3 so they have a positive
effect in the end, since this situation is preferable. As mentioned before, 
it can offer extra score for pacman and even some "safe" time to eat food pellets
and even ghosts without being in danger.


