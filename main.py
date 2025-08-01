from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import message as platform_message

# from ..LangBot.pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
# from ..LangBot.pkg.plugin.events import *  # 导入事件类
# from ..LangBot.pkg.platform.types import message as platform_message


# 注册插件
@register(name="DifyInputExt", description="Plugin for extend Dify input, sending more chat contexts", version="0.1", author="MadCat")
class DifyInputExt(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # @handler(PromptPreProcessing)
    # async def prompt_pre_processing(self, ctx: EventContext):

    # 当收到个人消息时触发

    # @handler(PersonNormalMessageReceived)
    # async def person_normal_message_received(self, ctx: EventContext):
    #     msg_chain: platform_message.MessageChain = ctx.event.query.message_chain
    #     ctx.event.query.set_variable("source", str(msg_chain.source))

    @handler(PersonMessageReceived)
    async def person_message_received(self, ctx: EventContext):
        msg_chain: platform_message.MessageChain = ctx.event.message_chain
        ctx.event.query.set_variable("source", str(msg_chain.source))
        self.ap.logger.info("hello, {}".format(str(msg_chain.source)))
        self.ap.logger.info("hello, {}".format(str(ctx.event.query)))

    # 当收到群消息时触发
    # @handler(GroupNormalMessageReceived)
    # async def group_normal_message_received(self, ctx: EventContext):
    #     msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
    #     if msg == "hello":  # 如果消息为hello

    #         # 输出调试信息
    #         self.ap.logger.debug("hello, {}".format(ctx.event.sender_id))

    #         # 回复消息 "hello, everyone!"
    #         ctx.add_return("reply", ["hello, everyone!"])

    #         # 阻止该事件默认行为（向接口获取回复）
    #         ctx.prevent_default()

    # 插件卸载时触发

    def __del__(self):
        pass
