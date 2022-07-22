from __future__ import annotations

from dataclasses import dataclass


# Base exception for all package
class CheckerException(Exception):
    pass


# All deadlines and conf exceptions
class BadConfig(CheckerException):
    pass


class BadTaskConfig(BadConfig):
    pass


class BadGroupConfig(BadConfig):
    pass


# Tests exceptions
class TesterException(CheckerException):
    pass


class TesterNotImplemented(CheckerException):
    pass


class TaskTesterException(TesterException):
    pass


class TaskTesterTestConfigException(TaskTesterException):
    pass


# Tests exceptions (with output)
@dataclass
class RunFailedError(TesterException):
    msg: str = ''
    output: str | None = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.msg}'


class ExecutionFailedError(RunFailedError):
    pass


class BuildFailedError(RunFailedError):
    pass


class RegexpCheckFailedError(RunFailedError):
    pass


class TestsFailedError(RunFailedError):
    pass


# Manytask exceptions
class ManytaskRequestFailedError(CheckerException):
    pass


class PushFailedError(ManytaskRequestFailedError):
    pass


class GetFailedError(ManytaskRequestFailedError):
    pass
