# Dual-Page Text Recognition

## Overview
This project focuses on recognizing and extracting text from dual-page document images, such as scanned books or magazines. The system processes both pages simultaneously to improve accuracy and efficiency.

## Features
- Dual-page text recognition using advanced OCR techniques.
- Preprocessing for image enhancement and noise reduction.
- Support for multiple languages.
- Export recognized text in various formats (e.g., plain text, JSON).

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Dual-Page Text Recognition
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your dual-page images in the `input` folder.
2. Run the recognition script:
   ```bash
   python recognize.py
   ```
3. The output will be saved in the `output` folder.

## Folder Structure
```
Dual-Page Text Recognition/
├── input/          # Folder for input images
├── output/         # Folder for output results
├── src/            # Source code
├── tests/          # Test cases
├── requirements.txt # Python dependencies
└── README.md       # Project documentation
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
