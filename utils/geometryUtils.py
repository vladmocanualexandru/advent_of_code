# generate intersection point of segments AB and CD, defined by A and B, and C and D
# a, b, c, d are (x,y) coordinate tuples
#
# https://stackoverflow.com/a/19550879
def getIntersection( a, b, c, d ) :

    s10_x = b[0] - a[0]
    s10_y = b[1] - a[1]
    s32_x = d[0] - c[0]
    s32_y = d[1] - c[1]

    denom = s10_x * s32_y - s32_x * s10_y

    if denom == 0 : return None # collinear

    denom_is_positive = denom > 0

    s02_x = a[0] - c[0]
    s02_y = a[1] - c[1]

    s_numer = s10_x * s02_y - s10_y * s02_x

    if (s_numer < 0) == denom_is_positive : return None # no collision

    t_numer = s32_x * s02_y - s32_y * s02_x

    if (t_numer < 0) == denom_is_positive : return None # no collision

    if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive : return None # no collision


    # collision detected

    t = t_numer / denom

    intersection_point = [ a[0] + (t * s10_x), a[1] + (t * s10_y) ]


    return intersection_point