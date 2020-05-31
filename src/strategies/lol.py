from strategies import strategy

class BiggestServer(strategy.Strategy):

	def calculate(self, servers, job):
		system = self.tree.getroot()
		# sort the servers in system.xml by core count
		server_definitions = sorted(system[0], key=lambda x: int(x.attrib["coreCount"]))
		minAvail = 9999999
		smallest_server = servers[0]
		for defin in server_definitions:
			server_type = defin.attrib["type"]
			
			for server in servers:
				if(server_type == server.get_name):
				 
						smallest_server = server
		return smallest_server
