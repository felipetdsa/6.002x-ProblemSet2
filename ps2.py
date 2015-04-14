# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        #raise NotImplementedError
        assert type(width) == int and type(height) == int
        assert width > 0 and height > 0
        self.w = width
        self.h = height
        self.room = {}
        for i in xrange(self.w):
            for j in xrange(self.h):
                self.room[(i, j)] = 'dirty'
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #raise NotImplementedError
        self.posw = int(pos.getX())
        self.posh = int(pos.getY())
        self.room[(self.posw, self.posh)] = 'cleaned'
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #raise NotImplementedError
        return self.room[(m, n)] == 'cleaned'
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        #raise NotImplementedError
        return len(self.room)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        #raise NotImplementedError
        self.num_clear = 0
        for tile in self.room.keys():
            if self.room[tile] == 'cleaned':
                self.num_clear += 1
        return self.num_clear

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #raise NotImplementedError
        self.posx = float(random.choice(xrange(self.w)))
        self.posy = float(random.choice(xrange(self.h)))
        return Position(self.posx, self.posy)
        

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #raise NotImplementedError
        room_w = math.floor(pos.getX())
        room_h = math.floor(pos.getY())
        return self.room.has_key((room_w, room_h))
        


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        #raise NotImplementedError
        self.room = room
        self.i_pos = room.getRandomPosition()
        self.speed = speed
        self.angle = random.choice(xrange(0, 360))
        self.i_pos.getNewPosition(self.angle, self.speed)
        self.room.cleanTileAtPosition(self.i_pos)


    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        #raise NotImplementedError
        return self.i_pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        #raise NotImplementedError
        return self.angle

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        #raise NotImplementedError
        self.i_pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        #raise NotImplementedError
        self.angle = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        #new_pos = self.i_pos.getNewPosition(self.angle, self.speed)
        #old_pos = self.getRobotPosition()
        new_pos = self.i_pos.getNewPosition(self.angle, self.speed)
        #self.room.cleanTileAtPosition(new_pos)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)
        else:
            self.setRobotDirection(random.randint(0, 359))
            
#        if new_pos.getX() < 1 and new_pos.getY() < 1:
#            self.setRobotDirection(random.randint(0, 90))
#        elif int(new_pos.getX()) == self.room.w -1 and int(new_pos.getY()) == self.room.h -1:
#            self.setRobotDirection(random.randint(180, 270))
#        elif new_pos.getX() < 1 and int(new_pos.getY()) == self.room.h -1:
#            self.setRobotDirection(random.randint(90, 180))
#        elif new_pos.getY() < 1 and int(new_pos.getX()) == self.room.w -1:
#            self.setRobotDirection(random.randint(270, 360))
#
#        elif new_pos.getX() < 1 and new_pos.getY() > 1:
#            self.setRobotDirection(random.randint(0, 180))
#        elif new_pos.getY() < 1 and new_pos.getX() > 1:
#            self.setRobotDirection(random.choice([random.randint(270, 359), random.randint(0, 90)]))
#        elif int(new_pos.getX()) == self.room.w -1 and new_pos.getY() > 1:
#            self.setRobotDirection(random.randint(180, 360))
#        elif int(new_pos.getY()) == self.room.h -1 and new_pos.getX() > 1:
#            self.setRobotDirection(random.randint(90, 270))
            
        #or int(new_pos.getX()) == self.room.w - 1 or int(new_pos.getY()) == self.room.h - 1:
        #    self.setRobotDirection(random.randint(0, 359))
                #while self.room.getNumCleanedTiles() < self.room.getNumTiles():
        #    new_pos = self.i_pos.getNewPosition(self.angle, self.speed)
        #    self.room.cleanTileAtPosition(new_pos)
        #if self.getRobotPosition().getX == 0 or self.getRobotPosition().getX == self.room.w \
        #or self.getRobotPosition().getY == 0 or self.getRobotPosition().getY == self.room.h:
                #self.setRobotPosition(new_pos)
        #else:
        #    pass
        
        

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    #raise NotImplementedError
    avg = 0.
    trial = 0
    #robots_list = []
    #room = RectangularRoom(width, height)
    #for i in xrange(num_robots):
    #    robots_list.append(robot_type(room, speed))

    #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
    
    while trial < num_trials:
        robots_list = []
        room = RectangularRoom(width, height)
        for i in xrange(num_robots):
            robots_list.append(robot_type(room, speed))

        #anim = ps2_visualize.RobotVisualization(num_robots, width, height) #Uncomment for visualization
        clock_ticks = 0
        done = 0
        while done < min_coverage:
            #anim.update(room, robots_list) #Uncomment for visualization
            #print room.getNumCleanedTiles()
            #print room.getNumTiles()
            for robot in robots_list:
                robot.updatePositionAndClean()
                clock_ticks += 1
            done = float (room.getNumCleanedTiles()) / (room.getNumTiles())
            #print 'Done' + str(done)
        avg += clock_ticks // len(robots_list)
        trial += 1
        #anim.done() #Uncomment for visualization

    return (avg//num_trials)
        

# Uncomment this line to see how much your simulation takes on average
##print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        self.setRobotDirection(random.randint(0, 359))
        new_pos = self.i_pos.getNewPosition(self.angle, self.speed)
        #self.room.cleanTileAtPosition(new_pos)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(new_pos)
        else:
            self.setRobotDirection(random.randint(0, 359))


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
