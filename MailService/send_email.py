from asgiref.sync import async_to_sync
from fastapi_mail import FastMail, MessageSchema, MessageType
from settings import conf, celery_task

async def send_email(message):
    fm = FastMail(conf)
    await fm.send_message(message)
    print('====== Mail - Celery Worker ..ing ======')

@celery_task.task
def send_email_async(subject: str, email_list: list, body: str):
    print('====== Mail - Celery Worker Start ======')
    message = MessageSchema(
        subject= subject,
        recipients= email_list,
        body= body,
        subtype=MessageType.plain,
    )
    async_to_sync(send_email)(message)
    print('====== Mail - Celery Worker Completed ======')
    return True

