from models.request import Request
from models.teaching_plan import TeachingPlan


class Teacher:
    """
    Creates a teaching strategy for a user's Request.

    Responsibilities:
    - Understand the learner's needs.
    - Decide how the topic should be taught.
    - Produce a TeachingPlan.

    Non-Responsibilities:
    - Response generation.
    - Prompt construction.
    - LLM interaction.
    - Formatting output.
    """

    def create_plan(self, request: Request) -> TeachingPlan:
        """
        Create a TeachingPlan for the given Request.
        """

        # TODO: Understand what the learner needs.
        learning_goal = self._determine_goal(request)

        # TODO: Select the appropriate teaching strategy.
        strategy = self._select_strategy(learning_goal)

        # TODO: Build the TeachingPlan.
        plan = self._build_plan(learning_goal, strategy)

        return plan

    def _determine_goal(self, request: Request):
        """
        TODO:
        Identify the user's learning objective.
        """
        pass

    def _select_strategy(self, goal):
        """
        TODO:
        Choose the most appropriate teaching strategy.
        """
        pass

    def _build_plan(self, goal, strategy):
        """
        TODO:
        Construct the TeachingPlan.
        """
        pass