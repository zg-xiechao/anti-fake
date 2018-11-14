import os


class BaseConfig(object):
	DEBUG = True


def get_prj_dir():
	return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DevConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = "sqlite:///{}/devcms.db".format(get_prj_dir())
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductConfig(BaseConfig):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:psd123456@47.104.252.32/homework"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
