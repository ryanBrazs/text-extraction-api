import os
from app import create_app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)