"""
Système de Mémoire Conversationnelle - Desktop-Mate (Kira)

Gère la mémoire conversationnelle avec SQLite :
- Historique des conversations par utilisateur
- Support multi-source (GUI Desktop-Mate + Discord)
- Sauvegarde des émotions détectées
- Fonctions CRUD optimisées avec indexes
"""

import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from contextlib import contextmanager
import logging

# Configuration du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConversationMemory:
    """Gestionnaire de mémoire conversationnelle SQLite"""
    
    def __init__(self, db_path: str = "data/chat_history.db"):
        """
        Initialise le gestionnaire de mémoire
        
        Args:
            db_path: Chemin vers la base SQLite (créée automatiquement si inexistante)
        """
        self.db_path = db_path
        
        # Créer le dossier data si nécessaire
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Initialiser la base de données
        self._init_database()
        
        logger.info(f"✅ ConversationMemory initialisée : {db_path}")
    
    @contextmanager
    def _get_connection(self):
        """Context manager pour gérer les connexions SQLite de manière thread-safe"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error(f"❌ Erreur transaction SQLite : {e}")
            raise
        finally:
            conn.close()
    
    def _init_database(self):
        """Crée le schema de la base de données si nécessaire"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Table principale : historique des conversations
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    source TEXT NOT NULL,
                    user_input TEXT NOT NULL,
                    bot_response TEXT NOT NULL,
                    emotion TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Index pour optimiser les requêtes fréquentes
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_user_id 
                ON chat_history(user_id)
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_source 
                ON chat_history(source)
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON chat_history(timestamp DESC)
            """)
            
            # Index composite pour récupération rapide d'historique utilisateur
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_user_timestamp 
                ON chat_history(user_id, timestamp DESC)
            """)
            
            logger.info("✅ Schema SQLite créé/vérifié")
    
    def save_interaction(
        self,
        user_id: str,
        source: str,
        user_input: str,
        bot_response: str,
        emotion: Optional[str] = None
    ) -> int:
        """
        Sauvegarde une interaction dans la base de données
        
        Args:
            user_id: ID utilisateur (Discord ID ou "desktop_user")
            source: Source de l'interaction ("discord" ou "desktop")
            user_input: Message de l'utilisateur
            bot_response: Réponse de Kira
            emotion: Émotion détectée (optionnel)
        
        Returns:
            ID de l'interaction sauvegardée
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO chat_history (user_id, source, user_input, bot_response, emotion)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, source, user_input, bot_response, emotion))
            
            interaction_id = cursor.lastrowid
            
            logger.debug(
                f"💾 Interaction sauvegardée : "
                f"user={user_id[:8]}..., source={source}, emotion={emotion}"
            )
            
            return interaction_id
    
    def get_history(
        self,
        user_id: str,
        limit: int = 10,
        source: Optional[str] = None
    ) -> List[Dict]:
        """
        Récupère l'historique des conversations d'un utilisateur
        
        Args:
            user_id: ID utilisateur
            limit: Nombre maximum d'interactions à récupérer
            source: Filtrer par source ("discord" ou "desktop"), None = toutes
        
        Returns:
            Liste d'interactions (du plus ancien au plus récent)
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            if source:
                cursor.execute("""
                    SELECT user_input, bot_response, emotion, timestamp
                    FROM chat_history
                    WHERE user_id = ? AND source = ?
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (user_id, source, limit))
            else:
                cursor.execute("""
                    SELECT user_input, bot_response, emotion, timestamp
                    FROM chat_history
                    WHERE user_id = ?
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (user_id, limit))
            
            rows = cursor.fetchall()
            
            # Convertir en liste de dictionnaires (du plus ancien au plus récent)
            history = [
                {
                    'user_input': row['user_input'],
                    'bot_response': row['bot_response'],
                    'emotion': row['emotion'],
                    'timestamp': row['timestamp']
                }
                for row in reversed(rows)  # Inverser pour avoir chronologique
            ]
            
            logger.debug(f"📖 Historique récupéré : {len(history)} interactions pour {user_id[:8]}...")
            
            return history
    
    def clear_user_history(self, user_id: str, source: Optional[str] = None) -> int:
        """
        Efface l'historique d'un utilisateur spécifique
        
        Args:
            user_id: ID utilisateur
            source: Filtrer par source (optionnel)
        
        Returns:
            Nombre d'interactions supprimées
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            if source:
                cursor.execute("""
                    DELETE FROM chat_history
                    WHERE user_id = ? AND source = ?
                """, (user_id, source))
            else:
                cursor.execute("""
                    DELETE FROM chat_history
                    WHERE user_id = ?
                """, (user_id,))
            
            deleted_count = cursor.rowcount
            
            logger.info(
                f"🗑️ Historique effacé : {deleted_count} interactions "
                f"pour {user_id[:8]}... (source={source or 'all'})"
            )
            
            return deleted_count
    
    def clear_all_history(self) -> int:
        """
        Efface TOUT l'historique (nécessite 2FA)
        
        ⚠️ ATTENTION : Cette action est irréversible !
        
        Returns:
            Nombre total d'interactions supprimées
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM chat_history")
            deleted_count = cursor.rowcount
            
            logger.warning(
                f"⚠️ TOUT l'historique effacé : {deleted_count} interactions supprimées"
            )
            
            return deleted_count
    
    def get_stats(self) -> Dict:
        """
        Récupère des statistiques sur la base de données
        
        Returns:
            Dictionnaire avec statistiques globales
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Nombre total d'interactions
            cursor.execute("SELECT COUNT(*) FROM chat_history")
            total_interactions = cursor.fetchone()[0]
            
            # Nombre d'utilisateurs uniques
            cursor.execute("SELECT COUNT(DISTINCT user_id) FROM chat_history")
            unique_users = cursor.fetchone()[0]
            
            # Répartition par source
            cursor.execute("""
                SELECT source, COUNT(*) as count
                FROM chat_history
                GROUP BY source
            """)
            by_source = {row['source']: row['count'] for row in cursor.fetchall()}
            
            # Répartition par émotion
            cursor.execute("""
                SELECT emotion, COUNT(*) as count
                FROM chat_history
                WHERE emotion IS NOT NULL
                GROUP BY emotion
                ORDER BY count DESC
            """)
            by_emotion = {row['emotion']: row['count'] for row in cursor.fetchall()}
            
            # Interaction la plus récente
            cursor.execute("""
                SELECT timestamp
                FROM chat_history
                ORDER BY timestamp DESC
                LIMIT 1
            """)
            last_interaction = cursor.fetchone()
            last_timestamp = last_interaction['timestamp'] if last_interaction else None
            
            stats = {
                'total_interactions': total_interactions,
                'unique_users': unique_users,
                'by_source': by_source,
                'by_emotion': by_emotion,
                'last_interaction': last_timestamp,
                'database_path': self.db_path
            }
            
            logger.info(
                f"📊 Stats : {total_interactions} interactions, "
                f"{unique_users} utilisateurs"
            )
            
            return stats
    
    def get_user_stats(self, user_id: str) -> Dict:
        """
        Récupère des statistiques pour un utilisateur spécifique
        
        Args:
            user_id: ID utilisateur
        
        Returns:
            Dictionnaire avec statistiques utilisateur
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Nombre total d'interactions
            cursor.execute("""
                SELECT COUNT(*) FROM chat_history WHERE user_id = ?
            """, (user_id,))
            total = cursor.fetchone()[0]
            
            # Par source
            cursor.execute("""
                SELECT source, COUNT(*) as count
                FROM chat_history
                WHERE user_id = ?
                GROUP BY source
            """, (user_id,))
            by_source = {row['source']: row['count'] for row in cursor.fetchall()}
            
            # Émotions les plus fréquentes
            cursor.execute("""
                SELECT emotion, COUNT(*) as count
                FROM chat_history
                WHERE user_id = ? AND emotion IS NOT NULL
                GROUP BY emotion
                ORDER BY count DESC
                LIMIT 5
            """, (user_id,))
            top_emotions = [(row['emotion'], row['count']) for row in cursor.fetchall()]
            
            return {
                'user_id': user_id,
                'total_interactions': total,
                'by_source': by_source,
                'top_emotions': top_emotions
            }


