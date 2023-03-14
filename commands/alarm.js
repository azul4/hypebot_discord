import { SlashCommandBuilder } from 'discord.js';

export const Alarm10pm = {
    data: new SlashCommandBuilder()
        .setName('10시 알람')
        .setDescription('다시 인사해 줄 거에요.'),

    async execute(interaction) {
        await interaction.reply('인사잘한다')
    }
}

