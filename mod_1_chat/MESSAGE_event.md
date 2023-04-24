# MESSAGE event

Below is an example of the json sent by a bot for the standard MESSAGE event.

```
{
    'type': 'MESSAGE',
    'eventTime': '2023-04-24T14:32:30.748607Z',
    'message': {
        'name': 'spaces/7IpBtkAAAAE/messages/SUlZCne99Co.SUlZCne99Co',
        'sender': {
            'name': 'users/112642549360622779129',
            'displayName': 'Shannon Thompson',
            'avatarUrl': 'https://lh3.googleusercontent.com/a/AGNmyxZCl43e3Iuhwhba4loLFX99HOIIgafA-0PYvVhh=k-no',
            'email': 'shannon@hennekelabs.com',
            'type': 'HUMAN',
            'domainId': '1hzekco'
        },
        'createTime': '2023-04-24T14:32:30.748607Z',
        'text': 'Is this bot working?',
        'thread': {
            'name': 'spaces/7IpBtkAAAAE/threads/SUlZCne99Co',
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
        'argumentText': 'Is this bot working?',
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
    'configCompleteRedirectUrl': 'https://chat.google.com/api/bot_config_complete?token=AESOpNOHTnu6_FqLeIPAGD8mDbP3auY-csCySs3nd9FFxkbFlb6YhI9asIxctpvDuzAu6CNLa_rVMUtn-bTZKGyfqsfzD0PnGIqye15AGOByH8LVKj6P3mE8C6HTSyis60Qms2mb4cT6TQYShGjdq-Fd6g%3D%3D',
    'common': {
        'userLocale': 'en',
        'hostApp': 'CHAT'
    }
}
```