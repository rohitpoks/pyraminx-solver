# pyraminx-solver
A python program that solves an input Pyraminx and prints out the steps to solve it in the least number of rotations.

**Usage:**
Run solver.py, eg  usage: `python solver.py`

**Assumptions:**

This program assumes you have the corner pieces aligned to their center colors. For more information, check out my blog post (URL will be added soon :)).


**Inputting the pyraminx:**

The program asks for the state of the Pyraminx. To input this, first put the Pyraminx on a flat surface and have a vertex pointing at you. Then, identify the bottom face and mark the center color on the bottom face right below the front vertex. We shall use this center color as our point of reference to input the state of the pyraminx.

Start by having the front vertex point at you, and identify the left, right, back and bottom faces. Then, first enter the colors on the left face starting top left to bottom right. You can enter a sequence of characters to idenfity the face, like (`YGGBBRRRY` means yellow, green green green blue, blue red red red yellow). Then, rotate the pyraminx so you're now facing the right face and input the colors. Do the same for the back face. Finally, turn the pyraminx so you face the bottom face, and input the colors such that the centre color you identified earlier is on top, and it's the fourth color that you enter for the bottom face.


**Understanding outputs:**

Each step of the breadth first search prints out the number of states it has seen so far, and the number of new states it has uncovered. The program might output this for a total of 11 times before it gets to a solution. It then prints the corresponding rotations to solve the pyraminx.


**Don't see the steps to solve the pyraminx after the program termintates?**

This is because the pyraminx input to the program is incorrect. Double check to make sure you have the corner pieces aligned to the center colors, and the colors are formatted properly and entered in the correct order.


**Thanks for using my program, and hope your satisfied with the solution!**
