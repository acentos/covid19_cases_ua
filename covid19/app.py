from covid19_stat import app, create_app


if __name__ == '__main__':
    create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)