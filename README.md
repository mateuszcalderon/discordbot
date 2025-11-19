<div align="center">
  <h1>da Vinci Discord Bot</h1>
</div>

da Vinci is a clean but meaningful Discord bot built with Python and discord.py,
developed following the best practices it includes fun user interaction commands,
automated server events, and an organized and extensible architecture.

## Features:
#### Slash Commands:
  - **/coin** – Flip a coin.
  - **/dice** – Roll a six‑sided dice.
  - **/emoji** – Click a button to receive a random emoji.
  - **/ping** – Check the bot’s latency.
  - **/ship** – Calculate the love percentage between two users.

#### Automatic Events:
  - Welcomes new members with a message.
  - Sends a farewell message when a member leaves.
  - Announces when a new text channel is created.

#### Secure Token Handling:
  - Uses a ` .env ` file to store the Discord bot token securely.
  - Includes error handling to prevent the bot from running without a valid token.

## Project Structure:
` discordbot/
├── main.py # Main settings and commands for the Discord bot.
├── cogs/
│ └── events.py # All event-related functionalities for the Discord bot.
├── .env # Environment variables.
└── .gitignore # Excludes unwanted files. `

## License:
This project is licensed under the [MIT License](https://github.com/mateuszcalderon/discordbot/blob/main/LICENSE).
