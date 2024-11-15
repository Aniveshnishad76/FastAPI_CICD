# Define parameters for the group tasks
from celery import chord

from test import celery_master_app


@celery_master_app.task
def add(x, y):
    return x + y

@celery_master_app.task
def sum_results(results):
    return sum(results)

params = [(2, 3), (4, 5), (6, 7)]
group_tasks = [add.s(x, y) for x, y in params]
chord_result = chord(group_tasks)(sum_results.s())


result = chord_result.get()
print(f'Total sum: {result}')
