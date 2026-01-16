#!/usr/bin/env python3
import math

# Work out triangles sides in more detail than mix-For-Shapes-(2D+3D).py and can do angles, but doesn't do area or perimeter.

while not exit:
    print("(R)ight angled or (E)lse")
    
    mode = input()
    
    
    if mode.upper() == "R":
        hyp = None
        opp = None
        adj = None
        ang = None
        knowns = input("Knowns: ").split()
        for known in knowns:
            if known.upper() == "A":
                adj = float(input("Adjacent: "))
                
            elif known.upper() == "O":
                opp = float(input("Opposite: "))
                
            elif known.upper() == "H":
                hyp = float(input("Hypotenuse: "))
            elif known.upper() == "T":
                ang = math.radians(float(input("Theta: ")))
    
        for _ in range(3):
	    if adj is not None and opp is not None and hyp is not None:
                if not (adj**2 + opp**2 == hyp**2):
                    print("You have either entered information incorrectly for this triangle or this triangle cannot exist when it's right-angled.")
                    print("The information outputted by this program will be incorrect. Please use the (E)lse section for triangles that do not have a right-angle.")
            if hyp is not None and opp is not None and ang is None:
                ang = math.asin(opp / hyp)
            elif adj is not None and opp is not None and ang is None:
                ang = math.atan(float(opp) / (adj))
            elif hyp is not None and adj is not None and ang is None:
                ang = math.acos(float(adj) / float(hyp))
        
            if ang is not None and hyp is not None and opp is None:
                opp = hyp * math.sin(ang)
            elif ang is not None and adj is not None and opp is None:
                opp = adj * math.tan(ang)

            if ang is not None and hyp is not None and adj is None:
                adj = hyp * math.cos(ang)
            elif opp is not None and ang is not None and adj is None:
                adj = opp / math.tan(ang)

            if opp is not None and ang is not None and hyp is None:
                hyp = opp / math.sin(ang)
            elif adj is not None and ang is not None and hyp is None:
                hyp = adj / math.cos(ang)
        print() 
        print("─────────────────────")
        if adj is not None:
            print(f"    Adj: {round(adj, 4):g}")
        if opp is not None:
            print(f"    Opp: {round(opp, 4):g}")
        if hyp is not None:
            print(f"    Hyp: {round(hyp, 4):g}")
        if ang is not None:
            print(f"    Ang: {round(math.degrees(ang), 4):g}")
        print("─────────────────────")
        print()
    
    elif mode.upper() == "E":
        possible = 0
        hyp = None
        opp = None
        adj = None
        angHO = None
        angOA = None
        angAH = None
        knowns = input("Knowns: ").split()
        for known in knowns:
            if known.upper() == "A":
                adj = float(input("Adjacent: "))
                possible += 1
            elif known.upper() == "O":
                opp = float(input("Opposite: "))
                possible += 1
            elif known.upper() == "H":
                hyp = float(input("Hypotenuse: "))
                possible += 1
            elif known.upper() == "AHO" or known.upper() == "AOH":
                angHO = math.radians(float(input("Angle HO: ")))
                possible += 1
            elif known.upper() == "AOA" or known.upper() == "AAO":
                angOA = math.radians(float(input("Angle OA: ")))
                possible += 1
            elif known.upper() == "AAH" or known.upper() == "AHA":
                angAH = math.radians(float(input("Angle AH: ")))
                possible += 1
        if possible >= 3:
            for _ in range(3):
                if hyp is not None and adj is not None and angAH is not None and opp is None:
                    opp = math.sqrt(hyp**2 + adj**2 - (2 * hyp * adj) * math.cos(angAH))
                
                elif adj is not None and opp is not None and angOA is not None and hyp is None:
                    hyp = math.sqrt(adj**2 + opp**2 - (2 * adj * opp) * math.cos(angOA))
                
                elif hyp is not None and opp is not None and angHO is not None and adj is None:
                    adj = math.sqrt(hyp**2 + opp**2 - (2 * hyp * opp) * math.cos(angHO))
                
                if angHO is not None and angOA is not None and angAH is None:
                    angAH = math.radians(180 - (math.degrees(angHO) + math.degrees(angOA)))
                elif angAH is not None and angOA is not None and angHO is None:
                    angHO = math.radians(180 - (math.degrees(angAH) + math.degrees(angOA)))
                elif angHO is not None and angAH is not None and angOA is None:
                    angOA = math.radians(180 - (math.degrees(angHO) + math.degrees(angAH)))
                    
                if hyp is not None and opp is not None and adj is not None and angHO is None:
                    angHO = math.acos((opp**2 + adj**2 - hyp**2)/(opp * 2 * adj))
                if hyp is not None and opp is not None and adj is not None and angOA is None:
                    angOA = math.acos((opp**2 + hyp**2 - adj**2)/(opp * 2 * hyp))
                if hyp is not None and opp is not None and adj is not None and angAH is None:
                    angAH = math.acos((hyp**2 + adj**2 - opp**2)/(hyp * 2 * adj))
                    
        print() 
        print("─────────────────────")
        if adj is not None:
            print(f"    Adj: {round(adj, 4):g}")
        if opp is not None:
            print(f"    Opp: {round(opp, 4):g}")
        if hyp is not None:
            print(f"    Hyp: {round(hyp, 4):g}")
        if angHO is not None:
            print(f"    aHO: {round(math.degrees(angHO), 4):g}")
        if angOA is not None:
            print(f"    aOA: {round(math.degrees(angOA), 4):g}")
        if angAH is not None:
            print(f"    aAH: {round(math.degrees(angAH), 4):g}")
        print("─────────────────────")
        print()
    else:
        exit = True
                



