"""Neo4j database connection setup."""

from neo4j import GraphDatabase
from .config import settings

driver = GraphDatabase.driver(
    settings.neo4j_uri,
    auth=(settings.neo4j_user, settings.neo4j_password),
)


def get_neo4j():
    """Dependency that provides a Neo4j session per request."""
    with driver.session() as session:
        yield session


def close_neo4j():
    """Close the Neo4j driver on shutdown."""
    driver.close()