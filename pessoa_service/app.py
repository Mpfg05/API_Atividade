import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config import create_app
from atividade_service.controllers.atividade_controller import atividade_bp
from controllers.pessoa_controller import pessoa_bp

app = create_app()


app.register_blueprint(atividade_bp, url_prefix='/atividades')
app.register_blueprint(pessoa_bp, url_prefix='/pessoas')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
