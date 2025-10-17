"""
Main application class using PySide6 (Qt).
Manages the GUI and coordinates with Unity via IPC.
"""

import sys
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QFileDialog, QMenuBar, QMenu
from PySide6.QtCore import Qt, QTimer

from ..ipc.unity_bridge import UnityBridge
from ..utils.config import Config

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.unity_bridge = UnityBridge()
        
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Desktop-Mate Control Panel")
        self.setGeometry(100, 100, 800, 600)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Header
        header = QLabel("Desktop-Mate Control Panel")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(header)
        
        # Unity connection status
        self.status_label = QLabel("Unity Status: Not Connected")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.connect_btn = QPushButton("Connect to Unity")
        self.connect_btn.clicked.connect(self.connect_unity)
        button_layout.addWidget(self.connect_btn)
        
        self.load_vrm_btn = QPushButton("Load VRM Model")
        self.load_vrm_btn.clicked.connect(self.load_vrm_model)
        self.load_vrm_btn.setEnabled(False)
        button_layout.addWidget(self.load_vrm_btn)
        
        layout.addLayout(button_layout)
        layout.addStretch()
        
        # Status timer
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(1000)  # Check every second
        
    def create_menu_bar(self):
        """Create the application menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        load_action = file_menu.addAction("Load VRM Model...")
        load_action.triggered.connect(self.load_vrm_model)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about)
        
    def connect_unity(self):
        """Connect to Unity application."""
        logger.info("Attempting to connect to Unity...")
        if self.unity_bridge.connect():
            self.status_label.setText("Unity Status: Connected ✓")
            self.load_vrm_btn.setEnabled(True)
            self.connect_btn.setEnabled(False)
            logger.info("Successfully connected to Unity")
        else:
            self.status_label.setText("Unity Status: Connection Failed ✗")
            logger.error("Failed to connect to Unity")
            
    def load_vrm_model(self):
        """Open file dialog to load a VRM model."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select VRM Model",
            "",
            "VRM Files (*.vrm);;All Files (*.*)"
        )
        
        if file_path:
            logger.info(f"Loading VRM model: {file_path}")
            self.unity_bridge.send_command("load_model", {"path": file_path})
            
    def update_status(self):
        """Update connection status."""
        if self.unity_bridge.is_connected():
            self.status_label.setText("Unity Status: Connected ✓")
        else:
            if self.connect_btn.isEnabled() == False:
                self.status_label.setText("Unity Status: Disconnected ✗")
                self.connect_btn.setEnabled(True)
                self.load_vrm_btn.setEnabled(False)
                
    def show_about(self):
        """Show about dialog."""
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.about(
            self,
            "About Desktop-Mate",
            "Desktop-Mate v0.1.0\n\n"
            "Interactive VRM Desktop Companion\n"
            "Hybrid Unity + Python Application\n\n"
            "© 2025 Xyon15"
        )
        
    def closeEvent(self, event):
        """Handle window close event."""
        logger.info("Application closing...")
        self.unity_bridge.disconnect()
        self.config.save()
        event.accept()


class DesktopMateApp:
    """Main application wrapper."""
    
    def __init__(self, argv):
        """Initialize the application.
        
        Args:
            argv: Command line arguments
        """
        self.app = QApplication(argv)
        self.app.setApplicationName("Desktop-Mate")
        self.app.setOrganizationName("Xyon15")
        
        self.main_window = MainWindow()
        
    def run(self):
        """Run the application.
        
        Returns:
            Exit code
        """
        self.main_window.show()
        return self.app.exec()
