def suggest_direction(obstacles, frame_width):
    if not obstacles:
        return "clear"

    # find closest object (largest area)
    nearest = max(obstacles, key=lambda x: x["area"])
    x1, _, x2, _ = nearest["box"]
    center = (x1 + x2) // 2

    # Determine position
    if center < frame_width * 0.33:
        position = "left"
    elif center > frame_width * 0.66:
        position = "right"
    else:
        position = "center"

    # Determine closeness
    area = nearest["area"]
    if area > 120000:
        distance = "very_close"
    elif area > 60000:
        distance = "close"
    else:
        distance = "far"

    return position, distance
