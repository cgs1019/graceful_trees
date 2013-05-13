#!/usr/bin/env python

def node_value(node):
  return node[0]

def graceful_mnstar_label(m, n, i, j):
  """returns the label for the ith node in the jth leg of a graceful mn-star"""

# generate a graceful star with m legs of length n
def graceful_mnstar(m, n):
  """returns an n-row x m-matrix matrix of labels for an mn-star"""
  return [[ ((-1) ** j) * (n * (-int(m / 2) + i) + int((j+1)/2))
             for i in range(m)
          ] for j in range(n)
         ]
  return [[ ((-1) ** j) * (n * (-int(m/2) + i)  + int((j + 1) / 2))
             for i in range(m)
          ] for j in range(n)
         ]

def print_graceful_mnstar(mnstar):
  m = len(mnstar[0])
  n = len(mnstar)
  print(
      '\n'.join(
        ['\t'.join(['%d' % (int((m*n)/2) + el) for el in row])
         for row in mnstar])
  )

def graceful_mnstar_edges(mnstar):
  m = len(mnstar[0])
  n = len(mnstar)
  # initialize to mnstar (copy)
  result = [list(x) for x in mnstar]
  result[0] = [ int((m * n + 1) / 2) - x for x in mnstar[0] ]
  for j in range(1, n):
    for i in range(m):
      result[j][i] = abs(mnstar[j][i] - mnstar[j-1][i])
  return result

