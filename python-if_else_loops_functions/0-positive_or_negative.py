#!/usr/bin/python2

import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("{} is zero".format(number))

=======
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
>>>>>>> a801146067a7c75ec613bf17b8d36d75837984aa
