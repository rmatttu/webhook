# vim: fileencoding=utf-8

import argparse
import json
import logging.config
import requests
import sys
import yaml

def main():
    logging.config.fileConfig('log.ini')
    logger = logging.getLogger()
    conf = yaml.safe_load(open('conf/local.yml', 'r+'))
    # TODO: 実装する
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-m','--messages', action='append', help='Append messages.')
    # args = parser.parse_args()

    headers = {
        'Content-Type': conf['headers']['content-type'],
    }
    url = conf['url']
    logger.debug('data: {}'.format(conf['data']))
    response = requests.post(url, headers=headers, data=json.dumps(conf['data']))
    logger.debug(response)

if __name__ == '__main__':
    main()

