import numpy as np

def ApproxSpace(map: np.ndarray, rectangle: tuple, filename="c-space", savefile=False):
    # Approximate configuration space by drawing an mxn rectangle on pixels whose value is 1.
    # Where a pixel value of 1 is an obstacle.
    m, n = map.shape
    config_map = np.zeros(map.shape)
    rect_width, rect_height = rectangle
    for i in range(m*n):
        row, col = i // m, i % n
        if (map[row][col] > 0):
            pt1 = [col - int(rect_width/2), row - int(rect_height/2)]
            pt2 = [col + int(rect_width/2), row + int(rect_height/2)]

            pt1[0], pt2[0] = np.max([pt1[0], 0]), np.min([pt2[0], n-1])
            pt1[1], pt2[1] = np.max([pt1[1], 0]), np.min([pt2[1], m-1])
            config_map[pt1[1]:pt2[1], pt1[0]:pt2[0]] = 1
    if (savefile):
        np.save(f"{filename}.npy", config_map)
    return config_map