from icecream import ic
def man_dist_pt(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def point_in_range(xm, ym, x0, y0, d0):
    
    # d2 = man_dist_pt(x0, y0, xm, ym)
    # ic(x0, y0, xm, ym, d0, d2)
    return man_dist_pt(x0, y0, xm, ym) <= d0
