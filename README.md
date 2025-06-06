# NoteApp

A simple Django REST API for managing notes and tags.

---

## Features

- Create, retrieve, update, and delete notes
- Create and list tags
- Assign multiple tags to notes
- Retrieve a tag along with all notes associated with it

---

## Getting Started

### Prerequisites

- Python 3.10.7
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create and activate a virtual environment (recommended)**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```