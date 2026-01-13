@client.event
async def on_message(message):
    if message.content == 'What is the current version?':
        general_channel = client.get_channel(762725115905048599)

        myEmbed = discord.Embed(title="Current Version", description="The bot is running v1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="October 7th, 2020", inline=False)
        myEmbed.set_author(name="Seth")

        await general_channel.send(embed=myEmbed)
