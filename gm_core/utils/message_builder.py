"""
消息构建器模块

负责构建各种类型的精美消息。
采用模块级函数设计，符合 Pythonic 风格。
"""

from typing import Any
from astrbot.api.event import AstrMessageEvent


def success(content: str) -> str:
    """
    构建成功消息

    Args:
        content: 消息内容

    Returns:
        格式化后的成功消息
    """
    return f"✨ {content}"


def error(content: str) -> str:
    """
    构建错误消息

    Args:
        content: 消息内容

    Returns:
        格式化后的错误消息
    """
    return f"❌ {content}"


def warning(content: str) -> str:
    """
    构建警告消息

    Args:
        content: 消息内容

    Returns:
        格式化后的警告消息
    """
    return f"⚠️ {content}"


def info(content: str) -> str:
    """
    构建信息消息

    Args:
        content: 消息内容

    Returns:
        格式化后的信息消息
    """
    return f"ℹ️ {content}"


def admin_required(event: AstrMessageEvent) -> str:
    """
    构建需要管理员权限的消息

    Args:
        event: 消息事件

    Returns:
        格式化后的权限提示消息
    """
    sender_id = event.get_sender_id()
    return (
        f"🔒 @{sender_id}\n"
        f"❌ 此指令仅限管理员使用\n\n"
        f"💡 请联系群管理员或配置管理员列表"
    )


def build_admin_list(admins: list[str]) -> str:
    """
    构建管理员列表消息

    Args:
        admins: 管理员ID列表

    Returns:
        格式化后的管理员列表
    """
    if not admins:
        return warning("当前群没有配置管理员\n使用 /gm admin add [用户ID] 添加")

    message_parts = [
        "📋 当前群管理员列表\n",
        "=" * 40 + "\n"
    ]

    for idx, admin_id in enumerate(admins, 1):
        message_parts.append(f"{idx}. {admin_id}\n")

    message_parts.append(f"\n📊 总计: {len(admins)} 人")

    return "".join(message_parts)


def build_rules_list(rules: list[dict[str, Any]]) -> str:
    """
    构建规则列表消息

    Args:
        rules: 规则列表，每条规则包含 type 和 content 字段

    Returns:
        格式化后的规则列表
    """
    if not rules:
        return warning("当前群没有任何规则")

    message_parts = ["群规则："]

    for rule in rules:
        message_parts.append(f"\n{rule['content']}")

    return "".join(message_parts)


def build_whitelist_list(whitelist: list[str]) -> str:
    """
    构建白名单列表消息

    Args:
        whitelist: 白名单列表

    Returns:
        格式化后的白名单列表
    """
    if not whitelist:
        return warning("当前群白名单为空")

    message_parts = [
        "📋 当前群白名单\n",
        "=" * 40 + "\n"
    ]

    for idx, user_id in enumerate(whitelist, 1):
        message_parts.append(f"{idx}. {user_id}\n")

    message_parts.append(f"\n📊 总计: {len(whitelist)} 人")

    return "".join(message_parts)


def build_blacklist_list(blacklist: list[str]) -> str:
    """
    构建黑名单列表消息

    Args:
        blacklist: 黑名单列表

    Returns:
        格式化后的黑名单列表
    """
    if not blacklist:
        return warning("当前群黑名单为空")

    message_parts = [
        "📋 当前群黑名单\n",
        "=" * 40 + "\n"
    ]

    for idx, user_id in enumerate(blacklist, 1):
        message_parts.append(f"{idx}. {user_id}\n")

    message_parts.append(f"\n📊 总计: {len(blacklist)} 人")

    return "".join(message_parts)


def build_test_result(
    test_text: str,
    matched: bool,
    matched_rules: list[dict[str, Any]]
) -> str:
    """
    构建测试结果消息

    Args:
        test_text: 测试文本
        matched: 是否匹配
        matched_rules: 匹配的规则列表，每条规则包含 type 和 content 字段

    Returns:
        格式化后的测试结果
    """
    if matched:
        message_parts = [
            "✅ 测试通过\n",
            "=" * 40 + "\n",
            f"📝 测试文本: {test_text}\n",
            f"✨ 匹配到 {len(matched_rules)} 条规则:\n\n"
        ]

        for idx, rule in enumerate(matched_rules, 1):
            rule_type = "🔍 正则" if rule["type"] == "regex" else "🔑 关键词"
            message_parts.append(f"{idx}. {rule_type}: {rule['content']}\n")

        message_parts.append(f"\n🎉 该加群申请将被允许！")
    else:
        message_parts = [
            "❌ 测试失败\n",
            "=" * 40 + "\n",
            f"📝 测试文本: {test_text}\n",
            f"⚠️ 未匹配到任何规则\n",
            f"🚫 该加群申请将被拒绝！"
        ]

    return "".join(message_parts)


def build_help_message() -> str:
    """
    构建帮助信息

    Returns:
        格式化后的帮助消息
    """
    return (
        "🤖 GroupManager 群管理器帮助\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 功能介绍\n"
        "本插件支持通过关键词、正则表达式、白名单和黑名单验证加群申请。\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💻 指令列表\n\n"
        "【规则管理】\n"
        "  🔧 /gm add [关键词|正则]\n"
        "     添加关键词或正则规则\n"
        "  🔨 /gm remove [索引]\n"
        "     删除指定索引的规则\n"
        "  📋 /gm list\n"
        "     查看当前群的所有规则\n"
        "  🗑️ /gm clear\n"
        "     清空当前群的所有规则\n"
        "  🧪 /gm test [测试文本]\n"
        "     测试文本是否匹配规则\n\n"
        "【白名单管理】\n"
        "  ⚪ /gm whitelist add [用户ID]\n"
        "     添加用户到白名单\n"
        "  ⚪ /gm whitelist remove [用户ID]\n"
        "     从白名单移除用户\n"
        "  📋 /gm whitelist list\n"
        "     查看白名单\n\n"
        "【黑名单管理】\n"
        "  ⚫ /gm blacklist add [用户ID]\n"
        "     添加用户到黑名单\n"
        "  ⚫ /gm blacklist remove [用户ID]\n"
        "     从黑名单移除用户\n"
        "  📋 /gm blacklist list\n"
        "     查看黑名单\n\n"
        "【系统管理】\n"
        "  ⚙️ /gm enable\n"
        "     启用本群的群管理功能\n"
        "  ⚙️ /gm disable\n"
        "     禁用本群的群管理功能\n"
        "  👑 /gm admin add [用户ID]\n"
        "     添加本群管理员\n"
        "  👑 /gm admin remove [用户ID]\n"
        "     移除本群管理员\n"
        "  📋 /gm admin list\n"
        "     查看本群管理员列表\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 使用提示\n"
        "  • 正则表达式请使用 // 包裹\n"
        "  • 关键词支持部分匹配\n"
        "  • 白名单优先级最高，直接通过\n"
        "  • 黑名单优先级次之，直接拒绝\n"
        "  • 只有管理员可以添加/删除规则\n"
        "  • 所有成员都可以查看和测试规则\n\n"
        "📚 正则表达式示例\n"
        "  • 手机号: /\\d{11}/\n"
        "  • QQ号: /[1-9][0-9]{4,}/\n"
        "  • 邮箱: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/\n"
        "  • 学号: /\\d{8,12}/\n"
        "  • 身份证: /\\d{17}[\\dXx]/\n\n"
        "⚙️ 开发者: Kush-ShuL\n"
        "🔗 项目: https://github.com/Kush-ShuL/GroupManager"
    )
