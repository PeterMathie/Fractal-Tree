# Fractal-Tree


They're upside down oops)



Fractal Trees are a recursively drawn graphics which can be configured to resemble shapes found in nature, such as ferns, trees and brains.

The app has an interface to dynamically configure three variables and with this you can customise the graphic completely.Left and right angle will update the angle on the respective side that branch stems from. The depth variable is the number of iterations for which the fractal tree algorithm is run; expect a lot of lag past 14 iterations but this could be mitigated with multi-threading.



The same tree with a depth of 9 (left) and depth of 16 (right)

The app is interactive, playing with the config sliders will dynamically change the angles and depth, the tree will transition smoothly from one form to another.

The tree is built layer by layer in the same way a binary heap is built, which allowed me to take advantage of heap functionality such as using (i-1)//2 to find the index of parent from child branch at index i. The implication of this is the tree blooms breath first rather than growing each branch deeply, which is a more common approach to drawing the trees. 
