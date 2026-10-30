python -m venv .venv
source .venv/bin/activate
pip install colorama
pip freeze > requirements.txt
echo ".venv/" >> .gitignore