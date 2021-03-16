# Grid World program for the Markov Decision Process

Grid  World  is  a  2D  rectangular  grid  of  size  Ny,  Nx  (in  our  case,  Nx=6  and  Ny=6grid) with an agent starting off at one grid square. The agent will take actions in theform of directional steps (up, down, left, or right) to move to an adjacent grid squarewithin the environment of the rectangular grid

Referring to the diagram above, there are 4 types of grid squares:1)  Green  square:  Landing  on  this  square  results  in  the  agent  receiving  a  posi-tive 1 reward2) Brown Square: Landing on this square results in the agent receiving a negative 1reward3) White Square: Landing on this square has no effect on the agent in terms of rewardand4) Gray Square/Wall: This square serves as an obstacle - the agent cannot move intothis grid square
