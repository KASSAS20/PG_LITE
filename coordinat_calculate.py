def coordinat_circle(R, X, Y):
    points_inside_circle = []
    for x in range(int(X - R), int(X + R) + 1):
        for y in range(int(Y - R), int(Y + R) + 1):
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                points_inside_circle.append((x, y))
    return points_inside_circle


def coordinat_rect(x_1, y_1, x_2, y_2):
    points_inside_rect = []
    for x in range(x_1, x_2 + 1):
        for y in range(y_1, y_2 + 1):
            points_inside_rect.append((x, y))
    return points_inside_rect
