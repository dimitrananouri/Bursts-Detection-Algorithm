import sys 
import math

# default values
s = 2
gamma = 1
d = False

# user input
algorithm = sys.argv[1]
args = sys.argv[3:]

for i in range(len(args)):
    if args[i] == '-s':
        s = float(args[i+1])
    elif  args[i] == '-g':
        gamma = float(args[i+1])
    elif args[i] == '-d':
        d = True

# reading activity
with open(sys.argv[2], 'r') as file:
    content = file.read()
activity = [float(num) for num in content.split()]

# space between activity
X = [activity[i+1] - activity[i] for i in range(len(activity)-1)]

# number of q (states)
min_X = (min(X[i] for i in range(len(X)-1)))
T = activity[-1]
k = math.ceil(1 + math.log(T, s) + math.log(1/min_X))

# function τ that calculates the cost
def T_function(i, j, n):
    if j <= i :
        return 0
    else: 
        return gamma * (j-i) * math.log(n)
    
# calculating g (l=s/g)
T = activity[-1]
n = len(X)
g = T/n

# viterbi algorithm
def viterbi(d, k, s):

    C = [[0 if i == 0 and j == 0 else math.inf for j in range(k)] for i in range(n+1)]
    P = [[0] * (n+1) for _ in range(k)]
    
    for t in range(1, n+1):
        for m in range(0,k):
            l_min = 0
            c_min = C[t-1][0] + T_function(0, m, n)
            for l in range(1, k):
                c = C[t-1][l] + T_function(l, m, n)
                if c < c_min:
                    c_min = c
                    l_min= l
            l_f = (s**m)/g 
            if l_f * math.exp(-(l_f * X[t-1])) != 0: # in case of math domain error
                C[t][m] = c_min - math.log(l_f * math.exp(-(l_f * X[t-1])))
            P[m][:t] = P[l_min][:t]
            P[m][t] = m

    if d:
        for row in C:
            two_demicals_row = [round(cost,2) if cost!=math.inf else math.inf for cost in row]
            print(two_demicals_row)

    c_min = C[n][0]
    s_min = 0
    for m in range(1, k):
        if C[n][m] < c_min:
            c_min = C[n][m]
            s_min = m

    return P[s_min]


# bellman - ford algorithm
def trellis(d, k, s):

    dist = {}
    pred = {}
    for i in range(n + 1):
        for j in range(k):
            dist[(i, j)] = math.inf
            pred[(i, j)] = -1
    
    dist[(0, 0)] = 0

    Edges = []
    for i in range(1,n+1):
        for l in range(k):
            for j in range(k):
                l_f = (s**j)/g
                if l_f * math.exp(-(l_f * X[i-1])) != 0: # in case of math domain error
                    weight = T_function(l, j, n) - math.log(l_f * math.exp(-(l_f * X[i-1])))
                    Edges.append(((i-1,l), (i,j), weight))

    dist_before_relaxation = {}
    for i in range (n-1):
        for u,v,w in Edges:
            if dist[u]!=math.inf and dist[v] > dist[u] + w:
                dist_before_relaxation[v] = dist[v]
                dist[v] = dist[u] + w
                pred[v] = u

    if d:
        printed_elements = set()
        X_index = 1
        exp_of_l = 0
        for u,v,w in Edges:
            l_f = (s**exp_of_l)/g
            i = int(pred[v][1])
            j = v[1]
            current_element = v

            if current_element not in printed_elements:

                if (l_f * math.exp(-(l_f * X[X_index-1]))) == 0:
                    emission_cost = 0
                else:
                    emission_cost = abs(math.log(l_f * math.exp(-(l_f * X[X_index-1]))))

                printed_elements.add(current_element)
                print(v, f"{dist_before_relaxation[v]:.2f}", "->", f"{dist[v]:.2f}", "from", pred[v], f"{dist[pred[v]]:.2f}", "+", 
                      f"{T_function(i, j, n):.2f}", "+", f"{emission_cost:.2f}")
                
                exp_of_l = exp_of_l + 1
                if exp_of_l == k:
                    exp_of_l = 0
                    X_index = X_index + 1

    index_min = 0
    w_min = dist[(n,0)]
    for i in range(1,k):
        if dist[(n,i)] < w_min:
            w_min = dist[(n,i)]
            index_min = i
    
    path = [(n, index_min)] 

    current_element = (n, index_min)
    while pred[current_element] != -1:
        current_element = pred[current_element]
        path.append(current_element)

    path.reverse()

    P = [0] * (n+1)
    for i in range(n+1):
        P[i] = path[i][1]

    return P
 
# output
if algorithm == 'viterbi':
    P = viterbi(d, k, s)
elif algorithm == 'trellis':
    P = trellis(d, k, s)

start_index = 0
current_state = P[0]

if d:
    print(len(X)+1 , P)

for i in range (1, len(P)):
    if P[i] != current_state:
        print(f"{P[i-1]} [{activity[start_index]} {activity[i-1]})")
        start_index = i-1
        current_state = P[i]

print(f"{P[-1]} [{activity[start_index]} {activity[-1]})")


   

   
