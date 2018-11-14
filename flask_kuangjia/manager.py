from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app
from apps.models import db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
	print(app.url_map)
	manager.run()
