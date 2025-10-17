"""
Unit tests for Unity bridge IPC.
"""

import pytest
from unittest.mock import Mock, patch
from src.ipc.unity_bridge import UnityBridge


def test_unity_bridge_initialization():
    """Test UnityBridge initialization."""
    bridge = UnityBridge()
    
    assert bridge.host == "127.0.0.1"
    assert bridge.port == 5555
    assert bridge.connected is False
    assert bridge.socket is None


def test_unity_bridge_custom_params():
    """Test UnityBridge with custom parameters."""
    bridge = UnityBridge(host="localhost", port=8888)
    
    assert bridge.host == "localhost"
    assert bridge.port == 8888


@patch('socket.socket')
def test_connect_success(mock_socket):
    """Test successful connection to Unity."""
    bridge = UnityBridge()
    mock_socket_instance = Mock()
    mock_socket.return_value = mock_socket_instance
    
    result = bridge.connect()
    
    assert result is True
    assert bridge.connected is True
    mock_socket_instance.connect.assert_called_once()


def test_disconnect():
    """Test disconnection from Unity."""
    bridge = UnityBridge()
    bridge.connected = True
    mock_socket = Mock()
    bridge.socket = mock_socket
    bridge.running = False  # Prevent thread from starting
    
    bridge.disconnect()
    
    assert bridge.connected is False
    assert bridge.socket is None


def test_send_command_not_connected():
    """Test sending command when not connected."""
    bridge = UnityBridge()
    
    result = bridge.send_command("test_command")
    
    assert result is False
