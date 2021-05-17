from covid19_stat import app, create_app


if __name__ == '__main__':
    create_app()
    app.run(host='10.8.0.1', port=8000, debug=True)