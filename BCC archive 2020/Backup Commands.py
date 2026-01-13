@client.command(name='help', aliases=['h'])
async def news_command(ctx):
    await ctx.channel.send("Here are the following commands: news, news2, news3, gamenews, gamenews2, gamenews3, clear")


@client.command(name='news', aliases=['n', 'T5N'])
async def news_command(ctx):
    await ctx.channel.send("FOX, NBC, ABC, CBS, ESPN")


@client.command(name='news2', aliases=['topsource', 'tsource'])
async def new_command(ctx):
    await ctx.channel.send("FOX has the following: "
                           "1. https://www.foxnews.com/politics/2020-election-ballots-cast-so-far"

                           "2. https://www.foxnews.com/politics/biden-staff-misspoke-60-minutes-free-public-college"
                           "-cost "

                           "3. https://www.foxnews.com/politics/trump-biden-harris-pence-campaign-trail-october-26"

                           "4. https://www.foxbusiness.com/markets/us-stocks-october-26-2020"

                           "5. https://www.foxnews.com/media/hillary-clinton-birthday-tweet-future-president-draws"
                           "-mockery")


@client.command(name='news3', aliases=['topic'])
async def new_command(ctx):
    await ctx.channel.send("These are the topics: Sports, Music, and Health")


@client.command(name='gamenews', aliases=['g', 'GT5N'])
async def news_command(ctx):
    await ctx.channel.send("IGN, Xbox Wire, Nintendo Life, Game Informer, Polygon")


@client.command(name='gamenews2', aliases=['gametopsource', 'gtsource'])
async def new_command(ctx):
    await ctx.channel.send("Nintendo Life has the following: "
                           "1. https://www.nintendolife.com/reviews/switch-eshop/supraland "

                           "2. https://www.nintendolife.com/reviews/switch-eshop/vigil_the_longest_night"

                           "3. https://www.nintendolife.com/news/2020/10"
                           "/the_snes_encyclopedia_is_an_exhaustive_resource_for_nintendo_fans "

                           "4. https://www.nintendolife.com/news/2020/10"
                           "/anniversary_dig_out_the_plastic_and_reform_the_band_-_rock_band_3_turns_10_today "

                           "5. https://www.nintendolife.com/news/2020/10"
                           "/random_mario_kart_music_apparently_helps_with_your_homework")


@client.command(name='gamenews3', aliases=['gametopic'])
async def new_command(ctx):
    await ctx.channel.send("These are the topics: NVIDIA, Intel, and AMD")
