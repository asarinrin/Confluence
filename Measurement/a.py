# %matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from PIL import Image
from matplotlib import gridspec

png_dat = []

for i in range(10):
    # 画像ファイル名(パス)
    file_name = './png/sin_{}.png'.format(i)
    img = Image.open(file_name)
    img = img.resize((1100,500))
    png_dat.append(np.asarray(img))

img = png_dat[9]
img2 = png_dat[1]

npng = 1
nrows = 3
ncols = 3

slider_start_position = 0

fig = plt.figure(figsize=(12, 10))
gs = fig.add_gridspec(5, 3)
ax1 = fig.add_subplot(gs[0:2, 0:2])
ax1.imshow(img, interpolation='None')
ax1.axis("off")

vertical = []

for i in range(nrows):
    for j in range(ncols):
        t = np.arange(0.0, 10.0, 0.001)
        s = np.sin(2*np.pi*t)
        ax = fig.add_subplot(gs[npng+i+1, j])
        ax.plot(t,s,lw=2,color='red')
        vertical.append(ax.axvline(x=slider_start_position))
        ax.axis([0, 10, -3, 3])
        ax.set_title("yeah")
        fig.canvas.draw_idle()

axcolor = 'lightgoldenrodyellow'
axslider = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(axslider, 'time', 0.0, 10.0, valinit=slider_start_position)

plt.subplots_adjust(bottom=0.2)
plt.subplots_adjust(wspace=0.4, hspace=1)


def update(val):
    slider_value = slider.val
    idx = int(slider_value)
    img = png_dat[idx]
    ax1.imshow(img, interpolation='None')
    for i in range(ncols*(nrows+npng)): vertical[i].set_xdata(slider_value)
    fig.canvas.draw_idle()
slider.on_changed(update)

resetax = plt.axes([0.45, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    slider.reset()
button.on_clicked(reset)

# rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
# radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


# # def colorfunc(label):
# #     l.set_color(label)
# #     fig.canvas.draw_idle()
# # radio.on_clicked(colorfunc)

plt.show()