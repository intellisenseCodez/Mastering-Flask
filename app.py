from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)


@app.get("/user-info")
def form():
    message = request.args.get('message')
    return render_template("form.html", message=message)


@app.post("/user-info")
def formRequest():
    data = request.form
    # throw 401 if any data is missing
    if not data.get('firstname') or not data.get("lastname") or not data.get("country"):
        abort(401)

    message = f"{data.get('firstname')} {data.get('lastname')} lives in {data.get('country')}"
    return redirect(f"{url_for('form')}?message={message}")



if __name__ == "__main__":
    app.run(debug = True)