import yaml
import os

from conftest import BASE_DIR


def build_address_func():
    with open(BASE_DIR + '/data/adds_data.yaml',encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data_list = []
        for i in data:
            data_list.append((i.get('name'),i.get('phone')))
        print(data_list)
        return data_list
