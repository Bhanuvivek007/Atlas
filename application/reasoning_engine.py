from application.generation_engine import GenerationEngine
from application.memory_engine import MemoryEngine
from application.teacher import Teacher

from models.request import Request
from models.response import Response


class ReasoningEngine:
    """
    Determines how Atlas should think about a Request.

    Responsibilities:
    - Understand user intent.
    - Compose the appropriate processing pipeline.
    - Coordinate specialized capabilities.
    - Return the final Response.

    Non-Responsibilities:
    - Session management.
    - Request creation.
    - UI interaction.
    - Infrastructure concerns.
    """

    def __init__(
        self,
        teacher: Teacher,
        memory_engine: MemoryEngine,
        generation_engine: GenerationEngine,
    ):
        self._teacher = teacher
        self._memory_engine = memory_engine
        self._generation_engine = generation_engine

    def process(self, request: Request) -> Response:
        """
        Process a Request by selecting and executing the
        appropriate reasoning strategy.
        """

        # TODO: Determine what the user wants.
        intent = self._understand(request)

        # TODO: Select the capabilities required.
        pipeline = self._compose_pipeline(intent)

        # TODO: Execute the selected pipeline.
        response = self._execute_pipeline(pipeline, request)

        return response

    def _understand(self, request: Request):
        """
        TODO:
        Determine the user's intent from the Request.
        """
        pass

    def _compose_pipeline(self, intent):
        """
        TODO:
        Select the capabilities required to satisfy
        the identified intent.
        """
        pass

    def _execute_pipeline(self, pipeline, request):
        """
        TODO:
        Coordinate the selected capabilities and return
        the final Response.
        """
        pass
