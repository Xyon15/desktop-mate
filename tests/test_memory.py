"""
Tests Unitaires - Système de Mémoire Conversationnelle

Tests pour src/ai/memory.py
"""

import pytest
import os
import tempfile
from src.ai.memory import ConversationMemory


@pytest.fixture
def temp_db():
    """Fixture pour créer une base de données temporaire pour les tests"""
    # Créer un fichier temporaire
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    
    # Créer l'instance de mémoire
    memory = ConversationMemory(path)
    
    yield memory
    
    # Nettoyer après les tests
    if os.path.exists(path):
        os.unlink(path)


def test_save_and_retrieve_interaction(temp_db):
    """Test sauvegarde et récupération d'une interaction"""
    memory = temp_db
    
    # Sauvegarder une interaction
    interaction_id = memory.save_interaction(
        user_id="test_user_1",
        source="desktop",
        user_input="Bonjour !",
        bot_response="Salut !",
        emotion="joy"
    )
    
    assert interaction_id > 0
    
    # Récupérer l'historique
    history = memory.get_history("test_user_1", limit=10)
    
    assert len(history) == 1
    assert history[0]['user_input'] == "Bonjour !"
    assert history[0]['bot_response'] == "Salut !"
    assert history[0]['emotion'] == "joy"


def test_multiple_interactions(temp_db):
    """Test de plusieurs interactions pour un utilisateur"""
    memory = temp_db
    
    # Sauvegarder plusieurs interactions
    for i in range(5):
        memory.save_interaction(
            user_id="test_user_2",
            source="desktop",
            user_input=f"Message {i}",
            bot_response=f"Réponse {i}",
            emotion="neutral"
        )
    
    # Récupérer l'historique complet
    history = memory.get_history("test_user_2", limit=10)
    
    assert len(history) == 5
    # Vérifier que toutes les interactions sont présentes
    messages = [h['user_input'] for h in history]
    assert "Message 0" in messages
    assert "Message 4" in messages


def test_history_limit(temp_db):
    """Test de la limitation du nombre d'interactions récupérées"""
    memory = temp_db
    
    # Sauvegarder 10 interactions
    for i in range(10):
        memory.save_interaction(
            user_id="test_user_3",
            source="desktop",
            user_input=f"Message {i}",
            bot_response=f"Réponse {i}"
        )
    
    # Récupérer seulement les 5 plus récentes
    history = memory.get_history("test_user_3", limit=5)
    
    assert len(history) == 5
    # Vérifier que la limite est respectée (on récupère bien 5 interactions)
    # Les messages exacts peuvent varier selon le timestamp
    assert all('Message' in h['user_input'] for h in history)


def test_filter_by_source(temp_db):
    """Test du filtrage par source (desktop vs discord)"""
    memory = temp_db
    
    # Sauvegarder des interactions depuis 2 sources
    memory.save_interaction("test_user_4", "desktop", "Message desktop 1", "Réponse 1")
    memory.save_interaction("test_user_4", "discord", "Message discord 1", "Réponse 2")
    memory.save_interaction("test_user_4", "desktop", "Message desktop 2", "Réponse 3")
    
    # Récupérer seulement les interactions desktop
    history_desktop = memory.get_history("test_user_4", limit=10, source="desktop")
    assert len(history_desktop) == 2
    
    # Récupérer seulement les interactions discord
    history_discord = memory.get_history("test_user_4", limit=10, source="discord")
    assert len(history_discord) == 1
    
    # Récupérer toutes les interactions
    history_all = memory.get_history("test_user_4", limit=10)
    assert len(history_all) == 3


def test_clear_user_history(temp_db):
    """Test de l'effacement de l'historique d'un utilisateur"""
    memory = temp_db
    
    # Sauvegarder des interactions pour 2 utilisateurs
    memory.save_interaction("user_A", "desktop", "Message A1", "Réponse A1")
    memory.save_interaction("user_A", "desktop", "Message A2", "Réponse A2")
    memory.save_interaction("user_B", "desktop", "Message B1", "Réponse B1")
    
    # Effacer l'historique de user_A
    deleted = memory.clear_user_history("user_A")
    
    assert deleted == 2
    
    # Vérifier que user_A n'a plus d'historique
    history_a = memory.get_history("user_A")
    assert len(history_a) == 0
    
    # Vérifier que user_B a toujours son historique
    history_b = memory.get_history("user_B")
    assert len(history_b) == 1


