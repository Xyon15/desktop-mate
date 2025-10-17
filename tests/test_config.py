"""
Unit tests for configuration manager.
"""

import pytest
import json
from pathlib import Path
from src.utils.config import Config


def test_config_default_values(tmp_path):
    """Test that default configuration is created correctly."""
    config_file = tmp_path / "test_config.json"
    config = Config(str(config_file))
    
    assert config.get("unity.host") == "127.0.0.1"
    assert config.get("unity.port") == 5555
    assert config.get("audio.sample_rate") == 44100


def test_config_save_load(tmp_path):
    """Test saving and loading configuration."""
    config_file = tmp_path / "test_config.json"
    
    # Create and modify config
    config1 = Config(str(config_file))
    config1.set("unity.port", 9999)
    config1.set("avatar.last_model", "test.vrm")
    config1.save()
    
    # Load in new instance
    config2 = Config(str(config_file))
    
    assert config2.get("unity.port") == 9999
    assert config2.get("avatar.last_model") == "test.vrm"


def test_config_nested_keys():
    """Test nested key access."""
    config = Config()
    config.set("deep.nested.key", "value")
    
    assert config.get("deep.nested.key") == "value"
    assert config.get("deep.nested.nonexistent", "default") == "default"
