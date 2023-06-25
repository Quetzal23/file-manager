import logging

from src.controller.application_controller import AplicationController


def main():
    # Instancia del controlador e iniciar la aplicacion
    application_controller = AplicationController()
    application_controller.run()


if __name__ == '__main__':
    # Configuración del registro de errores
    logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        main()
    except Exception as error:
        logging.exception(f"Exception: {error}")
