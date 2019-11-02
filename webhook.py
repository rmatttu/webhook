# vim: fileencoding=utf-8

import argparse
import json
import logging.config
import requests
import sys
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('profile', help='Profile.')
    args = parser.parse_args()
    logging.config.fileConfig('log.ini')
    logger = logging.getLogger()
    configure = yaml.safe_load(open('conf/local.yml', 'r+'))
    conf = configure[args.profile]

    headers = {
        'Content-Type': conf['headers']['content-type'],
    }
    url = conf['url']
    logger.debug('data: {}'.format(conf['data']))
    response = requests.post(url, headers=headers, data=json.dumps(conf['data']))
    logger.debug(response)

if __name__ == '__main__':
    main()

