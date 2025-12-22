#!/usr/bin/env python3
import math

# For general use, but doesn't do angles and for triangles it's probably better to just use complicated-triangles.py
        

while True:
    print("(2)D or (3)D")
    dimension = int(input())
    
    if dimension == 2:
        area = None
        side1 = None
        side2 = None
        side3 = None
        perimeter = None
        perpheight1 = None
        perpheight2 = None
        perpheight3 = None
        radius = None
        diameter = None
        print("(R)ectangle or (C)ircle or (T)riangle or (Tr)apezium or (Q)uadrilateral")
        shape = input().lower()
        
        # Rectangle
        
        if shape == "r":
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "a":
                    area = float(input("Area: "))
                elif known == "s1":
                    side1 = float(input("Side pair 1: "))
                elif known == "s2":
                    side2 = float(input("Side pair 2: "))
                elif known == "p":
                    perimeter = float(input("Perimeter: "))
            
            for _ in range(3):
            
                if area is None and side1 is not None and side2 is not None:
                    area = side1 * side2
                elif area is None and perimeter is not None and side1 is not None:
                    area = ((((side1 * 2) - perimeter)/2) * -1) * side1
                elif area is None and perimeter is not None and side2 is not None:
                    area = ((((side2 * 2) - perimeter)/2) * -1) * side2
                    
                if area is not None and side1 is not None and side2 is None:
                    side2 = area / side1
                elif area is not None and side2 is not None and side1 is None:
                    side1 = area/ side2
                    
                if perimeter is None and side1 is not None and side2 is not None:
                    perimeter = (2 * side1) + (2 * side2)
                    
                
                
                    
            print() 
            print("─────────────────────")
            if area is not None:
                print(f"    Area: {round(area, 4):g}")
            if side1 is not None:
                print(f"    Side pair 1: {round(side1, 4):g}")
            if side2 is not None:
                print(f"    Side pair 2: {round(side2, 4):g}")
            if perimeter is not None:
                print(f"    Perimeter: {round(perimeter, 4):g}")
            print("─────────────────────")
            print()
        elif shape == "c":
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "c":
                    circumference = float(input("Circumference: "))
                elif known == "r":
                    radius = float(input("Radius: "))
                elif known == "d":
                    diameter = float(input("Diameter: "))
                elif known == "a":
                    area = float(input("Area: "))
                    
            for _ in range(3):
                
                if radius is not None and diameter is None:
                    diameter = radius * 2
                elif diameter is not None and radius is None:
                    radius = diameter / 2
                
                if area is None and radius is not None:
                    area = math.pi * (radius**2)
                
                if radius is None and area is not None:
                    radius = math.sqrt(area / math.pi)
                    
                if circumference is None and radius is not None:
                    circumference = math.pi * 2 * radius
                    
            print() 
            print("─────────────────────")
            if area is not None:
                print(f"    Area: {round(area, 4):g}")
            if radius is not None:
                print(f"    Radius: {round(radius, 4):g}")
            if diameter is not None:
                print(f"    Diameter: {round(diameter, 4):g}")
            if circumference is not None:
                print(f"    Circumference: {round(circumference, 4):g}")
            print("─────────────────────")
            print()
            
        elif shape == "t":
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "s1":
                    side1 = float(input("Side 1: "))
                elif known == "s2":
                    side2 = float(input("Side 2: "))
                elif known == "s3":
                    side3 = float(input("Side 3: "))
                elif known == "p":
                    perimeter = float(input("Perimeter: "))
                elif known == "a":
                    area = float(input("Area: "))
                elif known == "ph1":
                    perpheight1 = float(input("Altitude from Side 1: "))
                elif known == "ph2":
                    perpheight2 = float(input("Altitude from Side 2: "))
                elif known == "ph3":
                    perpheight3 = float(input("Altitude from Side 3: "))
                    
            for _ in range(3):
            
                if perimeter is None and side1 is not None and side2 is not None and side3 is not None:
                    perimeter = side1 + side2 + side3
                
                if side1 is None and side2 is not None and side3 is not None and perimeter is not None:
                    side1 = (perimeter - side2) - side3
                if side2 is None and side1 is not None and side3 is not None and perimeter is not None:
                    side2 = (perimeter - side1) - side3
                if side3 is None and side1 is not None and side2 is not None and perimeter is not None:
                    side3 = (perimeter - side2) - side1
                    
                if area is None and perpheight1 is not None and side1 is not None:
                    area = perpheight1 * side1 * 0.5
                if area is None and perpheight2 is not None and side2 is not None:
                    area = perpheight2 * side2 * 0.5
                if area is None and perpheight3 is not None and side3 is not None:
                    area = perpheight3 * side3 * 0.5
                    
                if perpheight1 is None and area is not None and side1 is not None:
                    perpheight1 = (area * 2) / side1
                if perpheight2 is None and area is not None and side2 is not None:
                    perpheight2 = (area * 2) / side2
                if perpheight3 is None and area is not None and side3 is not None:
                    perpheight3 = (area * 2) / side3
                    
                if area is None and perimeter is not None and side1 is not None and side2 is not None and side3 is not None:
                    temp_semiperimeter = perimeter / 2
                    area = math.sqrt((temp_semiperimeter * (temp_semiperimeter - side1)) * (temp_semiperimeter - side2) * (temp_semiperimeter - side3))
                    
                if perpheight1 is None and side1 is not None and area is not None:
                    perpheight1 = (area * 2) / side1
                    
                if perpheight2 is None and side2 is not None and area is not None:
                    perpheight2 = (area * 2) / side2
                    
                if perpheight3 is None and side3 is not None and area is not None:
                    perpheight3 = (area * 2) / side3
                    
            print() 
            print("─────────────────────")
            if area is not None:
                print(f"    Area: {round(area, 4):g}")
            if perimeter is not None:
                print(f"    Perimeter: {round(perimeter, 4):g}")
            if side1 is not None:
                print(f"    Side 1: {round(side1, 4):g}")
            if side2 is not None:
                print(f"    Side 2: {round(side2, 4):g}")
            if side3 is not None:
                print(f"    Side 3: {round(side3, 4):g}")
            if perpheight1 is not None:
                print(f"    Altitude 1: {round(perpheight1, 4):g}")
            if perpheight2 is not None:
                print(f"    Altitude 2: {round(perpheight2, 4):g}")
            if perpheight3 is not None:
                print(f"    Altitude 3: {round(perpheight3, 4):g}")
            print("─────────────────────")
            print()
                    
        elif shape == "tr":
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "s1":
                    side1 = float(input("Side 1: "))
                elif known == "s2":
                    side2 = float(input("Side 2: "))
                elif known == "s3":
                    side3 = float(input("Side 3 pair: "))
                elif known == "p":
                    perimeter = float(input("Perimeter: "))
                elif known == "a":
                    area = float(input("Area: "))
                elif known == "ph1":
                    perpheight1 = float(input("Altitude: "))
                    
            for _ in range(3):
            
                if area is None and perpheight1 is not None and side1 is not None and side2 is not None:
                    area = perpheight1 * ((side1 + side2) / 2)
                    
                if perpheight1 is None and area is not None and side1 is not None and side2 is not None:
                    perpheight1 = area/((side1 + side2)/2)
                    
                if perpheight2 is None and area is not None and side2 is not None and side3 is not None:
                    perpheight2 = area/((side2 + side3)/2)
                
                if perpheight3 is None and area is not None and side3 is not None and side1 is not None:
                    perpheight3 = area/((side3 + side1)/2)
                    
                if side1 is None and side2 is not None and area is not None and perpheight1 is not None:
                    side1 = (area/perpheight1 * 2) - side2
                if side2 is None and side1 is not None and area is not None and perpheight1 is not None:
                    side2 = (area/perpheight1 * 2) - side1
                    
                if perimeter is None and side1 is not None and side2 is not None and side3 is not None:
                    perimeter = side1 + side2 + (2 * side3)
                    
                if side3 is None and perimeter is not None and side1 is not None and side2 is not None:
                    side3 = (perimeter - side1 - side2)/2
                if side2 is None and perimeter is not None and side1 is not None and side3 is not None:
                    side2 = (perimeter - side1 - side3)
                if side1 is None and perimeter is not None and side2 is not None and side3 is not None:
                    side1 = (perimeter - side2 - side3)
                    
                if side3 is None and perpheight1 is not None and side2 is not None and side1 is not None:
                    side3 = math.sqrt(perpheight1**2 + ((abs(side1 - side2)/2)**2))
                    
            print() 
            print("─────────────────────")
            if side1 is not None:
                print(f"    Side 1: {round(side1, 4):g}")
            if side2 is not None:
                print(f"    Side 2: {round(side2, 4):g}")
            if side3 is not None:
                print(f"    Side 3: {round(side3, 4):g}")
            if perimeter is not None:
                print(f"    Perimeter: {round(perimeter, 4):g}")
            if area is not None:
                print(f"    Area: {round(area, 4):g}")
            if perpheight1 is not None:
                print(f"    Altitude: {round(perpheight1, 4):g}")
            print("─────────────────────")
            print()
                    
    elif dimension == 3:
        volume = None
        surfarea = None
        length = None
        width = None
        height = None
        circumference = None
        radius = None
        diameter = None
        
        print("(C)uboid or (S)phere or (Te)trahedron or (Sq)uare-based pyramid or (Co)ne")
        shape = input().lower()
        
        
        if shape == "c":
        
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "l":
                    length = float(input("Length: "))
                elif known == "w":
                    width = float(input("Width: "))
                elif known == "h":
                    height = float(input("Height: "))
                elif known == "v":
                    volume = float(input("Volume: "))
                elif known == "sa":
                    surfarea = float(input("Surface area: "))
                    
            for _ in range(3):
                
                if volume is None and width is not None and height is not None and length is not None:
                    volume = length * width * height
                
                if width is None and volume is not None and height is not None and length is not None:
                    width = (volume / height) / length
                if length is None and volume is not None and height is not None and width is not None:
                    length = (volume / height) / width
                if height is None and volume is not None and width is not None and length is not None:
                    height = (volume / width) / length
                    
                if surfarea is None and volume is not None and width is not None and length is not None and height is not None:
                    surfarea = 2 * ((length * height) + (width * height) + (width * length))
                    
            print() 
            print("─────────────────────")
            if length is not None:
                print(f"    Length: {round(length, 4):g}")
            if width is not None:
                print(f"    Width: {round(width, 4):g}")
            if height is not None:
                print(f"    Height: {round(height, 4):g}")
            if volume is not None:
                print(f"    Volume: {round(volume, 4):g}")
            if surfarea is not None:
                print(f"    Surface area: {round(surfarea, 4):g}")
            print("─────────────────────")
            print()
            
            
        elif shape == "s":
            
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "r":
                    radius = float(input("Radius: "))
                elif known == "sa":
                    surfarea = float(input("Surface area: "))
                elif known == "d":
                    diameter = float(input("Diameter: "))
                elif known == "v":
                    volume = float(input("Volume: "))
                elif known == "c":
                    circumference = float(input("Circumference: "))
                    
            for _ in range(3):
            
                if radius is None and diameter is not None:
                    radius = diameter / 2
                elif diameter is None and radius is not None:
                    diameter = radius * 2
                    
                if volume is None and radius is not None:
                    volume = (4 / 3) * math.pi * (radius**3)
                
                if radius is None and volume is not None:
                    radius = ((volume / (4 / 3)) / math.pi) ** (1/3)
                    
                if surfarea is None and radius is not None:
                    surfarea = (4 * math.pi) * (radius**2)
                    
                if circumference is None and diameter is not None:
                    circumference = math.pi * diameter
                    
            print() 
            print("─────────────────────")
            if radius is not None:
                print(f"    Radius: {round(radius, 4):g}")
            if diameter is not None:
                print(f"    Diameter: {round(diameter, 4):g}")
            if volume is not None:
                print(f"    Volume: {round(volume, 4):g}")
            if circumference is not None:
                print(f"    Circumference: {round(circumference, 4):g}")
            if surfarea is not None:
                print(f"    Surface area: {round(surfarea, 4):g}")
            print("─────────────────────")
            print()
            
        elif shape == "te":
        
            print()
            print("(R)egular or (E)lse")
            tetrahedron_choice = input()
            
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "v":
                    volume = float(input("Volume: "))
                elif known == "sa":
                    surfarea = float(input("Surface area: "))
                elif known == "h":
                    height = float(input("Altitude (or height): "))
                elif known == "w":
                    width = float(input("Width (base): "))
                elif known == "l":
                    length = float(input("Length (base): "))
                    
            for _ in range(3):
                
                if volume is None and length is not None and width is not None and height is not None:
                    volume = ((length * width) / 2) * (1/3) * height
                    
                if length is None and volume is not None and width is not None and height is not None:
                    length = (((volume * 3) / height) * 2 / width)
                elif width is None and volume is not None and length is not None and height is not None:
                    width = (((volume * 3) / height) * 2 / length)
                elif height is None and volume is not None and length is not None and width is not None:
                    height = (volume * 3) / ((length * width) / 2)
                
                
                if tetrahedron_choice == "e": 
                    if surfarea is None and height is not None and length is not None and width is not None:
                        surfarea = (1/2) * ((length * width)+(length * height)+(width * height)+ math.sqrt( (length**2 * width**2) + (length**2 * height**2) + (width**2 * height**2)  ))
                elif tetrahedron_choice == "r":
                
                    if length is not None and width is not None:
                    
                        not_a_side = None
                        if length > width:
                            not_a_side = length
                        elif width >= length:
                            not_a_side = width
                        if surfarea is None:
                            surfarea = math.sqrt(3) * not_a_side**2
                    
                    
            print() 
            print("─────────────────────")
            if length is not None:
                print(f"    Length: {round(length, 4):g}")
            if width is not None:
                print(f"    Width: {round(width, 4):g}")
            if height is not None:
                print(f"    Height: {round(height, 4):g}")
            if volume is not None:
                print(f"    Volume: {round(volume, 4):g}")
            if surfarea is not None:
                print(f"    Surface area: {round(surfarea, 4):g}")
            print("─────────────────────")
            print()
            
        elif shape == "sq":
            
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "l":
                    length = float(input("Length: "))
                elif known == "w":
                    width = float(input("Width: "))
                elif known == "h":
                    height = float(input("Height: "))
                elif known == "v":
                    volume = float(input("Volume: "))
                elif known == "sa":
                    surfarea = float(input("Surface area: "))
                    
            for _ in range(3):
            
                if volume is None and length is not None and width is not None and height is not None:
                    volume = length * width * height * (1/3)
                
                elif length is None and volume is not None and width is not None and height is not None:
                    length = ((volume * 3) / height) / width
                
                elif width is None and volume is not None and length is not None and height is not None:
                    width = ((volume * 3) / height) / length
                
                elif height is None and volume is not None and length is not None and width is not None:
                    height = ((volume * 3) / width) / length
                    
                if surfarea is None and length is not None and width is not None and height is not None:
                    surfarea = (length * width) + (length * math.sqrt((width/2)**2 + height**2)) + (width * math.sqrt((length/2)**2 + height**2))
                    
            print() 
            print("─────────────────────")
            if length is not None:
                print(f"    Length: {round(length, 4):g}")
            if width is not None:
                print(f"    Width: {round(width, 4):g}")
            if height is not None:
                print(f"    Height: {round(height, 4):g}")
            if volume is not None:
                print(f"    Volume: {round(volume, 4):g}")
            if surfarea is not None:
                print(f"    Surface area: {round(surfarea, 4):g}")
            print("─────────────────────")
            print()
            
        elif shape == "co":
            
            knowns = input("Knowns: ").lower().split()
            for known in knowns:
                if known == "sa":
                    surfarea = float(input("Surface area: "))
                elif known == "r":
                    radius = float(input("Radius: "))
                elif known == "d":
                    diameter = float(input("Diameter: "))
                elif known == "v":
                    volume = float(input("Volume: "))
                elif known == "h":
                    height = float(input("Altitude (or height): "))
                    
            for _ in range(3):
            
                if radius is None and diameter is not None:
                    radius = diameter / 2
                elif diameter is None and radius is not None:
                    diameter = radius * 2
            
                if volume is None and radius is not None and height is not None:
                    volume = radius**2 * math.pi * height * (1/3)
                elif radius is None and volume is not None and height is not None:
                    radius = math.sqrt(((volume * 3) / height) / math.pi)
                elif height is None and volume is not None and radius is not None:
                    height = ((volume * 3) / radius**2) / math.pi
                    
                if surfarea is None and height is not None and radius is not None:
                    surfarea = (math.pi * radius * math.sqrt(radius**2 + height**2)) + (math.pi * radius**2)
                    
            print() 
            print("─────────────────────")
            if radius is not None:
                print(f"    Radius: {round(radius, 4):g}")
            if diameter is not None:
                print(f"    Diameter: {round(diameter, 4):g}")
            if height is not None:
                print(f"    Height: {round(height, 4):g}")
            if volume is not None:
                print(f"    Volume: {round(volume, 4):g}")
            if surfarea is not None:
                print(f"    Surface area: {round(surfarea, 4):g}")
            print("─────────────────────")
            print()
