'''
Contained tests given 2 segments, a and b
As =  Bs    +-----------+   (a)
Ae >= Be    +------+

As =  Bs    +------+        (b)
Ae <= Be    +-----------+

As >=  Bs        +------+   (c)
Ae == Be    +-----------+

As <= Bs    +-----------+   (d)
Ae == Be          +-----+

As <  Bs    +-----------+   (e)
Ae >= Be      +------+ 

As >  Bs      +------+      (f)
Ae <= Be    +-----------+

Contiguous test given 2 segments, a and b
Ae <  Bs    +-----+
                     +--+

As >  Be            +---+
            +----+

'''

class ScheduleChecker:
    overlap_count = 0
    contiguous_count = 0
    contained_count = 0
    schedule_id = 1
    
    def eval (self, a:range, b:range):
        if ( not self.checkContiguous(a, b) ):
            if ( not self.checkContained(a, b) ):
                self.overlap_count += 1
                print (f"Overlap    | Line={self.schedule_id} | {a[0]}-{a[-1]},{b[0]}-{b[-1]}")
        
        self.schedule_id += 1

    def checkContiguous(self, a:range, b:range) -> bool:
        result = False
        count = 0
        amin = a[0]
        amax = a[-1] 
        bmin = b[0]
        bmax = b[-1] 

        if (amax < bmin):
            count = 1
            result = True
        elif (amin > bmax):
            count = 1
            result = True
        
        self.contiguous_count += count
        #if result:
        #    print (f"Contiguous | Line={self.schedule_id} | {amin}-{amax},{bmin}-{bmax}")
        return result

    def checkContained(self, a:range, b:range) -> bool:
        result = False
        count = 0
        amin = a[0]
        amax = a[-1] 
        bmin = b[0]
        bmax = b[-1]
        condition = ""

        if ( (amin == bmin) and (amax >= bmax) ):
            count = 1
            result = True
            condition = "a"
        elif ( (amin == bmin ) and (amax <= bmax) ):
            count = 1
            result = True
            condition = "b"
        elif ( (amin >= bmin) and (amax == bmax) ):  
            count = 1
            result = True
            condition = "c"
        elif ( (amin <= bmin) and (amax == bmax) ):
            count = 1
            result = True
            condition = "d"
        elif ( (amin < bmin) and (amax >= bmax) ):
            count = 1
            result = True
            condition = "e"
        elif ( (amin > bmin ) and (amax <= bmax ) ):
            count = 1
            result = True
            condition = "f"

        self.contained_count += count
        #if result:
        #    print (f"Contained ({condition})  | Line={self.schedule_id} | {amin}-{amax},{bmin}-{bmax}")
        return result
    
    def getOverlapCount(self):
        return self.overlap_count

    def getContaindCount(self):
        return self.contained_count

    def getContiguousCount(self):
        return self.contiguous_count

checker = ScheduleChecker()
with open("input.txt", "r") as input:
    for line in input:
        # parse schedule pairs
        pairs = line.split(",")

        # parse upper and lower bounds of each schedule pair
        bounds = []
        bounds.append([int(x) for x in pairs[0].split('-')])
        bounds.append([int(x) for x in pairs[1].split('-')])

        # expand the pair min/max with range
        a = range( bounds[0][0], bounds[0][1] + 1 )
        b = range ( bounds[1][0], bounds[1][1] + 1 )

        checker.eval(a,b)

# Result 1: 505 (too high)
# Result 2: 483 (too high)
print (f"Results: Overlap={checker.getOverlapCount()} | Contained={checker.getContaindCount()} | Contiguous={checker.getContiguousCount()}")