import itertools
import time
def count_col_triang(input_):
    t0 = time.time()
    colours = []
    points = []
    def to_dict(arr):
        diction = {}
        for i in arr:
            t = tuple(i[0])
            colours.append(i[1])
            points.append(t)
            diction[t] = i[1]
        return diction
    def triangle_verifier(point1, point2, point3):
        x1 = point1[0]
        y1 =point1[1]
        x2 = point2[0]
        y2 =point2[1]
        x3 = point3[0]
        y3 =point3[1]
        if abs((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)) !=0:
            return True
        return False
    points_and_colours = to_dict(input_)
    t = (len(set(colours)))
    naive_triangles = itertools.combinations(points, 3)
    same_colour_triangles = []
    verified_triangles = [i for i in naive_triangles if triangle_verifier(i[0], i[1], i[2])]
    print(time.time()-t0)
    for triangle in verified_triangles:
        colours = [points_and_colours[i] for i in triangle]
        if colours.count(colours[0]) == len(colours):
            same_colour_triangles.append(colours[0])
    print(time.time()-t0)
    same_colour_triangle_set = list(set(same_colour_triangles))
    if len(same_colour_triangle_set) == 0:
        return len(points), t, len(same_colour_triangles), []
    count = {}
    for i in same_colour_triangle_set:
        count[i] = same_colour_triangles.count(i)
    nums = [count[i] for i in same_colour_triangle_set]
    max_value = max(nums)
    out = []
    for colour, value in count.items():
        if value == max_value:
            out.append(colour)
    out.append(max_value)
    return len(points),t, len(same_colour_triangles),out
