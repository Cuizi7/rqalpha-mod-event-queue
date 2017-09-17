from rqalpha.interface import AbstractMod
from rqalpha.const import RUN_TYPE

from .queued_event_bus import QueuedEventBus


class EventQueueMod(AbstractMod):
    def __init__(self):
        self._env = None
        self._mod_config = None

    def start_up(self, env, mod_config):
        self._env = env
        self._mod_config = mod_config
        if self._env.config.base.run_type == RUN_TYPE.BACKTEST:
            return
        self._env.event_bus = QueuedEventBus(self._env.event_bus, real_time=True)
        self._env.event_bus.start()

    def tear_down(self, code, exception=None):
        if self._env.config.base.run_type == RUN_TYPE.BACKTEST:
            return
        self._env.event_bus.stop()
