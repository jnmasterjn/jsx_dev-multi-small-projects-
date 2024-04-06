plot(sin,0,2*pi)
curve(sin(x) + 1, from = 0, to = 10 * pi)

# Plot the sine function without the x-axis
curve(sin(x), from = 0, to = 10 * pi, xaxt = 'n')

# Define the positions and labels for the x-axis
x_ticks <- seq(0, 10 * pi, by = pi)
x_labels <- c('0', 'π', '2π', '3π', '4π', '5π', '6π', '7π', '8π', '9π', '10π')

# Add the custom x-axis
axis(side = 1, at = x_ticks, labels = x_labels)

