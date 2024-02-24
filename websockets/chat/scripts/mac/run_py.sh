# chmod +x run_py.sh
# ./run_py.sh

# Create a virtual environment
virtualenv ./backend/python/venv

# Activate the virtual environment
source ./backend/python/venv/bin/activate

# Install dependencies
pip install -r ./backend/python/requirements.txt

# Run the Python script
python backend/python/main.py