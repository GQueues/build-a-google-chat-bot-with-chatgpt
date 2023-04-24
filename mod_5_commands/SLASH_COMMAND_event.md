# MESSAGE event for Slash Command

Below is an example of the json sent by a bot for a Slash Command message event.


```
{
    'type': 'MESSAGE',
    'eventTime': '2023-04-24T14:49:45.938847Z',
    'message': {
        'name': 'spaces/7IpBtkAAAAE/messages/wvIbPei44m0.wvIbPei44m0',
        'sender': {
            'name': 'users/112642549360622779129',
            'displayName': 'Shannon Thompson',
            'avatarUrl': 'https://lh3.googleusercontent.com/a/AGNmyxZCl43e3Iuhwhba4loLFX99HOIIgafA-0PYvVhh=k-no',
            'email': 'shannon@hennekelabs.com',
            'type': 'HUMAN',
            'domainId': '1hzekco'
        },
        'createTime': '2023-04-24T14:49:45.938847Z',
        'text': '/poet Explain how calculus is useful',
        'annotations': [{
            'type': 'SLASH_COMMAND',
            'startIndex': 0,
            'length': 5,
            'slashCommand': {
                'bot': {
                    'name': 'users/102211606836959565645',
                    'displayName': 'ChatGPT Bot',
                    'avatarUrl': 'https://lh6.googleusercontent.com/proxy/yNIjT7WKl3HxSm-u468-yf4LJHPpTC9IoXHhtCxnDSmiaJsosj3rrIXUZgLhU3mhVmsfbKaCujIhNI9nywD4btdYsqKPuMeIqHqLw1cUSok0dDV4V_ap',
                    'type': 'BOT'
                },
                'type': 'INVOKE',
                'commandName': '/poet',
                'commandId': '3'
            }
        }],
        'thread': {
            'name': 'spaces/7IpBtkAAAAE/threads/wvIbPei44m0',
            'retentionSettings': {
                'state': 'PERMANENT'
            }
        },
        'space': {
            'name': 'spaces/7IpBtkAAAAE',
            'type': 'DM',
            'singleUserBotDm': True,
            'spaceThreadingState': 'UNTHREADED_MESSAGES',
            'spaceType': 'DIRECT_MESSAGE',
            'spaceHistoryState': 'HISTORY_ON'
        },
        'argumentText': ' Explain how calculus is useful',
        'slashCommand': {
            'commandId': '3'
        },
        'retentionSettings': {
            'state': 'PERMANENT'
        },
        'messageHistoryState': 'HISTORY_ON'
    },
    'user': {
        'name': 'users/112642549360622779129',
        'displayName': 'Shannon Thompson',
        'avatarUrl': 'https://lh3.googleusercontent.com/a/AGNmyxZCl43e3Iuhwhba4loLFX99HOIIgafA-0PYvVhh=k-no',
        'email': 'shannon@hennekelabs.com',
        'type': 'HUMAN',
        'domainId': '1hzekco'
    },
    'space': {
        'name': 'spaces/7IpBtkAAAAE',
        'type': 'DM',
        'singleUserBotDm': True,
        'spaceThreadingState': 'UNTHREADED_MESSAGES',
        'spaceType': 'DIRECT_MESSAGE',
        'spaceHistoryState': 'HISTORY_ON'
    },
    'configCompleteRedirectUrl': 'https://chat.google.com/api/bot_config_complete?token=AESOpNNO-C2kKHvFtpVeIzJMPHZTsTiGN3mBmkBZhCPA3WxiXOwqwfMu0aluhleBQF8Huxw6fib3pY3z4R1-3k1WyOaDHYB6izlpnDM-lfknVr7KoTwnQ5mMX1othULlB6i_kW5GBY1HJlQRLnc9HuV92g%3D%3D',
    'common': {
        'userLocale': 'en',
        'hostApp': 'CHAT'
    }
}
```