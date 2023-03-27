""" 0x67 is a scout ant searching for food and discovers a beehive nearby. As it approaches the honeycomb, 0x67 can sense an area inside packed with dried honey that can be easily carried back to the nest and stored for winter. However, it must burrow through the honeycomb to reach the cell containing the sweet loot. If 0x67 can create a passage to the honey to help the other ants find it, it will do so before returning to the nest.

The cells of the honeycomb are numbered in row major order, so cell IDs can be assigned as shown below:

\includegraphics[width=0.5\textwidth ]{r4hexnumdemo.png}
When 0x67 discovers the opening to the honeycomb, it enters the cell. Some ants are stronger than others, depending on their age, so 0x67 can only chew through at most N cells before its jaw wears out and must return to the nest to recuperate. The honeycomb is hexagonal, and each edge length is R cells. 0x67 enters through a hole at location A and must get to the honey at location B by chewing a path through no more than N adjacent cells. Because ants can be competitive, 0x67 wants to reach the honey by chewing through the fewest possible cells. 0x67 can also sense some of the cells are hardened with wax and impossible to penetrate, so it will have to chew around those to reach the cell at location B.

\includegraphics[width=0.5\textwidth ]{r6hexdemo_path.png}
Figure 1: K=6
\includegraphics[width=0.5\textwidth ]{r6hexdemo_nopath.png}
Figure 2: No
Scout ants have rudimentary computational skills, and before 0x67 begins to chew, it will work out where it needs to go, and compute K, the least number of cells it needs to chew through to get from A to B, where B is the Kth cell. If K>N, 0x67 will not be strong enough to make the tunnel. When 0x67 returns to the nest, it will communicate to its nestmates how many cells it chewed through to get to B, or will report that it could not get to the honey.

Input
The input contains two lines. The first line contains five blank separated integers: R N A B X

R: the length (number of cells) of each edge of the grid, where 2≤R≤20. The total number of cells in the grid can be determined by taking a difference of cubes, R3−(R−1)3.

N: the maximum number of cells 0x67 can chew through, where 1≤N<R3−(R−1)3.

A: the starting cell ID, This cell is located on one of the grid edges: The cell has fewer than six neighbors.

B: the cell ID of the cell containing the honey, where 1≤B≤R3−(R−1)3.

X: the number of wax-hardened cells, where 0≤X<(R3−(R−1)3)−1.

The second line contains X integers separated by spaces, where each integer is the ID of a wax-hardened cell.

The ID’s, A, B, and all the ID’s on the second line, are distinct positive integers less than or equal to R3−(R−1)3.

Output
A single integer K if 0x67 reached the honey at cell B, where B is the Kth cell, otherwise the string No if it was impossible to reach the honey by chewing through N cells or less. """


#! /usr/bin/python3


def input_data():
    f = open('problems/problem_b/sample-data/1.in', 'r')
    data = f.read()
    data = data.split('\n')
    row1 = [int(i) for i in data[0].split(' ')]
    row2 = [int(i) for i in data[1].split(' ')]
    return row1, row2


class Honeycomb():

    def __init__(self, data):
        self.edge_length = data[0][0]
        self.mid_length = 2 * self.edge_length - 1
        self.total_cell_count = self.edge_length**3 - (self.edge_length - 1)**3
        self.max_move_count = data[0][1]
        self.starting_cell = data[0][2]
        self.finish_cell = data[0][3]
        self.hardened_cell_count = data[0][4]
        self.hardened_cells_id = data[1]
        self.graph = {}
        for i in range(1, self.total_cell_count + 1):
            self.graph[str(i)] = self.find_edges()[i - 1]

    def get_graph(self):
        return self.graph

    def find_edges(self):
        edges = []

        for row, row_length in enumerate(self.edge_length, self.mid_length):
            for column in range(1, self.mid_length):
                if column > row_length:
                    break

        return edges

    def node_type(self, row, column):
        ntyp = []
        if row == 1:
            ntyp.append()
        elif row == self.mid_length:
            ntyp.append()
        if column == 1:
            ntyp.append()
        elif column == self.mid_length:
            ntyp.append()

        return ntyp


if __name__ == "__main__":
    print(Honeycomb(input_data()).get_graph())