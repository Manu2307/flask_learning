from app import create_app
from config import DevConfig

cdp_app = create_app(DevConfig)


@cdp_app.route("/welcome", methods=["GET"])
def welcome_method():
    return "Hello flask learners"


if __name__ == "__main__":
    cdp_app.run()
