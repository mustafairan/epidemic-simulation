# import numpy as np
import  random
import matplotlib.pyplot as plt
# import matplotlib.animation as anim
import networkx as nx
# import time


class epidemic:

    def __init__(self):
        # self.colormap={'knows':'g','doesnt know':'w','died':'black','cured':'y',}
        self.nodes =70
        self.initiallyInfectedRatio=0.2
        self.initiallyInfectedNumber=int(self.nodes*self.initiallyInfectedRatio)
        self.edgeRatio=0.15
        self.edgeNumber=int(self.nodes*self.edgeRatio)
        self.infectionThreshold=7
        self.tellProbability=0.3
        self.believeProbability=0.3
        self.nodesize=300


        self.plottime=2
        self.iteration=0
        # self.infections= np.array([1]*self.initiallyInfectedNumber+[0]*(self.nodes-self.initiallyInfectedNumber))

        # np.random.shuffle(self.infections)

        #create our network
        self.ac=nx.fast_gnp_random_graph(self.nodes,self.edgeRatio)

        #everyone is doesnt know in iteration -1
        for i in self.ac.nodes():
            self.ac.node[i]['state']='doesnt know'
            self.ac.node[i]['color']='b'
        print "iteration ==>"+str(self.iteration)
        print nx.info(self.ac)

        #some get knows in iteration 0 (initially)
        for i in range (0, self.initiallyInfectedNumber+1):
            x=random.randint(0,self.nodes-1)
            while self.ac.node[x]['state']=='knows':
                x=random.randint(0,self.nodes-1)
            # del self.ac.node[x]['state']
            self.ac.node[x]['state']='knows'
    def probResult(self,probability):
        return random.random() >= probability

    def state(self,m):
        return self.ac.node[m]['state']
    def adjacentNumber(self,m):
        return len(self.ac.neighbors(m))
    def isknowsRightNow(self,m):
        return self.ac.node[m]['state']=='knows'
    def infectedAdjacentNumber(self,m):
        return sum (self.isknowsRightNow(i)  for i in  self.ac.neighbors(m))


    def spread(self):

        # pos=nx.random_layout (self.ac)
        # nx.draw_networkx(self.ac,pos)
        self.colors=[]
        for node,data in  self.ac.nodes_iter(data=True):
            if data['state']=='knows':

                self.colors.append('green')
                self.ac.node[node]['color']='green'
            else:
                self.colors.append('white')
                self.ac.node[node]['color']='white'
            print node,data['state'],self.ac.node[node]['color']
            # print "tesst",node,data['state']


        for i in range (0, self.nodes):# TODO self.node should be actuel number of node
            infNeigbour=self.infectedAdjacentNumber(i)
            if infNeigbour>=self.infectionThreshold and self.probResult(self.tellProbability) and self.probResult(self.believeProbability):
                self.ac.node[i]['state']='knows'
                self.ac.node[i]['color']='g'
            print i, self.ac.node[i]['state']





    def plotNetwork(self):

        # print nx.info(self.ac)
        # # pos=nx.random_layout (self.ac)
        # # nx.draw_networkx(self.ac,pos)
        #
        # colors=[]
        # for node,data in  self.ac.nodes_iter(data=True):
        #     if data['state']=='knows':
        #
        #         colors.append('green')
        #     else:
        #         colors.append('white')
        #
        #     print node,data['state']
        #     print "tesst",node,data['state']


        plt.ion()
        # nx.draw(self.ac,node_color=colors,with_labels=True,
        #         #node_size=90
        #          )
        # nx.draw_graphviz(self.ac)

        # plt.plot(self.ac)
        fig=plt.figure(figsize=(20,20))
        # anim.FuncAnimation(fig=fig,func=self.spread)

        plt.pause(0.002)

        while True:
            self.iteration=self.iteration+1
            print "iteration==> "+ str(self.iteration)

            self.spread()
            fig.clear()
            nx.draw_circular(self.ac,node_color=self.colors,with_labels=True,node_size=self.nodesize)
            # print self.colors
            # raw_input()
            # nx.write_graphml(self.ac,'www.graphml')
            # nx.write_gexf(self.ac,'www.gexf')

            # plt.show()

            plt.pause(self.plottime)


            # plt.clear()
        #  plt.draw()


def main():

    obj=epidemic()
    obj.plotNetwork()
    # print obj.infectedAdjacentNumber(1)

    # # nx.set_node_attributes(ac.nodes()[0],'hastalik',1)
    # # print random.choice(ac.nodes())


if __name__=='__main__':

    main()