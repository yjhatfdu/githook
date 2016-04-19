from flask import *
import os
import json
import logging

with open('config.json') as fp:
    config = json.load(fp)
logger = logging.getLogger('githook')
logger.setLevel(logging.INFO)

fh = logging.FileHandler(config['log'])

fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

app = Flask(__name__)


@app.route(config['path']+'<string:hook>',methods=['POST'])
def gothook(hook):
    try:
        body=request.json()
        branch=body['ref'].split('/')[-1]
        if branch!=u'master':
            return  ''
        logger.info('Get githook from:'+request.remote_addr)
        detail = config['hooks'][hook]
        os.system(detail['commands'])
        logger.info('Finish execute')
        return ''
    except:
        logger.info('Error hookname:' + hook)
        return abort(404)


if __name__=='__main__':
    app.run(config['address'], port=config['port'])
logger.info('git hook initialized')
