from functools import cmp_to_key

def compareCoords(c1,c2):
    if c1[0]!=c2[0]:
        return c1[0]-c2[0]
    elif c1[1]!=c2[1]:
        return c1[1]-c2[1]
    else:
        return c1[2]-c2[2]

def addTriples(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1],t1[2]+t2[2])

def generateSurfaceCoords(p1,p2,p3,p4):
    coords = [p1,p2,p3,p4]
    
    coords.sort(key=cmp_to_key(compareCoords))

    return coords

DELTAS = [
    (0,0,0), # 0
    (0,0,1), # 1
    (1,0,1), # 2
    (1,0,0), # 3
    (0,1,0), # 4
    (0,1,1), # 5
    (1,1,1), # 6
    (1,1,0), # 7
]

SURFACE_DEFS = [(0,1,2,3),(3,2,6,7),(7,6,5,4),(4,5,1,0),(4,0,3,7),(6,2,1,5)]

def generateSurfaces(cubeTriple):
    result = []

    for surfDef in SURFACE_DEFS:
        result.append(generateSurfaceCoords(
            addTriples(cubeTriple,DELTAS[surfDef[0]]),
            addTriples(cubeTriple,DELTAS[surfDef[1]]),
            addTriples(cubeTriple,DELTAS[surfDef[2]]),
            addTriples(cubeTriple,DELTAS[surfDef[3]]),
        ))

    return result

def countSurfaces(cubes):
    freeSurfaces = []
    for cube in cubes:
        for surface in generateSurfaces(cube):
            if surface in freeSurfaces:
                freeSurfaces.remove(surface)
            else:
                freeSurfaces.append(surface)
        
    result=len(freeSurfaces)

    return result