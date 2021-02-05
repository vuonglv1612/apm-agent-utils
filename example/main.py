from example.app import app
from example.controllers import test_controller


@app.route("/")
def main():
    return test_controller()


if __name__ == "__main__":
    app.run(debug=True)