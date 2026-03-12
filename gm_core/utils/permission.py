"""
权限检查模块

负责检查用户权限。
"""

from astrbot.api.event import AstrMessageEvent
from ..core import Config, Storage


async def is_admin(event: AstrMessageEvent, storage: Storage = None, config: Config = None) -> bool:
    """
    检查用户是否为管理员

    Args:
        event: 消息事件
        storage: 存储对象（可选，用于检查群管理员）
        config: 配置对象（可选，用于检查全局管理员）

    Returns:
        如果是管理员返回 True，否则返回 False
    """
    user_id = event.get_sender_id()
    group_id = event.message_obj.group_id

    if storage and group_id:
        group_admins = await storage.get_group_admins(group_id)
        if str(user_id) in [str(a) for a in group_admins]:
            return True

    if config:
        return config.is_admin(user_id)

    return True
