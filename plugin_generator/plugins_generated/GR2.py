import discord
from discord.ext import commands
import checks
import asyncio

class GR2():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='GR2', pass_context=True)
    async def choice(self, ctx):
        '''1=yes 2=no'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('1=yes 2=no')
        await self.bot.add_reaction(msg, '\U0001f499')
        await self.bot.add_reaction(msg, '\U0001f49a')

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f499', '\U0001f49a'], message=msg)
            if res.reaction.emoji == '\U0001f499':
                await self.bot.remove_reaction(msg, '\U0001f499', res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Member'))
            elif res.reaction.emoji == '\U0001f49a':
                await self.bot.remove_reaction(msg, '\U0001f49a', res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='NON Member'))


def setup(bot):
    bot.add_cog(GR2(bot))