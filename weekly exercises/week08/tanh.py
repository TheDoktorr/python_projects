#!/usr/bin/env python

# Example Python script that uses matplotlib to plot the tanh function.

# Note that there are lots of examples of clever things you can do and
# plots you can make with matplotlib at

#    https://matplotlib.org/stable/gallery/index.html

# Here I focus on doing a good job of making basic plots.

# Useful "cheatsheets" for Matplotlib can be found at

#    https://matplotlib.org/cheatsheets/

# Personally I (Neil) can remember almost none of the options for
# styles, sizes, colours etc., and I have to rely on things like these
# cheatsheets.  When creating a new figure I always copy an old one
# and adapt it, rather than starting from scratch.

import matplotlib.pyplot as plt
import numpy as np

# In many undergraduate reports, first-draft PhD theses and even
# manuscripts submitted to journals, the axis labels are microscopic.
# In some cases figures appear pixelated.

# *** You must ensure that your axis labels etc. are readable in your
# report. ***

# The easiest way to do this is to ensure that your figure size is set
# correctly.

# The problem is that the default matplotlib figure size is 6.4" x
# 4.8" (c.f., portrait-orientation A4 paper is 8.3" x 11.7"); if you
# use, say, a 10-point font (the default) in this figure and then
# scale the figure down to typical publication size when you include
# the figure in your report document, the resulting text is miniscule.

# The figure size is specified in inches (").  A plausible size for a
# figure in a report is 3.5" x 2.6".  A plausible number of dots per
# inch (dpi; controls the resolution of the figure) is 200.  If you
# want to save the image in a bitmap format, such as JPEG, for
# subsequent printing or blowing up in a presentation then you will
# probably want a much higher resolution, such as dpi=600.  However, I
# strongly recommend saving the figure in a vector graphics format
# such as PDF or EPS for inclusion in a LaTeX document, in which case
# the dpi value does not matter.

# The suggested figure size also makes figures that are appropriate
# for use in presentations.

# Create a figure object of size 3.5" x 2.6" with a resolution of 200
# dpi.
fig=plt.figure(figsize=(3.5,2.6),dpi=200)

# Add subplot 1 of a 1x1 array of plots.
ax=fig.add_subplot(1,1,1)

# Use np.arange to create a NumPy array of values from -6.0 to 6.0,
# with the spacing of the points being 0.01.  If you wanted to create
# an array of values from -6.0 to 6.0 with the length of the array
# being 1000 then you could use xx=np.linspace(-6.0,6.0,1000).  Note
# that there is not usually any point in making lineplots with more
# than a thousand points, unless you are going to zoom in.
xx=np.arange(-6.0,6.0,0.01)      

# NumPy functions are "elemental" functions, meaning that you can give
# a function an array as an argument, and the function will be applied
# element-wise to the array.  Hence np.tanh(xx) is an array containing
# hyperbolic tangent values, corresponding to xx.
yy=np.tanh(xx)

# Plot yy against xx.  Colour: red.  Line-style: solid line.
# Label: uses TeX commands.  Use a raw string (r"whatever") to avoid problems
# with backslashes in TeX commands.
ax.plot(xx,yy,c='r',ls="-",label=r"$y=\tanh(x)$")   # or no raw string, label="$y= \\tanh(x)$"

# Add a second line to the plot.  Avoid relying on distinctions
# between red and green: this is the most common colour-blindness.
yy=np.tanh(2.0*xx)
ax.plot(xx,yy,c='b',ls=":",label=r"$y=\tanh(2x)$")

# Load some data from a text file holding three columns: x data, y
# data and error bars on the y data.  Plot the data as points with
# error bars, but without lines joining the points.  Need to specify
# capsize since, by default, the caps on error bars aren't shown.

xx,yy,err_yy=np.loadtxt("/home/andrew/git/python/python_projects/281/weekly exercises/week08/example_data.dat",unpack=True)
ax.errorbar(xx,yy,err_yy,label="Example data",ls="",marker="o",c="k",capsize=3)

# Axes always need labels.  If plotting physical quantities then you
# should always give the correct units.  If you want your axis labels,
# etc., to look more professional, use TeX math mode for mathematical
# symbols.
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

# Add a legend (labelling which curve is which).  Override the default
# font size, so the legend fits on the graph (but is still just about
# big enough to read).  Font size is specified in "points" (1/72th of
# an inch).  In general the font size should be 10-12 point.
ax.legend(fontsize=8)

# Adjust the padding around subplots.
fig.tight_layout()

# Show the plot in an interactive manner.
#plt.show()

# Write out the plot as a PDF file, which you can incorporate into a
# TeX document using \includegraphics.
fig.savefig("tanh.pdf",transparent=True)
plt.show()

# Finally close the plot.
# plt.close()
