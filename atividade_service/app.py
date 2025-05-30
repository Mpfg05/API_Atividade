import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  
from atividade_service.controllers.atividade_controller import atividade_bp
from config import create_app


app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    app.run(host='localhost', port=5002)
