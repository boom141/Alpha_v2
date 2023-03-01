from webApplication import init_app

sio, app = init_app()

@app.route('/test')
def index():
    return 'PERSONAL PROJECT: Al-PROCEDURE WEB APPLICATION || NIJIDEV'


if __name__ == '__main__':
   sio.run(app, debug=True)