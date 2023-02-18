from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import openai
from os import environ, path

openai.api_key = environ('OPENAI_API_KEY')

class ChatGPTBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Привет, постараюсь ответить на любой вопрос!")

    async def on_message_activity(self, turn_context: TurnContext):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=turn_context.activity.text,
            temperature=0.9,
            max_tokens=4000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print(response)
        return await turn_context.send_activity(
            MessageFactory.text(response['choices'][0]['text'])
        )



