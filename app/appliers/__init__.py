"""Initialize appliers and register them with the factory."""

from app.appliers.factory import JobApplierFactory
from app.appliers.seek import SeekApplier
from app.appliers.greenhouse import GreenhouseApplier

# Register appliers
JobApplierFactory.register_applier("seek", SeekApplier)
JobApplierFactory.register_applier("greenhouse", GreenhouseApplier)
