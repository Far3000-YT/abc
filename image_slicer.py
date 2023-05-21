from PIL import Image
import zipfile
import os

# Load the original image
img = Image.open("images/player/SeparateAnim/Idle.png")

# Calculate the number of rows and columns of tiles
num_cols = img.width // 16
num_rows = img.height // 16

# Create a new ZIP archive
with zipfile.ZipFile("tiles.zip", "w") as zip_file:

    # Iterate over each tile in the image
    for i in range(num_rows * num_cols):

        # Calculate the row and column indices of the tile
        row = i // num_cols
        col = i % num_cols

        # Calculate the coordinates of the tile
        x0 = col * 16
        y0 = row * 16
        x1 = x0 + 16
        y1 = y0 + 16

        # Extract the tile from the original image
        tile = img.crop((x0, y0, x1, y1))

        # Save the tile as a new image with a numbered filename
        filename = f"{i:02d}.png"
        tile.save(filename)

        # Add the tile image to the ZIP archive
        zip_file.write(filename)

        # Delete the original tile image file
        os.remove(filename)
