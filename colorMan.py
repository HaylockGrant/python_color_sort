import cv2 
#pip3 install opencv-python

#this function converts a color from RGB to cieLAB
def rgbtolab(r,g,b):
    r=r/255
    g=g/255
    b=b/255
    if r>0.04045:
        r=((r+0.055)/1.055)**2.4
    else:
        r=r/12.92
    if g>0.04045:
        g=((g+0.055)/1.055)**2.4
    else:
        g=g/12.92
    if b>0.04045:
        b=((b+0.055)/1.055)**2.4
    else:
        b=b/12.92
    r=r*100
    g=g*100
    b=b*100
    x=r*0.4124+g*0.3576+b*0.1805
    y=r*0.2126+g*0.7152+b*0.0722
    z=r*0.0193+g*0.1192+b*0.9505
    x=x/95.047
    y=y/100.000
    z=z/108.883
    if x>0.008856:
        x=x**(1/3)
    else:
        x=(7.787*x)+(16/116)
    if y>0.008856:
        y=y**(1/3)
    else:
        y=(7.787*y)+(16/116)
    if z>0.008856:
        z=z**(1/3)
    else:
        z=(7.787*z)+(16/116)
    l=(116*y)-16
    a=500*(x-y)
    b=200*(y-z)
    return l,a,b

def rgbtoxyz(r,g,b):
    r=r/255
    g=g/255
    b=b/255
    if r>0.04045:
        r=((r+0.055)/1.055)**2.4
    else:
        r=r/12.92
    if g>0.04045:
        g=((g+0.055)/1.055)**2.4
    else:
        g=g/12.92
    if b>0.04045:
        b=((b+0.055)/1.055)**2.4
    else:
        b=b/12.92
    r=r*100
    g=g*100
    b=b*100
    x=r*0.4124+g*0.3576+b*0.1805
    y=r*0.2126+g*0.7152+b*0.0722
    z=r*0.0193+g*0.1192+b*0.9505
    return x,y,z

def xyztolab(x,y,z):
    #E equal energy of the illuminant
    x=x/100.0
    y=y/100.0
    z=z/100.0
    #x,y,z = (x/95.047,y/100.000,z/108.883) # D65 white point CIE 1931 
    #x,y,z = (x/94.811,y/100.000,z/107.304) # D65 white point CIE 1964

    if x>0.008856:
        x=x**(1/3.0)
    else:
        x=(7.787*x)+(16/116.0)
    if y>0.008856:
        y=y**(1/3.0)
    else:
        y=(7.787*y)+(16/116.0)
    if z>0.008856:
        z=z**(1/3.0)
    else:
        z=(7.787*z)+(16/116.0)
    l=(116*y)-16
    a=500*(x-y)
    b=200*(y-z)
    return l,a,b

def rgbtolab2(r,g,b):
    x,y,z = rgbtoxyz(r,g,b)
    return xyztolab(x,y,z)

def hextorgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

def hextolab(hex):
    r,g,b = hextorgb(hex)
    return rgbtolab(r,g,b)