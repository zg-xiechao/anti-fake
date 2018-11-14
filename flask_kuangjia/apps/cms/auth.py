from apps.cms import cms_bp


@cms_bp.route("/", endpoint="main")
def main():
	return "ok"
