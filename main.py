#!/usr/bin/env python3
import pygame
import sys
import asyncio

# Initialize Pygame
pygame.init()

# Define constants for the screen
WIDTH, HEIGHT = 480, 480
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 120, 215)  # Microsoft Blue
HIGHLIGHT = (255, 0, 0)  # Red highlight for better visibility

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2D Chess Board')

# Load chess piece image
piece_image = pygame.image.load('chess_piece.png')
piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))

# Piece position
piece_position = (0, 0)
selected_piece = None

def draw_chess_board():
    screen.fill(WHITE)  # Fill the background with white
    
    for row in range(ROWS):
        for col in range(COLS):
            # Calculate the color of the square
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            
            # Draw the square
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Highlight selected piece
    if selected_piece is not None:
        row, col = selected_piece
        pygame.draw.rect(screen, HIGHLIGHT, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_piece(row, col):
    screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

async def main():
    global selected_piece, piece_position
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                
                if selected_piece is None:
                    # Select piece if clicked on it
                    if piece_position == (clicked_row, clicked_col):
                        selected_piece = piece_position
                else:
                    # Move piece to the clicked square
                    piece_position = (clicked_row, clicked_col)
                    selected_piece = None
        
        draw_chess_board()
        draw_piece(piece_position[0], piece_position[1])
        pygame.display.flip()

        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())