from app.controller.main_controller import MainController


if __name__ == '__main__':
	try:
		controller = MainController()
		controller.run()
	except Exception as e:
		input(f"Exception: {e}\nPress any key for continue ...")
