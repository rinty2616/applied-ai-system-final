
"""PawPal+ smart planning and verification workflow."""

import logging
from datetime import date
from pawpal_system import Scheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


class SmartPlanner:
    """Plan, verify, and explain a pet-care schedule."""

    def __init__(self, owner):
        self.owner = owner
        self.scheduler = Scheduler(owner)

    def create_plan(self, on_date=None):
        day = on_date or date.today()
        logger.info("Creating pet-care plan for %s", day)

        # PLAN: Use the existing priority-aware scheduler.
        tasks, skipped = self.scheduler.build_daily_plan(day)

        # VERIFY: Independently check the proposed schedule.
        issues = []
        total_minutes = sum(
            task.duration_minutes for _, task in tasks
        )

        if total_minutes > self.owner.daily_available_minutes:
            issues.append("Plan exceeds the daily time budget.")

        for i, (_, first) in enumerate(tasks):
            for _, second in tasks[i + 1:]:
                if (
                    first.start_at() < second.end_at()
                    and second.start_at() < first.end_at()
                ):
                    issues.append(
                        f"Overlap: {first.title} and {second.title}"
                    )

        # EXPLAIN: Return the plan and reasons.
        explanations = [
            f"{pet.name}: {task.title} at {task.time} "
            f"({task.priority} priority)"
            for pet, task in tasks
        ]

        result = {
            "date": str(day),
            "verified": len(issues) == 0,
            "total_minutes": total_minutes,
            "schedule": explanations,
            "skipped": skipped,
            "issues": issues,
        }

        logger.info(
            "Verification complete: %s",
            "PASS" if result["verified"] else "FAIL"
        )

        return result
