# ISCS 30.23 - Containerizing Applications

## Original Members & GitHub Handles
- **Louis G. Binwag III** - [louis-uwie](https://github.com/louis-uwie)  
- **Jean Maximus C. Cacacho** - [jeanmaxcacacho](https://github.com/jeanmaxcacacho)  
- **Paco Antonio V. Zabala** - [Pacozabala](https://github.com/Pacozabala)  
- **Ysaac Rainier Mesa** - [Ysaac12](https://github.com/Ysaac12)  

## Repository Update (As of Feb 2, 2025)
@louis-uwie is repurposing this repository for **ISCS 30.23 - Containerizing Applications**.

## Original Members & GitHub Handles
- ***Ciana Magtipon*** - [cianamagtipon](https://github.com/cianamagtipon)

---

## Project Setup

### 1. Clone the Repository
Clone the repository into your designated directory:
```bash
git clone <repository_url>
```

Move into the project folder:
```bash
cd repository
```

### 2. Create & Activate a Virtual Environment
Create a virtual environment:
```bash
python -m venv myenv
```

Activate the virtual environment:
- **Windows:**
  ```bash
  myenv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source myenv/bin/activate
  ```

### 3. Install Dependencies
Upgrade `pip` and install project dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply Migrations & Run Development Server
Run database migrations:
```bash
python manage.py migrate  # Applying necessary migrations
```

Start the development server:
```bash
python manage.py runserver
```

### Documentation
For more details, refer to the official Django documentation:  
[Django Docs](https://docs.djangoproject.com/en/5.1/)
