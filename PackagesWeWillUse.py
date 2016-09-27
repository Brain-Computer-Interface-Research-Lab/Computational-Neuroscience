'''The packages we'll be using along the way
Since we will also be using the numpy package to help us with some of the math and the matplotlib package to help us visualize our results, we also recommend going through this numpy tutorial, as well as this plotting tutorial. A couple of notes about Python, numpy, and matplotlib: It is customary to import numpy as matplotlib in the following way at the beginning of each script (note: this is not how it's done in the numpy tutorial)'''


import numpy as np
import matplotlib.pyplot as plt


'''References to functions and objects within numpy and matplotlib's pyplot can then be made by prepending "np." or "plt." to your command. For example, you could make an array containing [1, -1, 2, -2, 3] and then plot it in the following way:'''


x = np.array([1, -1, 2, -2, 3])

plt.plot(x)
plt.show()



''' One other thing that messes up beginners trying to use Python to do mathematics is integer division. For example, when using the interpreter you might see the following result'''

>>> 3/5
0


'''This can be corrected by specifying that either 3 or 5 is a floating point number by appending a decimal point to it:'''
>>> 3./5
0.6
>>> 3/5.
0.6


'''However, for our purposes the best way of correcting this problem is to import "division" from the __future__ module:'''
from __future__ import division
>>> 3/5
0.6

'''This way all division will be treated as floating point division, and you won't have to worry about anything accidentally getting rounded to the nearest integer. You won't have to worry about this if you're using Python 3, as Python 3 is the future we're importing division from. In summary, if you're new to scientific Python, we highly recommend inserting following three lines at the beginning of each of your scripts:'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


'''Opening data files using the pickle module: Oftentimes data is stored using the pickle format. Data can be stored in or loaded from this format using the pickle module in the following way:'''

import pickle

# create dictionary containing all your data
data = {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}
# save data in pickle format
with open('my_data.pickle', 'w') as f:
    pickle.dump(data, f)

# open data from file
with open('my_data.pickle', 'rb') as f:
    new_data_variable = pickle.load(f)

# now new_data_variable is equal to the dict {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}
