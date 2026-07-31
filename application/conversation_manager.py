from application.reasoning_engine import ReasoningEngine
from models.request import Request
from models.response import Response


class ConversationManager:
    """
    Entry point into the Atlas application.

    Responsibilities:
    - Manage the lifecycle of a Request.
    - Resolve or create the appropriate Session.
    - Delegate reasoning to the ReasoningEngine.
    - Update session metadata.
    - Return the final Response.

    Non-Responsibilities:
    - Understanding user intent.
    - Memory retrieval.
    - Teaching.
    - Prompt construction.
    - LLM interaction.
    """

    def __init__(self, reasoning_engine: ReasoningEngine):
        self._reasoning_engine = reasoning_engine

    def handle_request(self, request: Request) -> Response:
        """
        Process a single Request through the Atlas pipeline.
        """

        # TODO: Implement session resolution.
        session = self._resolve_session(request)

        # Delegate all reasoning to the Reasoning Engine.
        response = self._reasoning_engine.process(request)

        # TODO: Update and persist session metadata.
        self._update_session(session)

        return response

    def _resolve_session(self, request: Request):
        """
        TODO:
        Determine whether this Request belongs to an existing
        Session or requires creating a new one.

        Deferred until session persistence is implemented.
        """
        pass

    def _update_session(self, session):
        """
        TODO:
        Update session metadata such as last_active_at and
        persist any changes.

        Deferred until session persistence is implemented.
        """
        pass
