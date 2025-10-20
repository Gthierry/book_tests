from app import create_app

# Créer une instance Flask configurée avec les routes
app = create_app()

if __name__ == "__main__":
	app.run(debug=True)