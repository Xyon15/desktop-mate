"""
Main application class using PySide6 (Qt).
Manages the GUI and coordinates with Unity via IPC.
"""

import sys
import logging
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QMenuBar, QMenu,
    QTabWidget, QSlider, QGroupBox
)
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
        self.setGeometry(100, 100, 900, 700)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Central widget with tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Header
        header = QLabel("Desktop-Mate Control Panel")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(header)
        
        # Unity connection status
        self.status_label = QLabel("Unity Status: Not Connected")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Tab widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Create tabs
        self.create_connection_tab()
        self.create_expressions_tab()
        
        # Status timer
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(1000)  # Check every second

    def create_connection_tab(self):
        """Create the Unity connection tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
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
        
        self.tabs.addTab(tab, "Connection")

    def create_expressions_tab(self):
        """Create the facial expressions tab with sliders."""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Group box for expressions
        expressions_group = QGroupBox("Facial Expressions")
        expressions_layout = QVBoxLayout()
        expressions_group.setLayout(expressions_layout)
        
        # Dictionary to store sliders and labels
        self.expression_sliders = {}
        self.expression_labels = {}
        
        # List of expressions with emoji and names
        expressions = [
            ("joy", "😊 Joy (Joyeux)"),
            ("angry", "😠 Angry (En colère)"),
            ("sorrow", "😢 Sorrow (Triste)"),
            ("surprised", "😲 Surprised (Surpris)"),
            ("fun", "😄 Fun (Amusé)")
        ]
        
        # Create slider for each expression
        for expr_id, expr_label in expressions:
            # Container for this expression
            expr_container = QWidget()
            expr_layout = QVBoxLayout()
            expr_container.setLayout(expr_layout)
            
            # Label with current value
            value_label = QLabel(f"{expr_label}: 0%")
            value_label.setStyleSheet("font-size: 14px; font-weight: bold;")
            expr_layout.addWidget(value_label)
            
            # Slider
            slider = QSlider(Qt.Orientation.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(0)
            slider.setTickPosition(QSlider.TickPosition.TicksBelow)
            slider.setTickInterval(10)
            
            # Connect slider to handler
            slider.valueChanged.connect(
                lambda value, eid=expr_id, lbl=value_label, orig_text=expr_label: 
                    self.on_expression_slider_change(eid, lbl, orig_text, value)
            )
            
            expr_layout.addWidget(slider)
            
            # Store references
            self.expression_sliders[expr_id] = slider
            self.expression_labels[expr_id] = value_label
            
            expressions_layout.addWidget(expr_container)
        
        layout.addWidget(expressions_group)
        
        # Reset button
        reset_layout = QHBoxLayout()
        reset_btn = QPushButton("Reset All Expressions")
        reset_btn.setStyleSheet("font-size: 14px; padding: 10px;")
        reset_btn.clicked.connect(self.reset_all_expressions)
        reset_layout.addStretch()
        reset_layout.addWidget(reset_btn)
        reset_layout.addStretch()
        layout.addLayout(reset_layout)
        
        layout.addStretch()
        
        self.tabs.addTab(tab, "Expressions")

    def on_expression_slider_change(self, expression_id: str, label: QLabel, 
                                    original_text: str, value: int):
        """Handle expression slider value change.
        
        Args:
            expression_id: ID of the expression (e.g., "joy")
            label: QLabel to update with new value
            original_text: Original label text with emoji
            value: Slider value (0-100)
        """
        # Update label with current value
        label.setText(f"{original_text}: {value}%")
        
        # Send to Unity if connected
        if self.unity_bridge.is_connected():
            # Convert 0-100 to 0.0-1.0
            normalized_value = value / 100.0
            self.unity_bridge.set_expression(expression_id, normalized_value)
            logger.debug(f"Set expression {expression_id} to {normalized_value:.2f}")

    def reset_all_expressions(self):
        """Reset all expressions to neutral."""
        # Reset all sliders to 0
        for slider in self.expression_sliders.values():
            slider.setValue(0)
        
        # Send reset command to Unity
        if self.unity_bridge.is_connected():
            self.unity_bridge.reset_expressions()
            logger.info("Reset all expressions")

        
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
