# Two-Circle-Intersection-Area

The program calculates the overlap area of two given circles. (implemented in python)

Usage-1: `python3 two-circle-intersection-area.py`
Usage-2: `python3 two-circle-intersection-area.py --x1 5 --y1 3 --r1 4 --x2 5.6 --y2 4.2 --r2 6`
Usage-3: `python3 two-circle-intersection-area.py -n`

## Usage-1
1. Open the code. 
2. Replace the radii and the center coordinates of the two circles (`p1, p2, r1, r2`).
3. Execute the code. 
4. The result determines whether the two circles have overlap. Show the overlap area if they have.

## Usage-2
1. Execute the code with command line arguments (circle information)
2. The result determines whether the two circles have overlap. Show the overlap area if they have.

## Usage-3
1. Execute the code with numerical mode
2. This mode shows only numerical result (overlap area) if there is 
3. This option can be used with Usage-2

## How it works?
1. Use the radii and the distance between two centers to determine the relationship of the two circles.
2. Calculate the angle between the two intersections and the center of circle by cosine-rule.
3. Calculate the triangle areas of two intersections and centers (t-area1, t-area2). 
4. Calculate the cone areas of two intersections and centers (c-area1, c-area2). 
5. Calculate the overlap areas by:
`Overlap Area = (c-area1 + c-area2) - (t-area1 + t-area2)`


