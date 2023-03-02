import { SlashCommandBuilder } from 'discord.js';

export const HiCommand = {
    data: new SlashCommandBuilder()
        .setName('안녕하세요')
        .setDescription('해당 명령어를 실행해보세요!ㅋㅋ'),

    async execute(interaction) {
        await interaction.reply('인사잘한다')
    }
}