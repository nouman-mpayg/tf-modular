from abc import ABCMeta, abstractmethod
from mpayg_domain.hub import base as hub_base


class SIMInfoService(metaclass=ABCMeta):

    #
    # Parent class which will be implemented by provider specific modules
    #

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_sim_info(cls):
        pass


class SIMInfoHelper(metaclass=ABCMeta):

    @classmethod
    def __init__(self):
        pass

    @abstractmethod
    def prepare_info(cls, api_response) -> hub_base.Hub:
        pass
