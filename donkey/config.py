
import os
import configparser

import donkey as dk

import keras

if int(keras.__version__.split('.')[0]) < 2:
    raise ImportError('You need keras version 2.0.0 or higher. Run "pip install keras --upgrade"')

config = configparser.ConfigParser()

my_path = os.path.expanduser('~/mydonkey/')
sessions_path = os.path.join(my_path, 'sessions')
models_path = os.path.join(my_path, 'models')
datasets_path = os.path.join(my_path, 'datasets')
results_path = os.path.join(my_path, 'results')


def parse_config(config_path):
    config_path = os.path.expanduser(config_path)
    config.read(config_path)

    cfg={}

    vehicle = config['vehicle']
    cfg['vehicle_id'] = vehicle.get('id')
    cfg['vehicle_loop_delay'] = vehicle.getfloat('loop_delay')

    camera = config['camera']
    cfg['camera_loop_delay'] = camera.getfloat('loop_delay')

    t_act = config['left_actuator']
    cfg['left_actuator_channel'] = t_act.getint('channel')
    cfg['left_actuator_min_pulse'] = t_act.getint('min_pulse')
    cfg['left_actuator_max_pulse'] = t_act.getint('max_pulse')
    cfg['left_actuator_zero_pulse'] = t_act.getint('zero_pulse')

    s_act = config['right_actuator']
    cfg['right_actuator_channel'] = t_act.getint('channel')
    cfg['right_actuator_min_pulse'] = t_act.getint('min_pulse')
    cfg['right_actuator_max_pulse'] = t_act.getint('max_pulse')
    cfg['right_actuator_zero_pulse'] = t_act.getint('zero_pulse')
    
    pilot = config['pilot']
    cfg['pilot_model_path'] = os.path.expanduser(pilot.get('model_path'))

    return cfg
