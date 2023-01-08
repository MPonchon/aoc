

from icecream import ic


def man_dist_pt(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def point_in_range(xm, ym, x0, y0, d0):
    
    # d2 = man_dist_pt(x0, y0, xm, ym)
    # ic(x0, y0, xm, ym, d0, d2)
    return man_dist_pt(x0, y0, xm, ym) <= d0


def x_in_segment(x, seg):
    return x >= seg[0] and x <= seg[1]


def merge_segments(segments):
    # print("** merge_segments")

    segments.sort() # x_s plus petit en premier
    # segs = sorted(segments, key=lambda seg: abs(seg[0]-seg[1])) # taille ++ en 1er
    # # segs = sorted(segments, key=lambda seg: abs(seg[0]-seg[1]), reverse=True) # taille ++ en 1er
    segs = segments
    
    merged_segs = []
    while segs:
        s1 = segs.pop(0)
        # ic(i_s, s1, segs)

        still_merging_segment = True
        while still_merging_segment:
            merged = False

            # taille = len(segs)
            for i in range(len(segs)):
                if i >= len(segs):
                    break
                # ic(i, len(segs), segs)
                li = merge_segment_s2_in_s1(s1, segs[i])
                # ic(li)
                if len(li) == 1:
                    del segs[i]
                    s1 = li[0]
                    merged = True
            
            if not merged:
                still_merging_segment = False

        merged_segs.append(s1)
        # ic(merged_segs, segs)
    return merged_segs


def merge_segment_s2_in_s1(s1, s2):
    # print(f"merge_segment_s2_in_s1 {s2} in {s1} ")
    # ic(s1, s2)

    if s1[1] + 1 == s2[0]:
        return[(s1[0], s2[1])]
    elif s2[1] + 1 == s1[0]:
        return[(s2[0], s1[1])]

    elif x_in_segment(s2[0], s1) and x_in_segment(s2[1], s1):
        return[s1]
    elif x_in_segment(s1[0], s2) and x_in_segment(s1[1], s2):
        return[s2]

    elif x_in_segment(s2[1], s1):
        return[(s2[0], s1[1])]

    elif x_in_segment(s2[0], s1):
        return[(s1[0], s2[1])]

    else:
        return [s1, s2]


def invert_segments(segments):
    # inverted = [ (s1[1]+1, s2[0]-1)  for s1, s2 in zip(segments, segments[1:])]
    inverted = []
    for s1, s2 in zip(segments, segments[1:]):
        if s1[0] < s2[0]:
            inverted.append((s1[1]+1, s2[0]-1) )
        else:
            inverted.append((s2[1]+1, s1[0]-1) )
    return inverted

    