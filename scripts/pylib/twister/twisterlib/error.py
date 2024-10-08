# vim: set syntax=python ts=4 :
#
# Copyright (c) 2018-2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

class TwisterException(Exception):
    pass


class TwisterRuntimeError(TwisterException):
    pass


class ConfigurationError(TwisterException):
    def __init__(self, cfile, message):
        TwisterException.__init__(self, str(cfile) + ": " + message)


class BuildError(TwisterException):
    pass


class ExecutionError(TwisterException):
    pass


class StatusAttributeError(TwisterException):
    def __init__(self, cls : type, value):
        msg = f'{cls.__name__} assigned status {value}, which could not be cast to a TwisterStatus.'
        super().__init__(msg)
