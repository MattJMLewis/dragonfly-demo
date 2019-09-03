from string import Template

import MySQLdb.cursors
import click

from config import DATABASE
from dragonfly.db.database_migrator import DatabaseMigrator

templates = {}

templates['models'] = Template('''from dragonfly.db.models.model import Model


class $name(Model):
    pass

''')

templates['middleware'] = Template('''
class $name:

    actions = []
    
    def before(self):
        pass

    def after(self):
        pass

''')

templates['controllers'] = Template('''from dragonfly.controller import Controller


class $name(Controller):
    pass

''')


@click.group()
def cli():
    pass


# generate commands
@cli.command()
@click.option('--type', type=click.Choice(['model', 'middleware', 'controller']),
              help="The type of file you want to generate.")
@click.argument('name', type=click.STRING)
def generate(type, name):
    """
    Generate the desired file type. The files should be named according to the PEP 8 naming scheme. Please note that the
    file names are converted to camel case for the class names.
    """
    old_type = type
    if type != 'middleware':
        type += 's'

    with open(f"{type}/{name}.py", 'w') as file:
        file.writelines(templates[type].substitute(name=''.join(x.capitalize() or '_' for x in name.split('_'))))

    click.secho(f"Successfully created {old_type}!", fg="green")


@cli.command()
def migrate():
    """
    Generate the SQL to create the tables for all user created models and run it.
    """
    dbm = DatabaseMigrator()

    db = MySQLdb.connect(**DATABASE, cursorclass=MySQLdb.cursors.DictCursor)
    cursor = db.cursor()

    for key, value in dbm.tables.items():
        click.secho(f"Migrating {key} model", fg="blue")
        cursor.execute(value)
        db.commit()
        click.secho(f"Migrated {key} successfully!", fg="green")

    cursor.close()
    db.close()


if __name__ == '__main__':
    cli()
