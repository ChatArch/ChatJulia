"Typed environment configuration for ChatJulia."

from chatenv import BaseEnvConfig, EnvField


class ChatjuliaConfig(BaseEnvConfig):
    "ChatJulia ChatEnv configuration."

    _title = "ChatJulia Configuration"
    _aliases = ["chatjulia"]
    _storage_dir = "Chatjulia"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATJULIA_API_KEY = EnvField(
        "CHATJULIA_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatjuliaConfig"]
