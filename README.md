# Two-Circle-Intersection-Area

Calculates the overlap area of two given circles. Implemented in python. 

## Step
1. Open the code. 
2. Replace the radii and the center coordinates of the two circles (`p1, p2, r1, r2`).
3. Excute the code. 
4. The result determines whether the two circles have overlap. Show the overlap area if they have.

## How it works?
1. Use the radii and the distance between two centers to determine the relationship of the two circles.
2. Calculate the angle between the two intersections and the center of circle by cosine-rule.
3. Calculate the triangle areas of two intersections and centers (t-area1, t-area2). 
4. Calculate the cone areas of two intersections and centers (c-area1, c-area2). 
5. Calculate the overlap areas by:
`Overlap Area = (c-area1 + c-area2) - (t-area1 + t-area2)`


