from PIL import Image, ImageDraw

def create_tetris_icon(size=512, filename="terminal-tetris.png"):
    """
    Generates a 512x512 icon for a terminal-based Tetris game.
    """
    # Define colors
    background_color = (20, 20, 30)  # Dark blue/purple
    grid_color = (50, 50, 70)

    # Tetromino colors (classic)
    colors = {
        'I': (0, 255, 255),   # Cyan
        'O': (255, 255, 0),   # Yellow
        'T': (128, 0, 128),   # Purple
        'L': (255, 165, 0),   # Orange
        'J': (0, 0, 255),     # Blue
        'S': (0, 255, 0),     # Green
        'Z': (255, 0, 0)      # Red
    }

    # Create a new image with a dark background
    image = Image.new("RGB", (size, size), background_color)
    draw = ImageDraw.Draw(image)

    # --- Draw the Grid ---
    grid_size = 10
    padding = 32
    cell_size = (size - 2 * padding) / grid_size

    grid_start = padding
    grid_end = size - padding

    for i in range(grid_size + 1):
        # Vertical lines
        x = grid_start + i * cell_size
        draw.line([(x, grid_start), (x, grid_end)], fill=grid_color, width=2)
        # Horizontal lines
        y = grid_start + i * cell_size
        draw.line([(grid_start, y), (grid_end, y)], fill=grid_color, width=2)

    def draw_block(x, y, color):
        """Helper function to draw a single block on the grid."""
        top_left_x = grid_start + x * cell_size
        top_left_y = grid_start + y * cell_size
        bottom_right_x = top_left_x + cell_size
        bottom_right_y = top_left_y + cell_size

        # Draw with a slight border effect
        draw.rectangle(
            [top_left_x, top_left_y, bottom_right_x, bottom_right_y],
            outline=(255, 255, 255),
            fill=color,
            width=2
        )

    # --- Draw some Tetrominoes ---
    # T-piece (purple)
    draw_block(4, 5, colors['T'])
    draw_block(3, 5, colors['T'])
    draw_block(5, 5, colors['T'])
    draw_block(4, 4, colors['T'])

    # L-piece (orange)
    draw_block(1, 7, colors['L'])
    draw_block(1, 8, colors['L'])
    draw_block(1, 9, colors['L'])
    draw_block(2, 9, colors['L'])

    # Z-piece (red)
    draw_block(7, 8, colors['Z'])
    draw_block(8, 8, colors['Z'])
    draw_block(6, 9, colors['Z'])
    draw_block(7, 9, colors['Z'])

    # O-piece (yellow)
    draw_block(4, 8, colors['O'])
    draw_block(5, 8, colors['O'])
    draw_block(4, 9, colors['O'])
    draw_block(5, 9, colors['O'])

    # --- Create Rounded Corners ---
    radius = 64
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, size, size), radius, fill=255)

    image.putalpha(mask)

    # Save the image
    image.save(filename, "PNG")
    print(f"Icon '{filename}' created successfully with rounded corners.")

if __name__ == "__main__":
    create_tetris_icon()