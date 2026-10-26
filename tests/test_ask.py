from types import SimpleNamespace

from app.ask import ask


def test_ask_sends_message_to_existing_chat(capsys):
    sent_messages = []

    def send_message(message):
        sent_messages.append(message)
        return SimpleNamespace(
            usage_metadata=SimpleNamespace(prompt_token_count=3, candidates_token_count=2),
            text="answer",
        )

    chat = SimpleNamespace(send_message=send_message)

    assert ask("follow-up", chat) == "answer"
    assert sent_messages == ["follow-up"]
    assert "[トークン数] 入力: 3 / 出力: 2" in capsys.readouterr().out