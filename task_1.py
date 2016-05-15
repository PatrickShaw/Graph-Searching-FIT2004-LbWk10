from int_input import range_input
from e_circuit import e_circuit
from d_graph import d_graph
__author__ = "Patrick Shaw"

def convert_base(n,base):
   convertString = "ABCDE"
   if n < base:
      return convertString[n]
   else:
      return convert_base(n//base,base) + convertString[n%base]


def number_to_letter(char):
    if char == 0:
        return 'A'
    elif char == 1:
        return 'B'
    elif char == 2:
        return 'C'
    elif char == 3:
        return 'D'

if __name__ == "__main__":
    m = range_input("Enter m", 2, 5)
    n = range_input("Enter n", 2, 8)
    graph = d_graph(m, n)
    circuit = e_circuit(graph, m, n, graph[0])
    if circuit is not None:
        print("E circuit found!")
        print("".join([convert_base(x,m) for x in circuit]))
    else:
        print("E circuit not found!")
