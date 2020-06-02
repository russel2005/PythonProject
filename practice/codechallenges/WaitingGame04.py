"""
your garget time is 4 seconds.
press enter to begin
press enter again after 4 seconds
Elapsed time: 4.213 seconds, 0.213 seconds to slow
"""

import time
import random

def waiting_game():
    target = random.randint(2,4) # target seconds to wait
    print('\nYour target time is {} seconds'.format(target))

    input(' ---Press Enter to Begin...')
    start = time.perf_counter()

    input('\n...Press Enter again after {} seconds'.format(target))
    elapsed = time.perf_counter() - start

    print('\nElapse time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('Unbelievable! Perfect timing!!!')
    elif elapsed < target:
        print('{0:.3f} seconds too fast'.format(target - elapsed))
    else:
        print('{0:.3f} seconds too fast'.format(elapsed - target))


waiting_game()
