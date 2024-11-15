# QR Code Generator Web App 🚀

A modern, responsive web application for generating QR codes with multiple formats support. Built with Flask and modern web technologies.

## Features ✨

- **Multiple QR Code Types Support**:
  - 🔗 URL QR Codes
  - 📶 WiFi Network QR Codes
  - 📧 Email QR Codes
  - 📱 WhatsApp QR Codes
  - 📝 Text QR Codes

- **Modern UI/UX**:
  - 🌓 Dark/Light Theme Toggle
  - 📱 Responsive Design
  - 🎨 Clean and Modern Interface
  - ⚡ Real-time QR Code Generation

## Tech Stack 💻

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **QR Generation**: qrcode library
- **Icons**: Font Awesome

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure 📁

```
web/
├── static/
│   └── qrcodes/          # Generated QR codes storage
├── templates/
│   ├── forms/            # Form templates for different QR types
│   │   ├── url.html
│   │   ├── wifi.html
│   │   ├── email.html
│   │   └── text.html
│   └── qr.html          # Main template
├── app.py               # Flask application
└── requirements.txt     # Project dependencies
```

## Usage 📝

1. Select QR code type from the top navigation
2. Fill in the required information
3. Click "Generate QR Code"
4. Download or scan your QR code

## Features by Type 🎯

### URL QR Codes
- Direct link generation
- Automatic URL formatting
- Support for all URL types

### WiFi QR Codes
- Network name (SSID)
- Password protection
- Encryption type selection (WPA/WEP/None)
- Hidden network support

### Email QR Codes
- Email address
- Subject line
- Pre-written message
- Direct email client opening

### WhatsApp QR Codes
- Phone number with country code
- Pre-written message
- Direct WhatsApp opening

### Text QR Codes
- Plain text support
- Multi-line capability
- Unicode support

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 👏

- QR Code library: [python-qrcode](https://github.com/lincolnloop/python-qrcode)
- Font Awesome for icons
- Flask framework

## Support 🆘

For support, please open an issue in the repository or contact contact@abhiyanpa.in.

## Screenshots 📸

<img width="945" alt="{64CF6B54-1F74-4CB7-945C-6943E7FDBC9D}" src="https://github.com/user-attachments/assets/2353285f-0d52-40fa-a1e9-ea85c8930dad">

---
Made with ❤️ by Abhiyan P A
