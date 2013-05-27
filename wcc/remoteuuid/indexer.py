from plone.indexer.decorator import indexer
from wcc.remoteuuid.interfaces import IRemoteUUID, IRemoteUUIDAware

@indexer(IRemoteUUIDAware)
def remoteuuidIndexer(obj):
    return IRemoteUUID(obj, None)

