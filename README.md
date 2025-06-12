### 📌 **Steganography Web App – README**

---

#### 💡 **Overview**
The **`Steganography-Mssage-Hiding`** project is a web-based steganography application that allows you to hide and extract secret messages in images with password protection. The purpose of this app is to enhance data security by enabling the concealment and secure sharing of sensitive information.

---

#### 🔥 **Features**
- **Image Steganography:** Hide secret messages inside images without altering their visual appearance.  
- **Password Protection:** Add a password while encoding and use the same password to decode the message.  
- **Decryption:** Extract hidden messages from steganographic images only with the correct password.  
- **User-Friendly Interface:** Simple and intuitive web interface for easy usage.  
- **Security-Focused:** Designed with basic cryptographic principles to ensure message integrity.  
- **Built With:** Flask (Python), HTML, CSS, and JavaScript.  

---

#### 🚀 **How It Works**
1. **Encoding:**  
   - Upload an image.  
   - Enter the secret message and set a password.  
   - The app embeds the message into the image and provides a downloadable stego image.  

2. **Decoding:**  
   - Upload the stego image.  
   - Enter the password used during encoding.  
   - The app extracts and displays the hidden message only if the correct password is entered.  

---

#### ⚙️ **Tech Stack**
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Steganography Library:** stegano 

---

#### 🛠️ **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/ShriKant114/Steganography-Mssage-Hiding/
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Modify `app.py` before running:
   ```python
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=10000)  # To run on localhost with custom port
   ```

4. Run the server:
   ```bash
   python app.py
   ```
5. Open the web app in your browser:
   ```
   http://localhost:10000
   ```

---

#### 🛡️ **Security Considerations**
- The app uses **LSB (Least Significant Bit)** steganography, making the hidden data less detectable.  
- **Password protection** ensures that only authorized users can extract hidden messages.  
- Use larger images to improve security and reduce the chances of visual artifacts.  

---

✅ **Contributions and Feedback** are welcome! 🎯
