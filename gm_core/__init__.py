"""
GroupManager - 智能群管理插件

一个强大的 AstrBot 群管理插件，支持通过正则表达式、关键词、
白名单和黑名单验证加群申请。

Author: Kush-ShuL
Version: v1.0.0
License: AGPL-v3
"""

__version__ = "1.0.0"
__author__ = "Kush-ShuL"

from .core.config import Config
from .core.storage import Storage
from .core.validator import Validator
from .core.validator import RuleType, ValidationResult

from .handlers.rule_handler import RuleHandler
from .handlers.whitelist_blacklist_handler import WhitelistBlacklistHandler
from .handlers.group_join_request_handler import GroupJoinRequestHandler

from .utils.message_builder import MessageBuilder
from .utils.permission import is_admin
from .utils.notification_manager import NotificationManager

__all__ = [
    "Config",
    "Storage",
    "Validator",
    "RuleType",
    "ValidationResult",
    "RuleHandler",
    "WhitelistBlacklistHandler",
    "GroupJoinRequestHandler",
    "MessageBuilder",
    "is_admin",
    "NotificationManager",
]
