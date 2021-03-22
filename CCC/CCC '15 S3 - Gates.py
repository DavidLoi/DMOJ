numGates = int(input())

gates = list(range(1, numGates + 1))

numPlanes = int(input())

planes = []

for i in range(numPlanes):
    planeNum = int(input())
    planes.append(planeNum)

planesLanded = 0

def checkPlane(plane, gates):
    checkGates = gates
    if plane in gates:
        return plane
    elif plane < gates[0]:
        return False
    else:
        plane = checkPlane(plane - 1, gates)
        return plane

for p in planes:
    checkedPlane = checkPlane(p, gates)
    if checkedPlane == False:
        break
    else:
        gates.remove(checkedPlane)
        planesLanded += 1

print(planesLanded)