def test_clear_user_history_by_source(temp_db):
    """Test de l'effacement de l'historique par source"""
    memory = temp_db
    
    # Sauvegarder des interactions depuis 2 sources
    memory.save_interaction("user_C", "desktop", "Message desktop", "Réponse 1")
    memory.save_interaction("user_C", "discord", "Message discord", "Réponse 2")
    
    # Effacer seulement les interactions desktop
    deleted = memory.clear_user_history("user_C", source="desktop")
    
    assert deleted == 1
    
    # Vérifier qu'il reste seulement l'interaction discord
    history = memory.get_history("user_C")
    assert len(history) == 1
    assert history[0]['user_input'] == "Message discord"


def test_clear_all_history(temp_db):
    """Test de l'effacement total de l'historique"""
    memory = temp_db
    
    # Sauvegarder des interactions pour plusieurs utilisateurs
    memory.save_interaction("user_X", "desktop", "Message X", "Réponse X")
    memory.save_interaction("user_Y", "discord", "Message Y", "Réponse Y")
    memory.save_interaction("user_Z", "desktop", "Message Z", "Réponse Z")
    
    # Effacer tout l'historique
    deleted = memory.clear_all_history()
    
    assert deleted == 3
    
    # Vérifier que tous les utilisateurs n'ont plus d'historique
    assert len(memory.get_history("user_X")) == 0
    assert len(memory.get_history("user_Y")) == 0
    assert len(memory.get_history("user_Z")) == 0


def test_get_stats(temp_db):
    """Test des statistiques globales"""
    memory = temp_db
    
    # Sauvegarder des interactions variées
    memory.save_interaction("user_1", "desktop", "Message 1", "Réponse 1", emotion="joy")
    memory.save_interaction("user_1", "discord", "Message 2", "Réponse 2", emotion="joy")
    memory.save_interaction("user_2", "desktop", "Message 3", "Réponse 3", emotion="sorrow")
    
    # Récupérer les stats
    stats = memory.get_stats()
    
    assert stats['total_interactions'] == 3
    assert stats['unique_users'] == 2
    assert stats['by_source']['desktop'] == 2
    assert stats['by_source']['discord'] == 1
    assert stats['by_emotion']['joy'] == 2
    assert stats['by_emotion']['sorrow'] == 1


def test_get_user_stats(temp_db):
    """Test des statistiques par utilisateur"""
    memory = temp_db
    
    # Sauvegarder plusieurs interactions pour un utilisateur
    memory.save_interaction("user_stats", "desktop", "Msg 1", "Rép 1", emotion="joy")
    memory.save_interaction("user_stats", "desktop", "Msg 2", "Rép 2", emotion="joy")
    memory.save_interaction("user_stats", "discord", "Msg 3", "Rép 3", emotion="angry")
    
    # Récupérer les stats utilisateur
    user_stats = memory.get_user_stats("user_stats")
    
    assert user_stats['total_interactions'] == 3
    assert user_stats['by_source']['desktop'] == 2
    assert user_stats['by_source']['discord'] == 1
    assert len(user_stats['top_emotions']) == 2
    # Joy devrait être en premier (2 occurrences)
    assert user_stats['top_emotions'][0][0] == 'joy'
    assert user_stats['top_emotions'][0][1] == 2


def test_emotion_none(temp_db):
    """Test sauvegarde sans émotion (optionnel)"""
    memory = temp_db
    
    # Sauvegarder sans émotion
    memory.save_interaction(
        user_id="user_no_emotion",
        source="desktop",
        user_input="Message neutre",
        bot_response="Réponse neutre"
        # Pas d'émotion
    )
    
    # Récupérer l'historique
    history = memory.get_history("user_no_emotion")
    
    assert len(history) == 1
    assert history[0]['emotion'] is None


def test_multiple_users_isolation(temp_db):
    """Test de l'isolation entre utilisateurs"""
    memory = temp_db
    
    # Sauvegarder des interactions pour différents utilisateurs
    memory.save_interaction("alice", "desktop", "Hello from Alice", "Hi Alice!")
    memory.save_interaction("bob", "discord", "Hello from Bob", "Hi Bob!")
    memory.save_interaction("alice", "desktop", "Second message Alice", "Second response!")
    
    # Vérifier l'isolation
    alice_history = memory.get_history("alice")
    bob_history = memory.get_history("bob")
    
    assert len(alice_history) == 2
    assert len(bob_history) == 1
    
    # Vérifier le contenu
    assert "Alice" in alice_history[0]['user_input']
    assert "Bob" in bob_history[0]['user_input']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
