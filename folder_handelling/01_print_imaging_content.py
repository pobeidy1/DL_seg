import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.gridspec import GridSpec
from PIL import Image

def display_images_in_grid(image_paths):
    num_images = len(image_paths)
    num_rows = (num_images + 3) // 4  # Calculate the number of rows needed for a 4x4 grid

    fig = plt.figure(figsize=(10, 10))
    gs = GridSpec(num_rows, 4)

    for i, image_path in enumerate(image_paths):
        ax = fig.add_subplot(gs[i // 4, i % 4])
        ax.axis('off')
        
        # Load and display the image using PIL
        img = Image.open(image_path)
        ax.imshow(img)
        ax.set_title(os.path.basename(image_path))

    # Adjust layout and show the figure
    gs.tight_layout(fig, h_pad=0.5, w_pad=0.5)
    plt.subplots_adjust(top=0.9)
    fig.suptitle(os.path.dirname(image_paths[0]), fontsize=14)
    plt.show()

def display_images_in_folders(root_path):
    for root, _, files in os.walk(root_path):
        image_paths = [os.path.join(root, file) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
        if image_paths:
            display_images_in_grid(image_paths[:min(len(image_paths), 10)])

if __name__ == "__main__":
    # Specify the root directory you want to start walking from
    root_directory = "your_root_directory_here"

    display_images_in_folders(root_directory)
