from celery import Celery

celery_master_app = Celery(
    "tasks",
    broker="redis://localhost:6380/1",
    backend="redis://localhost:6380/1",
    set_as_current=True,
    include=["my_task"]
)

# for inspect all node
running_client = celery_master_app.control.inspect()

# duplicate task check
def is_duplicate_task(task_name):
    """task is duplicate by name"""
    is_duplicate = False
    try:
        task_dict = running_client.active()
    except:
        is_duplicate = False
    finally:
        return is_duplicate