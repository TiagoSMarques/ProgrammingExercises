# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?


def dataRead(file):
    rectanges = {}
    with open(file, "r") as f:
        for line in f:
            # parsing the input string
            n, _, s, e = line.split(" ")
            x, y = map(int, (s[:-1].split(",")))
            c, d = map(int, e.split("x"))
            # build a dict with the claim as key and the respective rectange as value
            rectanges.update({n[1:]: [(x, y), (x + c, y + d)]})
    return rectanges


def checkOverlap(file):
    rectangles = dataRead(file)
    print(rectangles)
    # overlaps = set()
    overlaps = []
    totalArea = 0
    for claim in rectangles.keys():
        rOrig = rectangles.get(claim)
        x_a, y_a = rOrig[0]
        c_a, d_a = rOrig[1]
        for rOthers in rectangles.values():
            x_b, y_b = rOthers[0]
            c_b, d_b = rOthers[1]
            if rOthers != rOrig:
                if x_a < x_b < c_a and y_a < y_b < d_a:
                    overlaps.append(claim)
                    area = (min(c_a, c_b) - x_b) * (min(d_a, d_b) - y_b)
                    print(area, claim, rOthers)
                    totalArea += area

                elif x_a < c_b < c_a and y_a < y_b < d_a:
                    area = (min(c_a, c_b) - x_a) * (min(d_a, d_b) - y_b)
                    totalArea += area
                    print(area, claim, rOthers)
                    overlaps.append(claim)
                # overlaps.append(rOthers)
            # print("\n", overlaps)
    print("\n", "Total area: ", totalArea)
    # print(len(overlaps))


checkOverlap("3.txt")


# from collections import defaultdict

# with open("3.txt") as inputfile:
#     lines = inputfile.read().splitlines()

#     field = defaultdict(set)
#     intersections = defaultdict(set)

#     no_intersections = set()

#     for line in lines:
#         parts = line.split(" ")
#         cid = int(parts[0][1:])
#         left = int(parts[2].split(",")[0])
#         top = int(parts[2].split(",")[1][:-1])
#         width = int(parts[3].split("x")[0])
#         height = int(parts[3].split("x")[1])

#         no_intersections.add(
#             cid
#         )  # Assume this rectangle has no intersections with others
#         intersections_found = (
#             set()
#         )  # Every intersection that is found now will be removed from no_intersections later

#         for x in range(left, left + width):
#             for y in range(top, top + height):
#                 for other_cid in field[(x, y)]:
#                     intersections[cid].add(other_cid)
#                     intersections[other_cid].add(cid)
#                     intersections_found |= set([cid, other_cid])
#                 field[(x, y)].add(cid)

#         no_intersections -= intersections_found

#     print("A", sum([len(claims) >= 2 for claims in field.values()]))
#     print("B", list(no_intersections)[0])

