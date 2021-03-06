from discord_webhook import DiscordWebhook, DiscordEmbed

def errorHook(error, page):
    hook = DiscordWebhook(url="https://discord.com/api/webhooks/817776875106992159/b07AjZfor84Av5kZGIs34_jhmffwMUoMmEnWW3vgatn1FOK3LZhSePhVXsKDxJZDkXVL")  
    embed = DiscordEmbed(title="Web error!", description="Na webu se vyskytl error %s <@406894015204687872>" % (error,), color = 0xff0000)
    embed.add_embed_field(name="Page", value=page)
    hook.add_embed(embed)
    responce = hook.execute()
