from app.controller.file_explorer_controller import FileExplorerController


if __name__ == '__main__':
	try:
		controller = FileExplorerController()
		controller.run()
		pass
	except Exception as e:
		input(f"Exception: {e}\nPress any key for continue ...")
