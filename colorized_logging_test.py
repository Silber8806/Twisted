import sys
from twisted.python import log
from log_colorizer import ColorizedLogObserver

observer = ColorizedLogObserver(sys.stdout)
log.addObservor(observer.emit)

log.msg("Starting experiment")

log.msg("Logging exception")

try:
	1/0
except ZeroDivisionError, e:
	log.err(e)

log.msg("Ending experiment")