from flask import Flask


def register_db(app):
	from apps.models import db
	db.init_app(app)


def register_bp(app):
	from apps.cms import cms_bp
	app.register_blueprint(cms_bp)


def create_app():
	app = Flask(__name__)
	app.config.from_object('apps.setting.DevConfig')
	# 注册数据库
	register_db(app)
	# 注册蓝图
	register_bp(app)
	return app
