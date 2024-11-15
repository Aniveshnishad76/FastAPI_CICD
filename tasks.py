"""task file"""
from test import celery_master_app

celery_master_app.autodiscover_tasks()
celery_master_app.conf.update(
    timezone='Asia/Kolkata',  # Set to IST timezone
    enable_utc=True,          # Enable UTC (recommended)
)

celery_master_app.conf.beat_schedule = {}