from src.app import create_app  # assuming you have a factory pattern

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
