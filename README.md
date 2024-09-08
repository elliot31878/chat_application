# Local Multi-User Chat Application with Python (Socket TCP)

This is a Python-based local chat application that uses TCP sockets to allow users to chat in pairs. The application is structured into two main packages: `client` and `server`. The client package implements the Observer pattern, and the application uses the Peewee ORM for database management and Colorama for colored console outputs.

![chatApp](https://user-images.githubusercontent.com/63051195/127721207-501444a9-4523-4695-9c38-942a838863f3.gif)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create and Activate a Virtual Environment](#step-2-create-and-activate-a-virtual-environment)
  - [Step 3: Install Dependencies](#step-3-install-dependencies)
  - [Step 4: Running the Application](#step-4-running-the-application)
- [Architecture](#architecture)
  - [Client-Server Model](#client-server-model)
  - [Observer Pattern](#observer-pattern)
- [Code Structure](#code-structure)
- [Development Guidelines](#development-guidelines)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Local Chat**: Users can chat with each other locally using TCP sockets.
- **Client-Server Architecture**: The application follows a client-server model where multiple clients can connect to a central server.
- **Observer Pattern**: The client package is implemented using the Observer pattern, promoting better design and separation of concerns.
- **Peewee ORM**: Used for managing the database and storing chat logs or user information.
- **Colorama**: Used to add color to the console output, making the chat more user-friendly.

## Installation

To set up the chat application, follow these steps.

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **PyCharm**: (Optional but recommended) Use PyCharm IDE for better development experience. You can download it from [jetbrains.com](https://www.jetbrains.com/pycharm/download/).

### Step 1: Clone the Repository

Start by cloning the GitHub repository:

```bash
git https://github.com/elliot31878/chat_application.git
cd chat_application
cd server
pip install -r requirements.txt
