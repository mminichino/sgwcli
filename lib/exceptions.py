##
##

import sys
import os
import re
import inspect
import logging


def decode_error_code(code, message):
    if code == 4300:
        return IndexExistsError
    elif code == 5000:
        if re.match(".*Index .* already exists.*", message):
            return IndexExistsError
        else:
            return TransientError
    elif code == 12003:
        return TransientError
    else:
        return CouchbaseError


class cbUtilError(Exception):

    def __init__(self, message):
        frame = inspect.currentframe().f_back
        (filename, line, function, lines, index) = inspect.getframeinfo(frame)
        filename = os.path.basename(filename)
        print("Error: {} in {} {} at line {}: {}".format(type(self).__name__, filename, function, line, message))
        sys.exit(1)


class cbUtilException(Exception):

    def __init__(self, message):
        logger = logging.getLogger(self.__class__.__name__)
        frame = inspect.currentframe().f_back
        (filename, line, function, lines, index) = inspect.getframeinfo(frame)
        filename = os.path.basename(filename)
        self.message = "Error: {} in {} {} at line {}: {}".format(type(self).__name__, filename, function, line, message)
        logger.debug(f"Caught exception: {self.message}")
        super().__init__(self.message)


class HTTPExceptionError(cbUtilError):
    pass


class GeneralError(cbUtilError):
    pass


class NotAuthorized(cbUtilError):
    pass


class ForbiddenError(cbUtilError):
    pass


class ClusterInitError(cbUtilException):
    pass


class ClusterCloseError(cbUtilException):
    pass


class CbUtilEnvironmentError(cbUtilError):
    pass


class NodeUnreachable(cbUtilException):
    pass


class NodeConnectionTimeout(cbUtilException):
    pass


class NodeConnectionError(cbUtilException):
    pass


class NodeConnectionFailed(cbUtilException):
    pass


class DNSLookupTimeout(cbUtilException):
    pass


class NodeApiError(cbUtilError):
    pass


class AdminApiError(cbUtilError):
    pass


class CollectionGetError(cbUtilException):
    pass


class CollectionUpsertError(cbUtilException):
    pass


class CollectionSubdocUpsertError(cbUtilException):
    pass


class CollectionSubdocGetError(cbUtilException):
    pass


class CollectionRemoveError(cbUtilException):
    pass


class CollectionCountError(cbUtilException):
    pass


class CollectionWaitException(cbUtilException):
    pass


class CollectionCountException(cbUtilException):
    pass


class ScopeWaitException(cbUtilException):
    pass


class BucketWaitException(cbUtilException):
    pass


class QueryError(cbUtilException):
    pass


class QueryEmptyException(cbUtilException):
    pass


class QueryArgumentsError(cbUtilError):
    pass


class IndexStatError(cbUtilError):
    pass


class IndexConnectError(cbUtilError):
    pass


class IndexBucketError(cbUtilError):
    pass


class IndexScopeError(cbUtilError):
    pass


class IndexQueryError(cbUtilError):
    pass


class IndexCollectionError(cbUtilError):
    pass


class IndexInternalError(cbUtilError):
    pass


class ClusterConnectException(cbUtilException):
    pass


class BucketCreateException(cbUtilException):
    pass


class BucketDeleteException(cbUtilException):
    pass


class ScopeCreateException(cbUtilException):
    pass


class IsCollectionException(cbUtilException):
    pass


class CollectionCreateException(cbUtilException):
    pass


class NotFoundError(cbUtilException):
    pass


class CollectionNameNotFound(cbUtilException):
    pass


class IndexNotReady(cbUtilException):
    pass


class ClusterHealthCheckError(cbUtilException):
    pass


class ClusterKVServiceError(cbUtilException):
    pass


class ClusterQueryServiceError(cbUtilException):
    pass


class ClusterViewServiceError(cbUtilException):
    pass


class CouchbaseError(cbUtilException):
    pass


class IndexExistsError(cbUtilException):
    pass


class IndexNotFoundError(cbUtilException):
    pass


class TransientError(cbUtilException):
    pass


class TestPauseError(cbUtilException):
    pass


class BucketStatsError(cbUtilException):
    pass


class BucketNotFound(cbUtilException):
    pass


class CollectionNotDefined(cbUtilException):
    pass

