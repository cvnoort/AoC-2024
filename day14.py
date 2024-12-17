#!/usr/bin/python3

class Robot:

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def teleport(self, pos:int, dim:int):
        """Move to opposite side rather than out of the space."""
        return pos - dim if pos >= dim else dim - abs(pos) if pos < 0 else pos

    def move_robot(self, width:int, height:int):
        """Move robot according to its velocity."""
        self.position = [self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1]]
        if self.position[0] not in range(width):
            self.position[0] = self.teleport(self.position[0], width)
        if self.position[1] not in range(height):
            self.position[1] = self.teleport(self.position[1], height)


# Get initial position and velocity for each robot.
with open("input.txt") as file: 

    robots = {}

    for l, line in enumerate(file):
        
        robot_name = "robot_" + str(l+1)
        pos = line.split()[0].strip("p=").split(",")
        vel = line.split()[1].strip("v=").split(",")

        robots[robot_name] = Robot([int(pos[0]),int(pos[1])], 
                                   [int(vel[0]),int(vel[1])])


# Move robots for 100 seconds in a space 101 tiles wide and 103 tiles tall.
for robot in robots:
    for sec in range(100):
        robots[robot].move_robot(101, 103)

# Determine the safety factor.
quadrant_1 = [robots[robot].position for robot in robots 
              if robots[robot].position[0] < 50 and robots[robot].position[1] < 51]
quadrant_2 = [robots[robot].position for robot in robots 
              if robots[robot].position[0] > 50 and robots[robot].position[1] < 51]
quadrant_3 = [robots[robot].position for robot in robots 
              if robots[robot].position[0] < 50 and robots[robot].position[1] > 51]
quadrant_4 = [robots[robot].position for robot in robots 
              if robots[robot].position[0] > 50 and robots[robot].position[1] > 51]

print("Safety factor after 100 seconds:", 
      len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4))
