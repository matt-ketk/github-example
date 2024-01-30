import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def linear(x,b,m=0.7):
    y = m * x + b
    return y

x = np.linspace(0,10,100)
y = np.empty(0)
fig, ax = plt.subplots()

for i in range(5):
    y = linear(x,-4+i)
    ax.plot(x,y)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('5 lines')

fig.savefig('figures/5_lines.png')
Image.open('figures/5_lines.png').show()
