from twisted.internet import reactor
from twisted.web import http

class MyRequestHandler(http.request):
	resources = {
		'/': '<h1>Home</h1>Home page',
		'/about': '<h1>About</h1>All about me',
	}

	def process(self):
		self.setHeader('Content-Type', 'text/html')
		if self.resources.has_key(self.path):
			self.write(self.resources[self.path])
		else:
			self.setResponseCode(http.NOT_FOUND)
			self.write("<h1>NOt Found</h1>Sorry, no such resource.")
		self.finish()

class MyHTTP(http.HTTPChannel):
	def buildProtocol(self,addr):
		return myHTTP()

reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()