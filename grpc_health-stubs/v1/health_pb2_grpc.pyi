"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)

from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryStreamMultiCallable,
    UnaryUnaryMultiCallable,
)

from grpc.health.v1.health_service_pb2 import (
    HealthCheckRequest,
    HealthCheckResponse,
)

from typing import (
    Iterator,
)


class HealthStub:
    def __init__(self, channel: Channel) -> None: ...
    Check: UnaryUnaryMultiCallable[
        HealthCheckRequest,
        HealthCheckResponse]

    Watch: UnaryStreamMultiCallable[
        HealthCheckRequest,
        HealthCheckResponse]


class HealthServicer(metaclass=ABCMeta):
    @abstractmethod
    def Check(self,
        request: HealthCheckRequest,
        context: ServicerContext,
    ) -> HealthCheckResponse: ...

    @abstractmethod
    def Watch(self,
        request: HealthCheckRequest,
        context: ServicerContext,
    ) -> Iterator[HealthCheckResponse]: ...


def add_HealthServicer_to_server(servicer: HealthServicer, server: Server) -> None: ...
