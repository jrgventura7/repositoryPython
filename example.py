# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

def hello_world(abc):
    logger.info('starting skynet')
    skynet.init()
    # TODO Change this to logging framework before prod
    print(f'--> debug, skynet init vector is {skynet.iv}')
    return skynet.rule_forever()