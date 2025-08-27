import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 640, 700
BOARD_SIZE = 600
CELL_SIZE = BOARD_SIZE // 3
PADDING = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unbeatable Tic-Tac-Toe")

font = pygame.font.Font(None, 60)
title_font = pygame.font.Font(None, 48)
button_font = pygame.font.Font(None, 36)

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.human_symbol = 'X'
        self.ai_symbol = 'O'
        
    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def make_move(self, row, col, player):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = player
            if self.check_winner():
                self.game_over = True
                self.winner = player
            elif self.is_board_full():
                self.game_over = True
                self.winner = 'Tie'
            else:
                self.current_player = 'O' if player == 'X' else 'X'
            return True
        return False
        
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        
        return None
        
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    moves.append((i, j))
        return moves
    
    def minimax(self, board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        winner = self.check_winner()
        if winner == self.ai_symbol:
            return 10 - depth
        elif winner == self.human_symbol:
            return depth - 10
        elif self.is_board_full():
            return 0
        
        if is_maximizing:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = self.ai_symbol
                        eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                        board[i][j] = ''
                        max_eval = max(max_eval, eval_score)
                        alpha = max(alpha, eval_score)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = self.human_symbol
                        eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                        board[i][j] = ''
                        min_eval = min(min_eval, eval_score)
                        beta = min(beta, eval_score)
                        if beta <= alpha:
                            break
            return min_eval
    
    def get_best_move(self):
        best_score = -math.inf
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = self.ai_symbol
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move

def draw_board(game):
    screen.fill(WHITE)
    
    title_text = title_font.render("Unbeatable Tic-Tac-Toe", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    screen.blit(title_text, title_rect)
    
    board_y_offset = 70
    
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (PADDING, board_y_offset + i * CELL_SIZE), 
                        (WIDTH - PADDING, board_y_offset + i * CELL_SIZE), 3)
        pygame.draw.line(screen, BLACK, (PADDING + i * CELL_SIZE, board_y_offset), 
                        (PADDING + i * CELL_SIZE, board_y_offset + BOARD_SIZE), 3)
    
    pygame.draw.rect(screen, BLACK, (PADDING, board_y_offset, BOARD_SIZE, BOARD_SIZE), 3)
    
    for row in range(3):
        for col in range(3):
            cell_x = PADDING + col * CELL_SIZE
            cell_y = board_y_offset + row * CELL_SIZE
            center_x = cell_x + CELL_SIZE // 2
            center_y = cell_y + CELL_SIZE // 2
            
            if game.board[row][col] == 'X':
                color = BLUE
                text = font.render('X', True, color)
                text_rect = text.get_rect(center=(center_x, center_y))
                screen.blit(text, text_rect)
            elif game.board[row][col] == 'O':
                color = RED
                pygame.draw.circle(screen, color, (center_x, center_y), CELL_SIZE // 3, 5)
    
    if game.game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(WHITE)
        overlay.set_alpha(200)
        screen.blit(overlay, (0, 0))
        
        if game.winner == 'Tie':
            result_text = title_font.render("It's a Tie!", True, BLACK)
        elif game.winner == game.human_symbol:
            result_text = title_font.render("You Win! (Impossible!)", True, GREEN)
        else:
            result_text = title_font.render("AI Wins!", True, RED)
        
        result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(result_text, result_rect)
        
        restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        pygame.draw.rect(screen, LIGHT_GRAY, restart_button)
        pygame.draw.rect(screen, BLACK, restart_button, 2)
        
        restart_text = button_font.render("Play Again", True, BLACK)
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_text_rect)
        
        return restart_button
    
    status_y = HEIGHT - 50
    if game.current_player == game.human_symbol:
        status_text = button_font.render("Your turn (X)", True, BLUE)
    else:
        status_text = button_font.render("AI thinking...", True, RED)
    
    status_rect = status_text.get_rect(center=(WIDTH // 2, status_y))
    screen.blit(status_text, status_rect)
    
    return None

def get_clicked_cell(pos):
    x, y = pos
    board_y_offset = 70
    
    if PADDING <= x <= WIDTH - PADDING and board_y_offset <= y <= board_y_offset + BOARD_SIZE:
        col = (x - PADDING) // CELL_SIZE
        row = (y - board_y_offset) // CELL_SIZE
        return row, col
    return None

def main():
    clock = pygame.time.Clock()
    game = TicTacToe()
    ai_move_timer = 0
    ai_move_delay = 1000
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.game_over:
                    restart_button = draw_board(game)
                    if restart_button and restart_button.collidepoint(event.pos):
                        game.reset_game()
                        ai_move_timer = 0
                elif game.current_player == game.human_symbol:
                    cell = get_clicked_cell(event.pos)
                    if cell:
                        row, col = cell
                        if game.make_move(row, col, game.human_symbol):
                            ai_move_timer = pygame.time.get_ticks()
        
        if not game.game_over and game.current_player == game.ai_symbol:
            if pygame.time.get_ticks() - ai_move_timer > ai_move_delay:
                best_move = game.get_best_move()
                if best_move:
                    row, col = best_move
                    game.make_move(row, col, game.ai_symbol)
        
        restart_button = draw_board(game)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()