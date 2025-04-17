import cv2
import numpy as np
import time

# Creating  4x4 checkerboard
def create_checkerboard(size=4, square_size=50):
    board = np.zeros((size * square_size, size * square_size, 3), dtype=np.uint8)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                board[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = 255
    return board

checkerboard = create_checkerboard()
cv2.namedWindow('Checkerboard')

last_time = time.time()

while True:
    current_time = time.time()
 
    if current_time - last_time >= 1:
        checkerboard = cv2.bitwise_not(checkerboard)
        last_time = current_time
    
    cv2.imshow('Checkerboard', checkerboard)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
