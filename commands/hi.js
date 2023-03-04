import { SlashCommandBuilder } from 'discord.js';

export const HiCommand = {
    data: new SlashCommandBuilder()
        .setName('안녕하세요')
        .setDescription('다시 인사해 줄 거에요.'),

    async execute(interaction) {
        await interaction.reply('인사잘한다')
    }
}

