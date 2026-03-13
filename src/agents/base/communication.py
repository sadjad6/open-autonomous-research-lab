"""Inter-agent message bus for communication."""

from __future__ import annotations

import asyncio
import logging
from collections import defaultdict
from collections.abc import Callable, Coroutine
from typing import Any

from src.agents.base.types import AgentMessage, AgentRole

logger = logging.getLogger(__name__)

MessageHandler = Callable[[AgentMessage], Coroutine[Any, Any, None]]


class MessageBus:
    """Async message bus that routes messages between agents.

    Agents subscribe to their role and receive messages
    addressed to them via registered handlers.
    """

    def __init__(self) -> None:
        self._handlers: dict[AgentRole, list[MessageHandler]] = defaultdict(list)
        self._message_log: list[AgentMessage] = []

    def subscribe(self, role: AgentRole, handler: MessageHandler) -> None:
        """Register a handler for messages addressed to *role*."""
        self._handlers[role].append(handler)
        logger.info("Subscribed handler for role %s", role.value)

    async def publish(self, message: AgentMessage) -> None:
        """Deliver a message to all handlers of the target role."""
        self._message_log.append(message)
        logger.debug(
            "Message %s → %s (type=%s)",
            message.sender.value,
            message.receiver.value,
            message.message_type.value,
        )
        handlers = self._handlers.get(message.receiver, [])
        if not handlers:
            logger.warning("No handlers for role %s", message.receiver.value)
            return
        await asyncio.gather(*(h(message) for h in handlers))

    async def broadcast(self, message: AgentMessage, exclude: AgentRole | None = None) -> None:
        """Send a message to *all* registered roles (except *exclude*)."""
        tasks = []
        for role, handlers in self._handlers.items():
            if role == exclude:
                continue
            for handler in handlers:
                redirected = AgentMessage(
                    sender=message.sender,
                    receiver=role,
                    message_type=message.message_type,
                    payload=message.payload,
                    correlation_id=message.correlation_id,
                )
                tasks.append(handler(redirected))
        if tasks:
            await asyncio.gather(*tasks)

    @property
    def message_history(self) -> list[AgentMessage]:
        """Full log of processed messages (for observability)."""
        return list(self._message_log)

    def clear_history(self) -> None:
        self._message_log.clear()
