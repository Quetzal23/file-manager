from app.controller.explorer_controller import ExplorerController


if __name__ == '__main__':
	try:
		controller = ExplorerController()
		controller.run()
		pass
	except Exception as e:
		input(f"Exception: {e}\nPress any key for continue ...")
