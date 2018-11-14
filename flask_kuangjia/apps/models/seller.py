from apps.models import BaseModle, db


class CmsSellerModel(BaseModle):
	__tablename__ = "seller"
	username = db.Column(db.String(20), nullable=False, comment="用户名")
	password = db.Column(db.String(128), nullable=False, comment="用户密码")
