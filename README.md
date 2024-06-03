# Project Arte

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Arte is a personal AI assistant using speech recognition and natural language processing. It manages schedules, sends emails, and provides voice guidance. With cutting-edge technology, Arte enhances productivity and integrates seamlessly into daily tasks, making life more organized and efficient.

## Features

- Voice recognition
- Natural language processing
- Schedule management
- Email sending
- Voice guidance

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/cogito21g/Arte.git
    cd arte
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv arte_env
    source arte_env/bin/activate  # macOS/Linux
    .\arte_env\Scripts\activate   # Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    pip install pyobjc  # For macOS users
    ```

4. Download NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```


## Usage

1. Run the main script:
    ```sh
    cd src
    python main.py
    ```

2. Follow the voice instructions to interact with Arte. Here are some example commands:

- **Add event**: "Add event"
  - Arte: "Please tell me the date of the event."
  - User: "2024-06-15"
  - Arte: "Please tell me the event details."
  - User: "Doctor's appointment"

- **Show events**: "Show events"
  - Arte: "Please tell me the date of the events you want to see."
  - User: "2024-06-15"

- **Send email**: "Send email"
  - Arte: "Please tell me the recipient's email address."
  - User: "example@example.com"
  - Arte: "Please tell me the subject of the email."
  - User: "Meeting Schedule"
  - Arte: "Please tell me the body of the email."
  - User: "The meeting is scheduled for 3 PM tomorrow."

- **Stop**: "Stop"

## Project Structure

```
arte/
│
├── LICENSE
├── README.md
├── requirements.txt
├── data/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── speech_recognition.py
│   ├── speech_synthesis.py
│   ├── nlp.py
│   ├── scheduler.py
│   └── email_manager.py
└── tests/
    ├── __init__.py
    └── test_arte.py
```

- **README.md**: Project overview and instructions.
- **requirements.txt**: List of required Python packages.
- **data/**: Directory for data files.
- **notebooks/**: Directory for Jupyter notebooks.
- **src/**: Directory for source code.
  - **main.py**: Main script to run Arte.
  - **speech_recognition_module.py**: Module for speech recognition.
  - **speech_synthesis.py**: Module for speech synthesis.
  - **nlp.py**: Module for natural language processing.
  - **scheduler.py**: Module for schedule management.
  - **email_manager.py**: Module for email management.
- **tests/**: Directory for test scripts.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.