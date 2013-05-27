from wcc.remoteuuid.interfaces import IRemoteUUID
from wcc.remoteuuid.interfaces import IAttributeRemoteUUID
from wcc.remoteuuid.interfaces import IMutableRemoteUUID
from five import grok

from zope import interface
from zope import component

ATTRIBUTE_NAME='_wcc.remoteuuid'

@grok.implementer(IRemoteUUID)
@grok.adapter(IAttributeRemoteUUID)
def attributeRemoteUUID(context):
    return getattr(context, ATTRIBUTE_NAME, None)

class MutableRemoteUUID(grok.Adapter):
    grok.implements(IMutableRemoteUUID)
    grok.adapts(IAttributeRemoteUUID)

    def __init__(self, context):
        self.context = context

    def get(self):
        return getattr(self.context, ATTRIBUTE_NAME, None)

    def set(self, uuid):
        uuid = str(uuid)
        setattr(self.context, ATTRIBUTE_NAME, uuid)
