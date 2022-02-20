import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

# Load picture, convert to grayscale and detect edges
SlikaRGB = data.coffee()
SlikaGrayScale = color.rgb2gray(SlikaRGB)
Rubovi = canny(SlikaGrayScale, sigma=2.0,
              low_threshold=0.55, high_threshold=0.8)

# Perform a Hough Transform
# The accuracy corresponds to the bin size of a major axis.
# The value is chosen in order to get a single high accumulator.
# The threshold eliminates low accumulators
rezultat = hough_ellipse(Rubovi, accuracy=20, threshold=250,
                       min_size=100, max_size=120)
rezultat.sort(order='accumulator')

# Estimated parameters for the ellipse
best = list(rezultat[-1])
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

# Draw the ellipse on the original image
cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
SlikaRGB[cy, cx] = (0, 120, 120)
# Draw the edge (white) and the resulting ellipse (red)
Rubovi = color.gray2rgb(img_as_ubyte(Rubovi))
Rubovi[cy, cx] = (250, 0, 0)

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                sharex=True, sharey=True)
ax1.set_title('Izvorna slika')
ax1.imshow(SlikaRGB)
ax2.set_title('Rub (bijela) i rezultat (crvena)')
ax2.imshow(Rubovi)
plt.show()