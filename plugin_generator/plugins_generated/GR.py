import discord
from discord.ext import commands
import checks
import asyncio

class GR():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='GR', pass_context=True)
    async def choice(self, ctx):
        '''Please Click The Emoji To Choose: Blue= Member. Green= NON Member.'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('Please Click The Emoji To Choose: \U0001f499= Member. \U0001f49a= NON Member.')
        await self.bot.add_reaction(msg, '\U0001f499')
        await self.bot.add_reaction(msg, '\U0001f49a')

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f499', '\U0001f49a'], message=msg)
            if res.reaction.emoji == '\U0001f499':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Member'))
            elif res.reaction.emoji == '\U0001f49a':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='NON Member'))


def setup(bot):
    bot.add_cog(GR(bot))