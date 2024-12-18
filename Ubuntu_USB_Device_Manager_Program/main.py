from loguru import logger
from core.device_manager import USBDeviceManager
from ml_model.model import train_model
from gui.get_sudo_password import get_sudo_password_gui  # Import the GUI function

if __name__ == "__main__":
    # Prompt for the sudo password using the GUI
    sudo_password = get_sudo_password_gui()

    # If no password is provided, exit the program
    if not sudo_password:
        logger.error("No password provided. Exiting...")
        exit(1)

    # Train the model when the program starts
    train_model()

    # Start monitoring USB devices with the sudo password
    manager = USBDeviceManager(sudo_password)
    manager.monitor_usb_devices()
