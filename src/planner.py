import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal, obstacles):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        neighbors = [
            (current[0]+1, current[1]),
            (current[0]-1, current[1]),
            (current[0], current[1]+1),
            (current[0], current[1]-1)
        ]

        for n in neighbors:
            if n in obstacles or n[0] < 0 or n[1] < 0 or n[0] > 23 or n[1] > 23:
                continue

            new_cost = cost[current] + 1

            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                priority = new_cost + heuristic(n, goal)
                heapq.heappush(open_list, (priority, n))
                came_from[n] = current

    return came_from