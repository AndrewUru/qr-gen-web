from flask import Flask, render_template, request, url_for, redirect
import qrcode
from datetime import datetime
import os
import string
import random
import urllib.parse

app = Flask(__name__)
app.config['SECRET_KEY'] = '49d81e41c1c6a6d0530bb25582e9402319e7b99d95934b6cda05c39029f3b3fd'
app.config['UPLOAD_FOLDER'] = 'static/qrcodes'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def generate_qr(data, qr_type='text'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = f'qr_{timestamp}_{random_string}.png'
    
    # Process data based on QR type
    if qr_type == 'url' and not data.startswith(('http://', 'https://')):
        data = 'https://' + data
    elif qr_type == 'email':
        # Don't modify mailto: links
        if not data.startswith('mailto:'):
            data = f'mailto:{data}'
    elif qr_type == 'wifi':
        # Don't modify WIFI: data
        if not data.startswith('WIFI:'):
            data = f'WIFI:{data}'
    elif qr_type == 'whatsapp':
        # Don't modify whatsapp links
        if not data.startswith('https://wa.me/'):
            data = f'https://wa.me/{data}'
    # For text type, use data as-is
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img.save(file_path)
    
    return filename

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return redirect(url_for('url_qr'))

@app.route('/url', methods=['GET', 'POST'])
def url_qr():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            filename = generate_qr(url, qr_type='url')
            return render_template('qr.html', 
                                page='url',
                                qr_code=url_for('static', filename=f'qrcodes/{filename}'),
                                original_url=url)
    return render_template('qr.html', page='url')

@app.route('/email', methods=['GET', 'POST'])
def email_qr():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject', '')
        message = request.form.get('message', '')
        
        if email:
            # Format mailto string
            mailto_string = f"mailto:{email}"
            params = []
            if subject:
                params.append(f"subject={urllib.parse.quote(subject)}")
            if message:
                params.append(f"body={urllib.parse.quote(message)}")
            if params:
                mailto_string += "?" + "&".join(params)
                
            filename = generate_qr(mailto_string, qr_type='email')
            return render_template('qr.html', 
                                page='email',
                                qr_code=url_for('static', filename=f'qrcodes/{filename}'),
                                original_url=f"Email: {email}")
    return render_template('qr.html', page='email')

@app.route('/text', methods=['GET', 'POST'])
def text_qr():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            filename = generate_qr(text, qr_type='text')
            display_text = text if len(text) < 50 else text[:47] + "..."
            return render_template('qr.html', 
                                page='text',
                                qr_code=url_for('static', filename=f'qrcodes/{filename}'),
                                original_url=f"Text: {display_text}")
    return render_template('qr.html', page='text')

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp_qr():
    if request.method == 'POST':
        country_code = request.form.get('country_code', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '')
        
        if country_code and phone:
            full_phone = f"{country_code}{phone.replace(' ', '')}"
            whatsapp_data = full_phone
            if message:
                whatsapp_data += f"?text={urllib.parse.quote(message)}"
            
            filename = generate_qr(whatsapp_data, qr_type='whatsapp')
            return render_template('qr.html', 
                                page='whatsapp',
                                qr_code=url_for('static', filename=f'qrcodes/{filename}'),
                                original_url=f"WhatsApp: +{country_code} {phone}")
    return render_template('qr.html', page='whatsapp')

@app.route('/wifi', methods=['GET', 'POST'])
def wifi_qr():
    if request.method == 'POST':
        ssid = request.form.get('ssid')
        password = request.form.get('password', '')
        encryption = request.form.get('encryption', 'WPA')
        hidden = request.form.get('hidden') == 'on'
        
        if ssid:
            # Format WiFi string according to standard
            wifi_string = f"WIFI:S:{ssid};T:{encryption};P:{password}"
            if hidden:
                wifi_string += ";H:true"
            wifi_string += ";;"
            
            filename = generate_qr(wifi_string, qr_type='wifi')
            return render_template('qr.html', 
                                page='wifi',
                                qr_code=url_for('static', filename=f'qrcodes/{filename}'),
                                original_url=f"WiFi Network: {ssid}")
    return render_template('qr.html', page='wifi')

if __name__ == '__main__':
    app.run(debug=True)