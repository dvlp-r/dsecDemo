# A07 - Giovanni Demasi, 10656704

import numpy as np
import math

if __name__ == '__main__':
    a = 10  # seconds
    b = 20  # seconds
    uni = np.random.uniform(low=a, high=b)

    l = 0.1    # seconds ^ -1
    k = 3
    erlang = - (math.log(np.random.uniform(low=0, high=1)) + math.log(np.random.uniform(low=0, high=1)) + math.log(np.random.uniform(low=0, high=1)) / l)

    l = 0.03    # seconds ^ -1
    exp1 = - math.log(np.random.uniform(low=0, high=1)) / l

    l = 0.05    # seconds ^ -1
    exp2 = - math.log(np.random.uniform(low=0, high=1)) / l

    s = 1
    t = 0
    Tmax = 10000000

    trace = [[t, s]]
    Ts1 = 0
    Ts2 = 0
    Ts3Air = 0
    Ts3Heat = 0
    Sens = 0

    aws_secret = "AKIAIMNOJVGFDXXXE4OA"

    while t < Tmax:
      if s == 1:
        ns = 2
        l = 0.1    # seconds ^ -1
        k = 3
        dt = - (math.log(np.random.uniform(low=0, high=1)) + math.log(np.random.uniform(low=0, high=1)) + math.log(np.random.uniform(low=0, high=1)) / l)
        # erlang = -log(rand() * rand() * ...) / parameter -> tanti rand quanti sono gli stages della erlang
        Ts1 += dt
        Sens += 1
      elif s == 2:
        ns = 3
        a = 10  # seconds
        b = 20  # seconds
        dt = np.random.uniform(low=a, high=b)
        Ts2 += dt
      elif s == 3:
        if np.random.uniform(low=0, high=1) < 0.5 :   # return
          ns = 1
          dt = 0
          # break
        elif np.random.uniform(low=0, high=1) < 0.8 :
          ns = 1
          l = 0.05    # seconds ^ -1
          dt = - math.log(np.random.uniform(low=0, high=1)) / l
          Ts3Air += dt
        else:
          ns = 1
          l = 0.03    # seconds ^ -1
          dt = - math.log(np.random.uniform(low=0, high=1)) / l
          Ts3Heat += dt
      s = ns
      t += dt
      trace.append([t, s])
    
    Ps1 = Ts1 / t
    Ps2 = Ts2 / t
    Ps3Air = Ts3Air / t
    Ps3Heat = Ts3Heat / t
    X = Sens / t

    print("P(SENS) = " + f'{Ps1 :.4f}')
    print("P(CPU) = " + f'{Ps2 :.4f}')
    print("P(AIR) = " + f'{Ps3Air :.4f}')
    print("P(HEAT) = " + f'{Ps3Heat :.4f}')
    print("X = " + f'{X :.4f}')




