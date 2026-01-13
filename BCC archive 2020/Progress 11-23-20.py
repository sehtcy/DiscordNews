import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


# settings a prefix command for the bot

@client.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)


# A clear command that refreshes the text channel


@client.event
async def on_ready():
    print('The Bot is on.')

    general_channel = client.get_channel(762725115905048599)
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Helping Users'))
    await general_channel.send('Hello and Welcome to the Server. To get started, type .commands')


# The bot turns on aiding the user to get started


@client.command(name='commands')
async def commands(ctx):
    myEmbed = discord.Embed(title="Commands", description="clear, version, news, news2, news3, gamenews, gamenews2, "
                                                          "gamenews3", color=0xffd700)
    myEmbed.add_field(name="The Bot Prefix:", value="The period symbol '.'", inline=False)
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='version')
async def version(ctx):
    myEmbed = discord.Embed(title="Current Version:", description="The bot is running v1.0", color=0x00ff00)
    myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/24/39/a6/2439a657128437d7b308e112f05c2b70.png")
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="October 7th, 2020", inline=False)
    myEmbed.add_field(name="Purpose:", value="Allowing users to access news quickly and effectively")
    myEmbed.add_field(name="More info:", value="https://github.com/scurry059/Discord-Bot")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='news')
async def news_command(ctx):
    myEmbed = discord.Embed(title="News Sources:", description="Top 5 News", color=0xff0000)
    myEmbed.add_field(name="Recommended Sources:", value="FOX, NBC, ABC, CBS, ESPN")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='news2')
async def new_command(ctx):
    myEmbed = discord.Embed(title="Second News:", description="Takes the most popular source and grabs the info",
    color=0xff0000)
    myEmbed.set_thumbnail(url="https://www.noisejournal.com/wp-content/uploads/2014/04/Fox-News-Logo.png")
    myEmbed.add_field(name="First link:", value="https://www.foxnews.com/politics/3rd-circuit-grants-trump-campaign"
    "-motion-for-expedited-review")
    myEmbed.add_field(name="Second link:", value="https://www.foxnews.com/politics/biden-to-tap-former-fed-chair"
    "-janet-yellen-as-treasury-secretary-report")
    myEmbed.add_field(name="Third link:", value="https://www.foxnews.com/us/fbi-threats-georgia-election-officials"
    "-voter-fraud-allegations")
    myEmbed.add_field(name="Fourth link:", value="https://www.foxnews.com/us/nj-gov-phil-murphy-coronavirus"
    "-restaurant-outdoor-dining")
    myEmbed.add_field(name="Fifth link:", value="https://www.foxnews.com/politics/trump-republicans-demand-signature"
    "-matching-in-georgia-recount-but-raffensperger-says-doing-so-is-impossible")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='news3')
async def new_command(ctx):
    myEmbed = discord.Embed(title="Current Topics:", description="Topics Available for the user", color=0xff0000)
    myEmbed.add_field(name="The Topics are listed:", value="Sports, Music, Health")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


# The end of all news commands

@client.command(name='gamenews')
async def news_command(ctx):
    myEmbed = discord.Embed(title="Gaming News Sources:", description="Top 5 Gaming News", color=0xff0000)
    myEmbed.add_field(name="Recommended Sources:", value="IGN, Xbox Wire, Nintendo Life, Game Informer, Polygon")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='gamenews2')
async def new_command(ctx):
    myEmbed = discord.Embed(title="Second News:", description="Takes the most popular source and grabs the info",
    color=0xff0000)
    myEmbed.set_thumbnail(url="https://www.userlogos.org/files/logos/zahnjin/ign_logo_plain.png")
    myEmbed.add_field(name="First link:", value="https://www.ign.com/articles/the-croods-a-new-age-review")
    myEmbed.add_field(name="Second link:", value="https://www.ign.com/videos/tomb-raider-reloaded-teaser-trailer")
    myEmbed.add_field(name="Third link:", value="https://www.ign.com/articles/cyberpunk-2077-physical-copies-appear"
    "-to-be-in-the-wild-so-beware-of-spoilers")
    myEmbed.add_field(name="Fourth link:", value="https://www.ign.com/videos/neo-the-world-ends-with-you-official"
    "-announcement-trailer")
    myEmbed.add_field(name="Fifth link:", value="https://www.ign.com/videos/cyberpunk-2077-11-burning-questions"
    "-answered")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


@client.command(name='gamenews3')
async def new_command(ctx):
    myEmbed = discord.Embed(title="Current Gaming Topics:", description="Topics Available for the user", color=0xff0000)
    myEmbed.add_field(name="The Topics are listed:", value="NVIDIA, Intel, AMD")
    myEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')

    await ctx.message.channel.send(embed=myEmbed)


# The end of all gaming commands


client.run('Insert Token here')
# Allows the bot to actually run
