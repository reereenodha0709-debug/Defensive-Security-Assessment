from flask import Flask, request, render_template_string

app = Flask(__name__)

# Demo-only secret key. Replace it before using sessions in any real application.
app.config["SECRET_KEY"] = "change-this-demo-key"

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'; object-src 'none'; frame-ancestors 'none'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    # HSTS is intentionally not enabled for this HTTP-only localhost demo.
    return response

PAGE = """
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Local Security Demo</title></head>
<body>
  <h1>Local Security Demo</h1>
  <p>This is a small application for authorized defensive testing.</p>
  <form method="post">
    <label for="message">Enter a short message:</label>
    <input id="message" name="message" maxlength="100">
    <button type="submit">Submit</button>
  </form>
  {% if message %}<p>Received: {{ message }}</p>{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        message = request.form.get("message", "")[:100]
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    # Localhost only: do not change the host to 0.0.0.0 for this exercise.
    app.run(host="127.0.0.1", port=5000, debug=False)
