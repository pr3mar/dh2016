import json
import snap
import numpy as np

m = np.loadtxt(open("../matrica.csv", "rb"), delimiter=",")
print(m)

with open("../names.txt") as f:
    names = {y: x[:-1] for x, y in zip(f.readlines(), range(m.shape[0]))}

print names

G = snap.TNGraph.New()
for i in range(m.shape[0]):
    G.AddNode(i)
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i, j]:
            G.AddEdge(i, j)

#snap.DrawGViz(G, snap.gvlDot, "graph.png", "graph 1")

for node in G.Nodes():
    print(node.GetOutDeg()),
print "!"

d = {}
PRankH = snap.TIntFltH()
snap.GetPageRank(G, PRankH)

Gu = snap.ConvertGraph(snap.PUNGraph, G)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Gu, Nodes, Edges, 1.0)

# (spammer, ignorant, important, link)
for node in G.Nodes():
    d[names[node.GetId()]] = [float(node.GetOutDeg()) / (node.GetInDeg() + 0.1),
                              float(node.GetInDeg()) / (node.GetOutDeg() + 0.1),
                              PRankH[node.GetId()], Nodes[node.GetId()]]
    #print d[names[node.GetId()]]



def get_order(spammers):
    order_spam = sorted(range(len(spammers)), key=lambda k: -spammers[k])
    order_spam2 = zip(range(len(order_spam)), order_spam)
    order_spam3 = [0] * len(order_spam2)
    print(order_spam2[:5])
    for x, y in order_spam2:
        print(x, y)
        order_spam3[y] = x + 1
    return order_spam3

arranged = sorted(d.items())
order_spam = get_order([x[1][0] for x in arranged])
order_igno = get_order([x[1][1] for x in arranged])
order_impo = get_order([x[1][2] for x in arranged])
order_link = get_order([x[1][3] for x in arranged])

d2 = {}
for i in range(len(arranged)):
    d2[arranged[i][0]] = [order_spam[i], order_igno[i], order_impo[i], order_link[i]]
#d2 = {x: y for x, y in zip([x[0] for x in arranged], zip(order_spam, order_igno, order_impo, order_link))}
out = open('../viz/libs/ranks.js', 'w')
out.write("ranks=" + json.dumps(d2, indent=1) + ";")
