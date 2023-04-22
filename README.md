# Build a Google Chat Bot Powered by ChatGPT
You already use ChatGPT in the browser, but how do you incorporate the technology into your own product? 

This code lab will walk you through all the steps to create a Google Chat bot that is powered by ChatGPT and fully customizable to your desires.

## Prerequisites
1. Google Workspace account with Google Chat enabled.
2. [Google Cloud account](https://console.cloud.google.com/), with billing enabled, or free trial.
3. [OpenAI account](https://platform.openai.com/), with billing enabled, or free trial credits.
4. Experience with Python.

## What You'll Learn
By the end of the code lab you will have learned:
- How to set up and configure a Google Chat bot
- How to set up a Google Cloud Function and trigger it from Google Chat
- How to protect your bot's code from unauthorized traffic
- How to use the Chat and Image APIs from OpenAI to make your bot brilliant
- How to use slash commands to give your bot specific skills
- How to use Google Cloud Datastore to track a history of messages
- How to create cards and dialogs to improve the UX of your bot
- How to combine everything you've built into a brand new skill for your bot

## Structure and Progression
The lab is split in nine modules that are designed to be completed in order, with each one building on the work from the previous one.

In the first module you'll build a basic chat bot. Each subsequent module will add additional functionality to the bot. At the end of each module you should have a working bot which you can test to verify all the steps were completed successfully.

Each module also contains a repo which is how your code should look *after* completing all the steps in the module. If you ever get stuck, you can compare your code to the repo code to track down any issues.

> As an alternative, you can start at any module and use the repo code from the previous module as the starting point for your project.

## Modules

- [Module 1 - Build a Basic Chat Bot](mod_1_chat#readme)<br />
Set up and configure a basic bot for Google Chat.

- [Module 2 - Add OpenAI](mod_2_openai#readme)<br />
Use ChatGPT to reply to incoming messages.

- [Module 3 - Verify Requests](mod_3_verify#readme)<br />
Verify requests before processing messages. 

- [Module 4 - Add Datastore](mod_4_datastore#readme)<br />
Give your bot memory by tracking a history of messages.

- [Module 5 - Add Slash Commands](mod_5_commands#readme)<br />
Give your bot special skills with custom commands.

- [Module 6 - Add Image Support](mod_6_images#readme)<br />
Add support for image generation using DALL·E 2. 

- [Module 7 - Collect API Key](mod_7_apiKey#readme)<br />
Process messages with each user's OpenAI API key.

- [Module 8 - Add a Dialog](mod_8_dialogs#readme)<br />
Improve the setup experience by using a dialog.

- [Module 9 - Interactive Story](mod_9_story#readme)<br />
Build a "Choose Your Own Adventure" story generator.

## References
**Google Chat API**
- [Documentation](https://developers.google.com/chat/how-tos/apps-develop)
- [Event Reference](https://developers.google.com/chat/api/reference/rest/v1/Event)
- [Card Reference](https://developers.google.com/chat/api/reference/rest/v1/cards)
- [Card Builder](https://gw-card-builder.web.app/)
- [Text Formatting Reference](https://developers.google.com/chat/api/guides/message-formats/cards#card_text_formatting)
- [Publish Google Chat apps](https://developers.google.com/chat/how-tos/apps-publish)

<br />

**OpenAI**
- [Chat API](https://platform.openai.com/docs/guides/chat)
- [Image API](https://platform.openai.com/docs/guides/images)
- [Error Codes](https://platform.openai.com/docs/guides/error-codes)

<br />

**Google Cloud**
- [Cloud Functions - Write HTTP functions](https://cloud.google.com/functions/docs/writing/write-http-functions)
- [Datastore ndb Documentation](https://googleapis.dev/python/python-ndb/latest/)


## Authors

* **Cameron Henneke** - [GQueues](https://www.gqueues.com)

<br />

## Sponsor

This code lab was built by the makers of GQueues.

<a href="https://www.gqueues.com">
<img 
    src="https://app.gqueues.com/images/5.7.1/gqueues_logo.svg"
    alt="GQueues"
    width="200">
    </a>

### Prioritize your team’s work with a task manager that helps you get more out of Google Workspace.

<br />
<br />

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

