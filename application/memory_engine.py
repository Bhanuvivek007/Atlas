from models.memory import Memory
from models.request import Request


class MemoryEngine:
    """
    Retrieves the memories relevant to a user's Request.

    Responsibilities:
    - Identify relevant memories.
    - Return them for reasoning.

    Non-Responsibilities:
    - Database access.
    - Embedding generation.
    - Response generation.
    """

    def retrieve(self, request: Request) -> list[Memory]:
        """
        Retrieve the memories relevant to the given Request.
        """

        # TODO: Determine what information is needed.
        query = self._build_query(request)

        # TODO: Retrieve matching memories.
        memories = self._retrieve_memories(query)

        return memories

    def _build_query(self, request: Request):
        """
        TODO:
        Build a search query from the Request.
        """
        pass

    def _retrieve_memories(self, query):
        """
        TODO:
        Retrieve the matching memories.
        """
        pass
