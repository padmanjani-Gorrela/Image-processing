import cv2
import numpy as np

# Game settings
window_width = 800
window_height = 600
ball_radius = 20
ball_color = (0, 255, 0)  # Green
obstacle_color = (0, 0, 255)  # Red
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
gravity = 1
jump_strength = -15

# Initialize ball properties
ball_x = 100
ball_y = window_height - ball_radius
ball_velocity_y = 0
is_jumping = False

# Initialize obstacle properties
obstacles = [{'x': window_width, 'y': window_height - obstacle_height}]

# Initialize game state
score = 0
game_over = False

def draw_ball(frame):
    cv2.circle(frame, (ball_x, ball_y), ball_radius, ball_color, -1)

def draw_obstacles(frame):
    for obstacle in obstacles:
        cv2.rectangle(frame, (obstacle['x'], obstacle['y']),
                      (obstacle['x'] + obstacle_width, obstacle['y'] + obstacle_height),
                      obstacle_color, -1)

def update_ball():
    global ball_y, ball_velocity_y, is_jumping
    if is_jumping:
        ball_velocity_y += gravity
        ball_y += ball_velocity_y
        if ball_y >= window_height - ball_radius:
            ball_y = window_height - ball_radius
            is_jumping = False
            ball_velocity_y = 0
    else:
        if ball_y < window_height - ball_radius:
            ball_velocity_y += gravity
            ball_y += ball_velocity_y
        else:
            ball_y = window_height - ball_radius

def update_obstacles():
    global obstacles, score, game_over
    for obstacle in obstacles:
        obstacle['x'] -= obstacle_speed
        if obstacle['x'] + obstacle_width < 0:
            obstacles.remove(obstacle)
            score += 1
            obstacles.append({'x': window_width, 'y': window_height - obstacle_height})

def check_collision():
    global game_over
    for obstacle in obstacles:
        if (ball_x + ball_radius > obstacle['x'] and
            ball_x - ball_radius < obstacle['x'] + obstacle_width and
            ball_y + ball_radius > obstacle['y'] and
            ball_y - ball_radius < obstacle['y'] + obstacle_height):
            game_over = True

def draw_score(frame):
    cv2.putText(frame, f'Score: {score}', (window_width - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

def main():
    global is_jumping, game_over

    while True:
        frame = np.zeros((window_height, window_width, 3), dtype=np.uint8)
        
        if not game_over:
            update_ball()
            update_obstacles()
            check_collision()
        
        draw_ball(frame)
        draw_obstacles(frame)
        draw_score(frame)
        
        if game_over:
            cv2.putText(frame, 'Game Over', (window_width // 3, window_height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('Dino Game', frame)
        
        key = cv2.waitKey(30)
        if key == 27:  # Esc key to exit
            break
        elif key == ord(' '):  # Space bar to jump
            if not is_jumping and not game_over:
                is_jumping = True

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
