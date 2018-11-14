from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModle(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer(), primary_key=True, autoincrement=True, comment="ID")
	is_delete = db.Column(db.Integer(), default=0, comment="是否删除")


from apps.models.seller import CmsSellerModel
