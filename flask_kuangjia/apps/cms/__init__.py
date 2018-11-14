from flask import Blueprint

cms_bp = Blueprint("cms", __name__)
from apps.cms.auth import *
