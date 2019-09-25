import os
import random
import time
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify

from task import BaseTask, async_result

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'



class LongTask(BaseTask):

    task_name = "LongTask"

    def run(self, task_id):
        """Background task that runs a long function with progress reports."""
        verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
        adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
        noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']

        message = ''
        total = random.randint(10, 50)

        for i in range(total):
            if not message or random.random() < 0.25:
                message = '{0} {1} {2}...'.format(random.choice(verb),
                                                  random.choice(adjective),
                                                  random.choice(noun))
            self.update_state(task_id=task_id, state='PROGRESS',
                              meta={'current': i, 'total': total,
                                    'status': message})
            time.sleep(1)
        
        self.update_state(task_id=task_id, state='FINISH', meta={'current':100, 'total': 100,'status': 'Task completed!', 'result':32})
        return



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/longtask', methods=['POST'])
def longtask():
    long_task = LongTask()
    task_id = long_task.delay()
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task_id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    info = async_result(task_id)
    print(info)
    if info.state == 'PENDING':
        response = {
            'state': info.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif info.state != 'FAILURE':
        response = {
            'state': info.state,
            'current': info.meta.get('current', 0),
            'total': info.meta.get('total', 1),
            'status': info.meta.get('status', '')
        }
        if 'result' in info.meta:
            response['result'] = info.meta['result']
    else:
        # something went wrong in the background job
        response = {
            'state': info.state,
            'current': 1,
            'total': 1,
            'status': str(info.meta),  # this is the exception raised
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
