from strategies import strategy
from operator import itemgetter

class costFit(strategy.Strategy):

    def getAlt(self,job, servers, server):
        alt = server
        for serverj in servers:
            if(serverj.get_cores() >= alt.get_cores() and serverj != alt and 1<=serverj.get_state()<=3):
                alt = serverj
                print('JOB SENT TO ALT FREE SERVER') #-> show when alt picked
        return alt

    def initServerUtil(self,servers,job):
        dict = {}
        for server in servers:
            dict[server.get_name() + str(server.get_id())] = 0
        return dict

    def addQueue(self,count,serverLoads, server):
        count += 1
        serverLoads[server.get_name() + str(server.get_id())] = count
        #print(serverLoads) #-> show most servers are not overqueued
        return serverLoads[server.get_name() + str(server.get_id())]

    def calculate(self, servers, job):
        serverLoads = self.initServerUtil(servers,job)
        for server in servers:
            queueCount = serverLoads[server.get_name() + str(server.get_id())]
            if(server.get_cores() == 0):
                queueCount = self.addQueue(queueCount,serverLoads, server)
                print("JOB QUEUED ON" + " " + server.get_name() + "id:" + str(server.get_id()) + " -- > " + "QCOUNT" +str(serverLoads[server.get_name() + str(server.get_id())])) #-> show when server is overloaded vs altServer chosen
                if(queueCount >= 1):
                    altServer = self.getAlt(job,servers,server)
                    return altServer

            return server
