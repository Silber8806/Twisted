from twisted.internet.defer import Deferred

def myCallback(result):
	print result

def myErrback(failure):
	print failure

def addBold(result):
	return "<b>%s</b>" % (result,)

def addItalic(result):
	return "<i>%s</i>" % (result,)

def printHTML(result):
	print result

d = Deferred()
d.addCallback(myCallback)
d.callback("Triggering callback.")

d = Deferred()
d.addErrback(myErrback)
d.errback("Triggering errback.")

d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
d.callback("Hello World")

