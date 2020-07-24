import numpy as np
import cv2  
from matplotlib import pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


darkorg = cv2.cvtColor(cv2.imread('dark.jpg'), cv2.COLOR_RGB2BGR)
dark = darkorg
hsv_dark = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

plt.subplot(1,2,1)
plt.imshow(darkorg)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

# h, s, v = cv2.split(hsv_dark)
# fig = plt.figure() 
# axis = fig.add_subplot(1, 1, 1, projection="3d")

# pixel_colors = dark.reshape((np.shape(dark)[0]*np.shape(dark)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()


# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show()

reddown = (115, 0, 0)
redup = (150, 255, 255)

mask = cv2.inRange(hsv_dark, reddown, redup)
result = cv2.bitwise_and(dark, dark, mask=mask)

dark -= result

result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
dark +=result

plt.subplot(1,2,2)
plt.imshow(dark)
plt.title('Modified Image')
plt.xticks([])
plt.yticks([])



plt.show()
cv2.destroyAllWindows()
