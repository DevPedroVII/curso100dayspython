const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === '!clear') {
    msg.channel.bulkDelete(100);
    msg.channel.send('Chat limpo!').then(message => message.delete({ timeout: 2000 }));
  }
});

client.login('SEU_TOKEN_AQUI');
