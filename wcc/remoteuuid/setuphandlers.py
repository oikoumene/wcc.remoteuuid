from collective.grok import gs
from wcc.remoteuuid import MessageFactory as _

@gs.importstep(
    name=u'wcc.remoteuuid', 
    title=_('wcc.remoteuuid import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.remoteuuid.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
