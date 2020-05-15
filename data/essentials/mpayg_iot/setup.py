#!/usr/bin/env python

from setuptools import setup

setup(name='mpayg_iot',
      version='0.1',
      description='M-PAYG\'s IoT related packages',
      author='Kashif Masood',
      author_email='v-kashif@mpayg.com',
      license='Proprietary',
      long_description=open('README').read(),
      install_requires=[
            'xmltodict',
      ],
      packages=[
            'mpayg_iot',
            'mpayg_iot.device_messaging',
            'mpayg_iot.event_parser',
            'mpayg_iot.sim_management',
            'mpayg_iot.m2m_sms',
            'mpayg_iot.m2m_sms.mo',
            'mpayg_iot.m2m_sms.mt',
            'mpayg_iot.services',
      ],
)
