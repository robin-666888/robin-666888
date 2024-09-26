import matplotlib.pyplot as plt
import numpy as np

def draw_circle(ax, center, radius, color, edgecolor='black'):
    """Draw a filled circle on the given axes."""
    circle = plt.Circle(center, radius, color=color, ec=edgecolor)
    ax.add_artist(circle)

def draw_cat():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Cat Body
    draw_circle(ax, (0.5, 0.4), 0.25, 'lightgray')  # Body
    draw_circle(ax, (0.5, 0.6), 0.2, 'gray')       # Head

    # Ears
    ear_left = np.array([[0.35, 0.7], [0.4, 0.9], [0.5, 0.7]])
    ear_right = np.array([[0.65, 0.7], [0.6, 0.9], [0.5, 0.7]])
    ax.add_patch(plt.Polygon(ear_left, color='lightgray', ec='black'))  # Left ear
    ax.add_patch(plt.Polygon(ear_right, color='lightgray', ec='black'))  # Right ear

    # Inner Ears
    inner_ear_left = np.array([[0.4, 0.75], [0.45, 0.85], [0.5, 0.75]])
    inner_ear_right = np.array([[0.6, 0.75], [0.55, 0.85], [0.5, 0.75]])
    ax.add_patch(plt.Polygon(inner_ear_left, color='pink', ec='black'))  # Inner Left ear
    ax.add_patch(plt.Polygon(inner_ear_right, color='pink', ec='black'))  # Inner Right ear

    # Eyes
    draw_circle(ax, (0.45, 0.65), 0.05, 'white')  # Left eye
    draw_circle(ax, (0.55, 0.65), 0.05, 'white')  # Right eye
    draw_circle(ax, (0.45, 0.65), 0.025, 'black')  # Left pupil
    draw_circle(ax, (0.55, 0.65), 0.025, 'black')  # Right pupil

    # Nose
    draw_circle(ax, (0.5, 0.58), 0.025, 'pink')

    # Mouth
    ax.plot([0.5, 0.5], [0.56, 0.54], color='black', linewidth=2)  # Middle line of mouth
    ax.plot([0.5, 0.48], [0.54, 0.52], color='black', linewidth=2)  # Left side of mouth
    ax.plot([0.5, 0.52], [0.54, 0.52], color='black', linewidth=2)  # Right side of mouth

    # Whiskers
    ax.plot([0.35, 0.48], [0.55, 0.55], color='black', linewidth=2)  # Left whisker
    ax.plot([0.35, 0.48], [0.53, 0.53], color='black', linewidth=2)  # Left whisker top
    ax.plot([0.35, 0.48], [0.57, 0.57], color='black', linewidth=2)  # Left whisker bottom

    ax.plot([0.52, 0.65], [0.55, 0.55], color='black', linewidth=2)  # Right whisker
    ax.plot([0.52, 0.65], [0.53, 0.53], color='black', linewidth=2)  # Right whisker top
    ax.plot([0.52, 0.65], [0.57, 0.57], color='black', linewidth=2)  # Right whisker bottom

    # Legs
    ax.add_patch(plt.Rectangle((0.35, 0.2), 0.1, 0.25, color='lightgray', ec='black'))  # Left front leg
    ax.add_patch(plt.Rectangle((0.55, 0.2), 0.1, 0.25, color='lightgray', ec='black'))  # Right front leg
    ax.add_patch(plt.Rectangle((0.4, 0.1), 0.1, 0.2, color='lightgray', ec='black'))  # Left back leg
    ax.add_patch(plt.Rectangle((0.5, 0.1), 0.1, 0.2, color='lightgray', ec='black'))  # Right back leg

    # Cat Tail
    tail_x = [0.3, 0.2, 0.15, 0.15, 0.3]
    tail_y = [0.45, 0.55, 0.65, 0.7, 0.6]
    ax.plot(tail_x, tail_y, color='gray', linewidth=10, linestyle='-', marker='o')

    # Setting the limits and aspect
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide the axes

    plt.title('Cute Detailed Cat Drawing')
    plt.show()

draw_cat()

