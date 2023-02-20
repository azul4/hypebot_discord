const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
console.log("hello")


// Slash Command 추가
registerCommands(process.env.DISCORD_BOT_TOKEN, process.env.CLIENT_ID, process.env.TO_REGISTER_GUILD);


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`)
});

// 메시지를 받으면 호출되는 함수
client.on('interactionCreate', async interaction => {
  // Original: https://discordjs.guide/interactions/replying-to-slash-commands.html#receiving-interactions
  if (!interaction.isCommand()) return;

  if (interaction.commandName === '안녕하세요') {
      await interaction.reply('인사 잘한다~');
  }
});

client.login(token);