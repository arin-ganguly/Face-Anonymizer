# Face-Anonymizer-Using-Mediapipe

An open-source Python application that detects and anonymizes faces in images and videos using Mediapipe. 
This tool can blur or pixelate detected faces, making it useful for privacy protection in media content.

**Sample Output Video**
https://github.com/user-attachments/assets/8e34400c-53be-456a-be52-81f40b20d4fa

## 📌 Features

- ✅ Detect faces using MediaPipe
- ✅ Anonymize faces by:
  - Gaussian Blur
  - Pixelation
- ✅ Support for:
  - Static Images
  - Video Files
  - Webcam Feed

**🧠 How It Works**
- Face Detection: Uses MediaPipe's lightweight face detection model to identify faces in the frame.

- Anonymization: Each detected face region is either blurred using a Gaussian kernel or pixelated using resizing techniques.

- Output: Processed frames are displayed live and optionally saved.


