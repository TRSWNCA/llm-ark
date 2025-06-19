import llm
from llm.default_plugins.openai_models import Chat

# Try to import AsyncChat, but don't fail if it's not available
try:
    from llm.default_plugins.openai_models import AsyncChat
    HAS_ASYNC = True
except ImportError:
    HAS_ASYNC = False

MODELS = (
    # DeepSeek Models
    "deepseek-r1-250528",
    "deepseek-v3-250324",
    "deepseek-r1-distill-qwen-7b-250120"
    # Doubao Text Models
    "doubao-seed-1-6-250615",
    "doubao-seed-1.6-flash-250615"
    "doubao-1.5-pro-32k-250115",
    "doubao-1.5-pro-256k-250115",
    "doubao-1.5-lite-32k-250115"
)


class ArkChat(Chat):
    needs_key = "ark"
    key_env_var = "ARK_API_KEY"

    def __init__(self, model_name):
        super().__init__(
            model_name=model_name,
            model_id=model_name,
            api_base="https://ark.cn-beijing.volces.com/api/v3",
        )

    def __str__(self):
        return "Ark: {}".format(self.model_id)


# Only define AsyncChat class if async support is available
if HAS_ASYNC:

    class ArkAsyncChat(AsyncChat):
        needs_key = "ark"
        key_env_var = "ARK_API_KEY"

        def __init__(self, model_name):
            super().__init__(
                model_name=model_name,
                model_id=model_name,
                api_base="https://ark.cn-beijing.volces.com/api/v3",
            )

        def __str__(self):
            return "Ark: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    # Only do this if the key is set
    key = llm.get_key("", "ark", ArkChat.key_env_var)
    if not key:
        return
    for model_id in MODELS:
        if HAS_ASYNC:
            register(
                ArkChat(model_id),
                ArkAsyncChat(model_id),
            )
        else:
            register(ArkChat(model_id))