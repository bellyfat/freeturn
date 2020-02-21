import functools
import os
import sys

import dotenv
import invoke

dotenv.load_dotenv()


# https://github.com/pyinvoke/invoke/issues/555
def configure_django():
    from django.db.backends.base.base import BaseDatabaseWrapper
    BaseDatabaseWrapper.queries_limit = 50000
    from django.core.wsgi import get_wsgi_application
    PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rms.settings")
    sys.path.append(PROJECT_DIR)
    get_wsgi_application()


def with_django(func):
    @functools.wraps(func)
    def _inner(context, *args, **kwargs):
        configure_django()
        func(context, *args, **kwargs)

    return _inner


@invoke.task
def deploy(context, repo=True, db_backup=True):
    if db_backup:
        context.run("heroku pg:backups:capture ")
    if repo:
        context.run("git push origin && git push heroku develop:master")
    else:
        context.run("git push heroku develop:master")


@invoke.task
def sync_production_db(ctx, backup=True):
    # if backup:
    #     ctx.run("heroku pg:backups:capture")
    # ctx.run("heroku pg:backups:download")
    database_url = os.environ['DATABASE_URL']
    ctx.run(f"pg_restore --verbose --clean --no-acl --no-owner --dbname={database_url} latest.dump")
    os.remove("latest.dump")


@invoke.task
def sync_production_s3(ctx):
    from portfolio.settings import production, production_local
    ctx.run(
        f"aws s3 sync --acl public-read s3://{production.AWS_STORAGE_BUCKET_NAME} "
        f"s3://{production_local.AWS_STORAGE_BUCKET_NAME}"
    )


@invoke.task
@with_django
def mail(context):
    from crm.gmail_utils import sync
    sync()


@invoke.task
@with_django
def create_admin(ctx):
    """Creates admin for local instance"""
    assert getattr(ctx, 'host', 'localhost') == 'localhost'
    from django.contrib.auth import get_user_model

    if not get_user_model().objects.filter(username='admin').exists():
        user = get_user_model().objects.create_superuser(
            'admin', 'admin@admin.com', 'admin'
        )
        print(f"Created user {user} with password 'admin'")


@invoke.task
def fill(context, migrate=False):
    configure_django()
    if migrate:
        context.run('rm db.sqlite3')
        context.run('PYTHONUNBUFFERED=1 ./manage.py migrate')
        create_admin(context)
    from initial_filling import fill
    fill()
