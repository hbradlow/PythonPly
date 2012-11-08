import regex

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "Point: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

def read_file(f):
    points = []
    line = f.readline()
    while line:
        number = r"[\d\w-.]+"
        match = regex.match(r"^\s*(" + number + r")\s+(" + number + r")\s+(" + number + r")\s*$",line)
        try:
            points.append(Point(float(match.group(1)),float(match.group(2)),float(match.group(3))))
        except ValueError:
            pass
        except AttributeError:
            pass
        line = f.readline()
    return points

if __name__=="__main__":
    import sys
    print "Filename >>>",
    fname = sys.stdin.readline().strip()
    with open(fname) as f:
        print read_file(f)[0:500]
