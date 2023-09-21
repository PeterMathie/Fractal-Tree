# Fractal-Tree


They're upside down oops)

![image](https://github.com/PeterMathie/Fractal-Tree/assets/47106793/4cce8b3e-3354-4048-9ab0-b586040cda57)  ![image](https://github.com/PeterMathie/Fractal-Tree/assets/47106793/a8a49280-15e7-4a45-bce5-cd300c3f22c8)



Fractal Trees are a recursively drawn graphics which can be configured to resemble shapes found in nature, such as ferns, trees and brains.

The app has an interface to dynamically configure three variables and with this you can customise the graphic completely.Left and right angle will update the angle on the respective side that branch stems from. The depth variable is the number of iterations for which the fractal tree algorithm is run; expect a lot of lag past 14 iterations but this could be mitigated with multi-threading.

![image](https://github.com/PeterMathie/Fractal-Tree/assets/47106793/bda2fb08-7f6f-47e9-a764-910f617a2e03) ![image](https://github.com/PeterMathie/Fractal-Tree/assets/47106793/b6af1658-c2cb-49fc-9bbe-3a35e723e042)



The same tree with a depth of 9 (left) and depth of 16 (right)

The app is interactive, playing with the config sliders will dynamically change the angles and depth, the tree will transition smoothly from one form to another.

The tree is built layer by layer in the same way a binary heap is built, which allowed me to take advantage of heap functionality such as using (i-1)//2 to find the index of parent from child branch at index i. The implication of this is the tree blooms breath first rather than growing each branch deeply, which is a more common approach to drawing the trees. 
