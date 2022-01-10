const fs = require('fs');
const { Client, Collection, Intents } = require('discord.js');
const { token, mongodbUsername, mongodbPassword, mongodbName,mongodbCollection } = require('./config.json');
const { MongoClient } = require('mongodb');

const uri = `mongodb+srv://${mongodbUsername}:${mongodbPassword}@cluster0.z5ix9.mongodb.net/${mongodbName}?retryWrites=true&w=majority`;
const mongoClient = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
mongoClient.connect(err => {
  const collection = mongoClient.db(mongodbName).collection(mongodbCollection);
  // perform actions on the collection object
  console.log("connected to db");
  mongoClient.close();
});

const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	// Set a new item in the Collection
	// With the key as the command name and the value as the exported module
	client.commands.set(command.data.name, command);
}

client.once('ready', () => {
	console.log('Ready!');
});

client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
	}
});

client.login(token);