# Instance globale (sera créée dans config.py)
_memory_instance = None

def get_memory(db_path: str = "data/chat_history.db") -> ConversationMemory:
    """
    Récupère l'instance globale de ConversationMemory (singleton)
    
    Args:
        db_path: Chemin vers la base SQLite
    
    Returns:
        Instance ConversationMemory
    """
    global _memory_instance
    
    if _memory_instance is None:
        _memory_instance = ConversationMemory(db_path)
    
    return _memory_instance


# Pour tests et usage direct
if __name__ == "__main__":
    # Test rapide du système de mémoire
    print("🧪 Test du système de mémoire...\n")
    
    memory = ConversationMemory("data/test_chat_history.db")
    
    # Test sauvegarde
    print("1. Sauvegarde d'une interaction...")
    interaction_id = memory.save_interaction(
        user_id="desktop_user",
        source="desktop",
        user_input="Bonjour Kira !",
        bot_response="Salut ! Comment puis-je t'aider ?",
        emotion="joy"
    )
    print(f"   ✅ Interaction sauvegardée : ID={interaction_id}\n")
    
    # Test récupération historique
    print("2. Récupération de l'historique...")
    history = memory.get_history("desktop_user", limit=10)
    print(f"   ✅ {len(history)} interactions récupérées\n")
    
    # Test statistiques
    print("3. Statistiques globales...")
    stats = memory.get_stats()
    print(f"   ✅ Total : {stats['total_interactions']} interactions")
    print(f"   ✅ Utilisateurs : {stats['unique_users']}")
    print(f"   ✅ Par source : {stats['by_source']}\n")
    
    # Test effacement utilisateur
    print("4. Effacement historique utilisateur...")
    deleted = memory.clear_user_history("desktop_user")
    print(f"   ✅ {deleted} interactions supprimées\n")
    
    print("✅ Tous les tests passés !")
