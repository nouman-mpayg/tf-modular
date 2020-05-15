from mpayg_iot.sim_management import base


class SIMInfoService(base.SIMInfoService):

    #
    # Mocked implementation of SIM information service
    #

    @classmethod
    def __init__(self):
        pass

    @classmethod
    def get_sim_info(cls):
        pass
