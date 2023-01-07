# TSegment = namedtuple('Segment', ['left', 'right'])

class Segment():
    """
    Segment de droite
    """

    def __init__(self, l, r):
        self.left = min(l, r)
        self.right = max(l, r)
        

    def __contains__(self, x):
        if isinstance(x, int):
            return x >= self.left and x <= self.right
        elif isinstance(x, Segment):
            return x.left >= self.left and x.right <= self.right


    def merge(self, other) -> bool:
        """
        Fusionne 2 segment, retourne True si fusion ok, False si echec
        """
        if isinstance(other, Segment):
            if other.left in self or other.right in self:
                self.right = max(other.right, self.right)
                self.left = min(other.left, self.left)
                return True

            return False

        else:
            raise ValueError ("Not implemented yet !")
        
    def __repr__(self) -> str:
        return f"|_{self.left},{self.right}_|"

@total_ordering
class CSensor:
    def __init__(self, coord: Point, beacon: Point) -> None:
        self.point = coord
        self.beacon = beacon

        self.man = man_dist(coord, beacon)

    def in_range(self, other: Point) -> bool:
        dist = man_dist(self.point, other)
        return dist <= self.man

    def detection_at_y(self, ym: int, minx, maxx) -> Set:
        detection = set()
        bornes = self._bornes_at_y(ym)
        if bornes:
            for x in range(bornes[0], bornes[1] + 1):
                if x >= minx and x <= maxx:
                    detection.add(x)
        return detection

    def segment_at_y(self, ym: int, minx, maxx) -> Segment|None:
        seg = None
        bornes = self._bornes_at_y(ym)
        xl = bornes[0]
        if xl < minx:
            xl = minx
        xr = bornes[1]
        if xr > maxx:
            xr = maxx
        # ic(bornes, xl, xr, maxx)
        if bornes:
            seg = Segment(xl, xr)
        return seg


    def _bornes_at_y(self, ym: int) -> Tuple[int, int]|None:
        # ic(man)
        dym = abs(ym - self.point.y)
        # ic(dym)
        if self.man < dym:
            return None
        dxm = self.man - dym
        # ic(dxm)
        return self.point.x - dxm, self.point.x + dxm

    def __eq__(self, other):
        return ((self.point, self.beacon) ==
                (other.point, other.beacon))

    def __lt__(self, other):
        return self.point.x < other.point.x

    def __hash__(self):
        return hash(self.point.x * self.point.y*self.beacon.x *self.beacon.y)

    def __repr__(self) -> str:
        return str(self.point.x) +"," +str(self.point.y) 



def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def in_range_sensor(ps, p1, dmax=9) -> bool:
    man_d = man_dist(ps , p1 )
    # ic(man_d, dmax)
    return man_d <= dmax


def in_range_dx(xs, x1, dmax=1) -> bool:
    return abs(x1 -xs) <= dmax


def bornes_range_sensor(ps, bs, ym):
    dx = abs(ps.x - bs.x)
    dy = abs(ps.y - bs.y)
    man = dx + dy
    # ic(man)
    dym = abs(ym - ps.y)
    # ic(dym)
    if man < dym:
        return None
    dxm = man - dym
    # ic(dxm)
    return ps.x - dxm, ps.x + dxm


def part1(sensors, ym):
    # recherche des sensors a y = 10
    # limites de detection
    # dx + dy
    sensors_ranged = set()

    # parcours des sensors potentiellement dans la portée
    # test au limites NS
    # ajout des bornes
    for sensor in sensors:
        # N et S
        rayon = sensors[sensor].dmax.y + sensors[sensor].dmax.x
        if in_range_sensor(sensor, (sensor.x, ym), rayon):
            sensors_ranged.add(sensor)
    ic(sensors_ranged)

    line_ym = {}
    nb_beacons_on_line = set(
        beacon_d.beacon for beacon_d in 
        (sensors[sensor] for sensor in sensors_ranged) 
        if beacon_d.beacon.y == ym)
    # ic(nb_beacons_on_line)

    nb = len(sensors_ranged)
    n = 0
    # for sensor in sorted(sensors_ranged):
    #     # ic(sensor)
    #     dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
    #     dmax_x = dmax # - dy
    #     for x in range(sensor.x-dmax_x, sensor.x+dmax_x +1):
    #         if x not in line_ym and \
    #             in_range_sensor(sensor, (x, ym), dmax_x):
    #                 line_ym[x] = 1
    #     n += 1
    #     ic (n , nb)

    for sensor in sorted(sensors_ranged):
        ic(sensor)
        dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
        bornes = bornes_range_sensor(sensor, sensors[sensor].beacon, ym)
        if bornes:
            for x in range(bornes[0], bornes[1]+1):
                if x not in line_ym and \
                    in_range_sensor(sensor, (x, ym), dmax):
                        line_ym[x] = 1
        n += 1
        ic (n , nb)

    no_beacon_here = len(line_ym) - len(nb_beacons_on_line)
    # ic(line_ym)
    # ic(nb_beacons_on_line)
    # ic(nb_libre)
    return no_beacon_here


def beacon_here(sensors, ym, max_range):
    sensors_ranged = set()
    for sensor, csensor in sensors.items():
        # rayon = sensors[sensor].dmax.y + sensors[sensor].dmax.x
        # if in_range_sensor(sensor, (sensor.x, ym), rayon):
        #     sensors_ranged.add(sensor)
        if csensor.in_range( Point(sensor.x, ym)):
            sensors_ranged.add(sensor)

    # line_ym = set(i for i in range(max_range))
    line_ym = []
    # ic(line_ym)
    # ic(sensors_ranged)

    for sensor in sorted(sensors_ranged):
        # dmax = sensors[sensor].dmax.x + sensors[sensor].dmax.y # dx + dy
        # bornes = bornes_range_sensor(sensor, sensors[sensor].beacon, ym)
        csensor =  sensors[sensor]
        # s = csensor.detection_at_y(ym, 0, max_range)
        segment = csensor.segment_at_y(ym, 0, max_range)
        if segment:
            # merge segments
            merged = False
            for seg in line_ym:
                merged = seg.merge(segment)
                if merged:
                    break
            if not merged:
                line_ym.append(segment)
    return line_ym


def freq(x):    return 56_000_011 - x * 4_000_000
# 19 × 131 × 149 × 151


def part2(sensors, ym, max_range):
    print("part2")
    ic(ym, max_range)
    beqs = set()
    line_ym = beacon_here(sensors, 11, max_range)

    # for y in range(11, 12):
    for y in range(0, max_range+1):
        line_ym = beacon_here(sensors, y, max_range)
        # ic(y, line_ym)
        for seg in line_ym:
            # ic(seg)
            for x in range(seg.left, seg.right +1):
                yfreq = freq(x)
                if yfreq > max_range or yfreq < 0: continue
                # ic(y, x, yfreq)
                beqs.add ((x, yfreq))
            
        if y%10 == 0:
            ic(y, line_ym, beqs)
    ic(beqs)

    for beq in beqs:
        x ,y = beq
        yfreq = freq(x)
        if int(yfreq) == yfreq:
            ic(beq)
            return beq
