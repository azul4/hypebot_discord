/* Old Conventions
const fs = require('node:fs');
const path = require('node:path');
const { REST, Routes, Client, Collection, Events, GatewayIntentBits } = require('discord.js');
*/

//Modern conventions
import fs from 'node:fs'
import path from 'node:path'
import { REST, Routes, Client, Collection, Events, GatewayIntentBits } from 'discord.js'
import {registerCommands} from "./commands/hi.js"
require('dotenv').config();
console.log("dotenv 설정 완료");

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages] });
const commands = [];
client.commands = new Collection();

const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
  const filePath = path.join(commandsPath, file);
  const command = require(filePath);

  if ('data' in command && 'execute' in command) {
    client.commands.set(command.data.name, command);
    commands.push(command.data.toJSON());
  } else {
    console.log(`[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`);
  }
}
console.log("hello")
const rest = new REST( {version: '10' }).setToken(process.env.DISCORD_TOKEN);

//즉시실행 함수
(async () => {
  try {
    console.log(`Started refreshing ${commands.length} application (/) commands.`);

    // The put method is used to fully refresh all commands in the guild with the current set
    const data = await rest.put(
      Routes.applicationGuildCommands(process.env.CLIENT_ID, process.env.TO_REGISTER_GUILD),
      { body: commands },
    );

    console.log(`Successfully reloaded ${data.length} application (/) commands.`);
  } catch (error) {
    // And of course, make sure you catch and log any errors!
    console.error(error);
  }
})();


// Slash Command 추가
registerCommands(process.env.DISCORD_TOKEN, process.env.CLIENT_ID, process.env.TO_REGISTER_GUILD);


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`)
});

// 메시지를 받으면 호출되는 함수
client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  //./commands에서 커맨드 찾아서 저장
  const command = client.commands.get(interaction.commandName);

  try {
    await command.execute(interaction);
  } catch(e) {
    await interaction.reply( {
      content: 'There was an error',
    })
  }
});

client.login(process.env.DISCORD_TOKEN);