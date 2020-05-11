import numpy
import copy
import math

def main():
    f = open('input.txt','r')
    global GridSize, Cars, Obstacles_total
    GridSize = int(f.readline().rstrip("\n"))
    Cars = int(f.readline().rstrip("\n"))
    Obstacles_total = int(f.readline().rstrip("\n"))
    Obstacle = []

    for i in range(Obstacles_total):
        Obstacle.append(f.readline().rstrip('\n'))

    CarInitial = []
    for i in range(Cars):
        CarInitial.append(f.readline().rstrip('\n'))

    CarDestination = []
    for i in range(Cars):
        CarDestination.append(f.readline().rstrip('\n'))

    State = []
    for i in range(GridSize):
        for j in range(GridSize):
            State.append(Coordinate(i,j))

    Actions = ['left', 'up', 'right', 'down']
    policies = numpy.full((Cars, GridSize, GridSize), 'right')
    l = 0

    for k in range(Cars):

        Reward, Utility, Updated_Utility, Policy, xg, yg = Initialize(Obstacle, CarDestination[k], State)

        while True:
            for i in range(len(State)):
                if State[i].x == xg and State[i].y == yg:
                    Updated_Utility[xg][yg] = numpy.float64(99.00)
                    continue
                Max_Utility = float('-inf')
                for j in range(len(Actions)):
                    x1, y1 = Go(State[i],Actions[j])
                    x2, y2 = Go(State[i], Move_Left(Actions[j]))
                    x3 , y3 = Go(State[i], Move_Right(Actions[j]))
                    x4, y4 = Go(State[i], Move_Opposite(Actions[j]))
                    Current_Utility = numpy.float64(0.7) * Utility[x1][y1] + numpy.float64(0.1) * Utility[x2][y2] + numpy.float64(0.1) * Utility[x3][y3] + numpy.float64(0.1) * Utility[x4][y4]
                    if Max_Utility == Current_Utility:
                        Policy[State[i].x][State[i].y] = Compare_Policy(Policy[State[i].x][State[i].y], Actions[j])
                    if Current_Utility > Max_Utility:
                        Max_Utility = Current_Utility
                        Policy[State[i].x][State[i].y] = Actions[j]

                Updated_Utility[State[i].x][State[i].y] = Reward[State[i].x][State[i].y] + numpy.float64(0.9) * Max_Utility
            maxDiff = numpy.float64(0)
            for i in range(len(State)):
                diff = abs(Updated_Utility[State[i].x][State[i].y] - Utility[State[i].x][State[i].y])
                if maxDiff < diff:
                    maxDiff = diff
            if maxDiff <= numpy.float64(0.1/9):
                break
            Utility = copy.deepcopy(Updated_Utility)
        policies[k] = Policy
    Reward[xg][yg] = numpy.float64(-1)

    o = open("output.txt", "w")

    for i in range(Cars):
        total_value = numpy.float64(0.00)
        for j in range(10):
            pos = CarInitial[i].split(",")
            x1 = pos[1]
            y1 = pos[0]
            pos = str(x1)+","+str(y1)
            numpy.random.seed(j)
            swerve = numpy.random.random_sample(1000000)
            k = 0
            end = CarDestination[i].split(",")
            x2 = end[1]
            y2 = end[0]
            end = str(x2) + "," + str(y2)
            if pos == end:
                total_value = numpy.float64(1000)
            value = numpy.float64(0.00)
            while pos != end:
                currentx = 0
                currenty = 0
                pos1 = pos.split(",")
                currentx = int(pos1[0])
                currenty = int(pos1[1])
                move = policies[i][currentx][currenty]
                if swerve[k] > numpy.float64(0.7):
                    if swerve[k] > numpy.float64(0.8):
                        if swerve[k] > numpy.float64(0.9):
                            move = Move_Opposite(move)
                        else:
                            move = Move_Right(move)
                    else:
                        move = Move_Left(move)
                newx, newy = Next_state(currentx, currenty, move)
                pos = str(newx) + "," + str(newy)
                value += Reward_func(newx, newy, x2, y2, Reward)
                k += 1
            total_value += value
            # print(total_value)
        o.write((str(math.floor(total_value/10))))
        o.write('\n')

    o.close()


def Next_state(currentx, currenty, Action):
    global GridSize
    if Action == 'left':
        if currenty - 1 < 0:
            return currentx, currenty
        else:
            return currentx, currenty - 1

    if Action == 'right':
        if currenty + 1 == GridSize:
            return currentx, currenty
        else:
            return currentx, currenty + 1

    if Action == 'up':
        if currentx - 1 < 0:
            return currentx, currenty
        else:
            return currentx - 1, currenty

    if Action == 'down':
        if currentx + 1 == GridSize:
            return currentx, currenty
        else:
            return currentx + 1, currenty

def Reward_func(newx, newy, endx, endy, Reward):
    if newx == int(endx) and newy == int(endy):
        return numpy.float64(99.00)
    else:
        return Reward[newx][newy]

def Go(State, Action):
    global GridSize
    if Action == 'left':
        if State.y - 1 < 0:
            return State.x, State.y
        else:
            return State.x, State.y - 1

    if Action == 'right':
        if State.y + 1 == GridSize:
            return State.x, State.y
        else:
            return State.x, State.y + 1

    if Action == 'up':
        if State.x - 1 < 0:
            return State.x, State.y
        else:
            return State.x - 1, State.y

    if Action == 'down':
        if State.x + 1 == GridSize:
            return State.x, State.y
        else:
            return State.x + 1, State.y


def Move_Left(Action):
    if Action == 'left':
        return 'down'
    if Action == 'down':
        return 'right'
    if Action == 'right':
        return 'up'
    if Action == 'up':
        return 'left'

def Move_Right(Action):
    if Action == 'left':
        return 'up'
    if Action == 'down':
        return 'left'
    if Action == 'right':
        return 'down'
    if Action == 'up':
        return 'right'

def Move_Opposite(Action):
    if Action == 'left':
        return 'right'
    if Action == 'down':
        return 'up'
    if Action == 'right':
        return 'left'
    if Action == 'up':
        return 'down'

def Compare_Policy(Action1, Action2):
    if Action1 == 'up' or Action2 == 'up':
        return 'up'
    elif Action1 == 'down' or Action2 == 'down':
        return 'down'
    elif Action1 == 'right' or Action2 == 'right':
        return 'right'
    elif Action1 == 'left' or Action2 == 'left':
        return 'left'

def Initialize(Obstacle, CarDestination, State):
    global GridSize, Obstacles_total
    Reward = numpy.full((GridSize, GridSize), numpy.float64(-1.00))
    Utility = numpy.full((GridSize, GridSize), numpy.float64(-1.00))
    Updated_Utility = numpy.full((GridSize, GridSize), numpy.float64(-1.00))
    Policy = numpy.full((GridSize, GridSize), 'right')

    for i in range(Obstacles_total):
        y = int(Obstacle[i].split(',')[0])
        x = int(Obstacle[i].split(',')[1])
        Reward[x][y] = numpy.float64(-101.00)

    y = int(CarDestination.split(',')[0])
    x = int(CarDestination.split(',')[1])
    Reward[x][y] = numpy.float64(99.00)
    Utility = Reward

    return Reward, Utility, Updated_Utility, Policy, x, y

class Coordinate(object):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    main()