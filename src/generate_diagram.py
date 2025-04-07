from eralchemy2 import render_er
from models import db  # Importa la instancia de SQLAlchemy (db)

# Genera el diagrama usando la metadata de tu base de datos
render_er(db.Model, 'diagram.png')
