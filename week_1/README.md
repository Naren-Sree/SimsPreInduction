Question 1:

 This happens because the simulation updates positions in discrete time intervals, dt, rather than tracking continuous motion. If a ball is moving fast enough, it can completely leap across the boundary line within a single dt. When the position check happens at the next frame, the ball’s coordinates are already sitting outside the radius R, meaning the code never catches the exact moment it touched the wall.   The factors involved: This tunneling effect depends on dt (larger intervals mean bigger leaps), v (higher speed covers more distance per step), r(ball radius), and R(arena radius). The gravitational acceleration g also plays an indirect role because it continuously accelerates the ball, increasing its velocity over time.
 
Question 2:

 Even tho the restitution is at 1, meaning that no energy is lost during a bounce, I noticed that peak height slowly rose by a very bit over hundreds of bounces. 
 
i googled about this and apparantly: 
This phantom energy is a side effect of Euler’s method. Because the simulation updates velocity first and then uses that new velocity to update the position within the same step, it assumes the ball travels at that faster speed for the entire duration of dt. This introduces a tiny bit of artificial energy into the system every single frame. Over thousands of steps, those microscopic errors compound, making the system act as if it's being gently pumped with extra energy from nowhere. 


I could do upto a total of 500 balls when i reduced the size of balls radius more and more but then the balls were too small.