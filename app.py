from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from PIL import Image
import io
import stegano.lsb
import base64  # Base64 

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Flash message 
@app.route('/')
def index():
    return render_template('index.html', hidden_image=False)

@app.route('/about')
def about():
    return render_template('about.html')

# Contact Us Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Terms and Conditions Route
@app.route('/termcondition')
def terms():
    return render_template('termcondition.html')

@app.route('/hide', methods=['POST'])
def hide():
    if 'image' not in request.files or 'message' not in request.form or 'password' not in request.form:
        flash("⚠️ Please fill in all fields!", "error")
        return redirect(url_for('index'))

    image = request.files['image']
    message = request.form['message']
    password = request.form['password']

    img = Image.open(image)
    secret = stegano.lsb.hide(img, password + message)

    img_bytes = io.BytesIO()
    secret.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Hidden image को Base64 में कन्वर्ट करेंगे
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    return render_template('index.html', hidden_image=True, image_data=img_base64)

@app.route('/reveal', methods=['POST'])
def reveal():
    if 'image' not in request.files or 'password' not in request.form:
        flash("⚠️ Please fill in all fields!", "error")
        return redirect(url_for('index'))

    image = request.files['image']
    password = request.form['password']

    img = Image.open(image)

    try:
        hidden_msg = stegano.lsb.reveal(img)
        if hidden_msg.startswith(password):
            msg = hidden_msg[len(password):]
            flash(f"✅ Message Found: {msg}", "success")
        else:
            flash("❌ Incorrect password!", "error")
    except Exception:
        flash("⚠️ No hidden message found!", "error")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000) #for render
