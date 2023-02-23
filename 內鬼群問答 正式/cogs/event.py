import json
import os
import random
import discord
#-------------------------------------------------------------------------------
from core.classes import Cog_Extension
from discord.ext import commands
import asyncio
import json
import datetime

class event(Cog_Extension):

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.command()
    
    async def 開始 (self,ctx):
        with open('問答設置(內鬼群).json','r',encoding='utf8') as jfile:
            ####   問答設置(測試群)   問答設置(內鬼群)   問答設置(內鬼群)延長    ######
            config = json.load(jfile)


        rang = int(len(config['問答集']))


        knowans = []
        playerpoint = {}
        answer = {}
        回 = config['按鈕回覆內容']
        秒 = config['每題間隔秒數']
        秒 = int(秒)
        shownum = config['結果呈現']
        shownum = int(shownum)


        embed=discord.Embed(title=f"正在讀取題目，暫時不接受答案...", color=discord.Colour.random())


        
        ba = discord.ui.Button(label='A',style=discord.ButtonStyle.blurple)
        bb = discord.ui.Button(label='B',style=discord.ButtonStyle.blurple)
        bc = discord.ui.Button(label='C',style=discord.ButtonStyle.blurple)
        bd = discord.ui.Button(label='D',style=discord.ButtonStyle.blurple)
        
        async def a_callback(inter):
            if inter.user.id not in knowans:
                
                if x1['答案'] == 'A':
                    
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 1
                        answer[str(inter.user.id)] = []
                    else:
                        playerpoint[str(inter.user.id)] += 1
                        
                else:
                    
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 0
                        answer[str(inter.user.id)] = []
                    
                knowans.append(inter.user.id)
                answer[str(inter.user.id)] += [f'{cur} - A']
                await inter.response.send_message(f'',ephemeral=True) 
                
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
                
        async def b_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'B':
                    
                    #await inter.response.send_message(f'{回}',ephemeral=True)
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 1
                        answer[str(inter.user.id)] = []
                    else:
                        playerpoint[str(inter.user.id)] += 1
                else:
                    
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 0
                        answer[str(inter.user.id)] = []
                        
                knowans.append(inter.user.id)
                answer[str(inter.user.id)] += [f'{cur} - B']
                await inter.response.send_message(f'',ephemeral=True) 
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        async def c_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'C':
                
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 1
                        answer[str(inter.user.id)] = []
                    else:
                        playerpoint[str(inter.user.id)] += 1
                else:
                
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 0
                        answer[str(inter.user.id)] = []
                        
                knowans.append(inter.user.id)
                answer[str(inter.user.id)] += [f'{cur} - C']
                await inter.response.send_message(f'',ephemeral=True) 
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
                
        async def d_callback(inter):
            if inter.user.id not in knowans:
                if x1['答案'] == 'D':
                
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 1
                        answer[str(inter.user.id)] = []
                    else:
                        playerpoint[str(inter.user.id)] += 1
                else:
                    
                    if str(inter.user.id) not in playerpoint:
                        playerpoint[str(inter.user.id)] = 0
                        answer[str(inter.user.id)] = []
                        
                knowans.append(inter.user.id)
                answer[str(inter.user.id)] += [f'{cur} - D']
                await inter.response.send_message(f'',ephemeral=True) 
                
            else:
                await inter.response.send_message(f'這題你已經回答過囉!',ephemeral=True)
        ba.callback = a_callback
        bb.callback = b_callback
        bc.callback = c_callback
        bd.callback = d_callback
        view = discord.ui.View(timeout=None)
        view.add_item(ba)
        view.add_item(bb)
        view.add_item(bc)
        view.add_item(bd)
        
        sendchanid = config['遊戲傳送頻道ID'] 
        sendchannel = self.bot.get_channel(int(sendchanid))
        wmsg = await sendchannel.send(embed=embed)
        await asyncio.sleep(5)
        
        cur = 0;
        
        for x1 in config['問答集']:
        
            if cur != 0 :
                ba.disabled = True
                bb.disabled = True
                bc.disabled = True
                bd.disabled = True
                await wmsg.edit(embed=embed,view=view)
                await asyncio.sleep(2)
                
            ba.disabled = False
            bb.disabled = False
            bc.disabled = False
            bd.disabled = False    
            cur = cur + 1
            q1 = x1['題目']
            q2 = x1['A']
            q3 = x1['B']
            q4 = x1['C']
            q5 = x1['D']
            q6 = str(x1['圖片網址'])
            x1embed=discord.Embed(title=f"{config['嵌入標題']} - 第 {cur} 題", description=f"{q1}\n\n> Ａ：{q2}\n> Ｂ：{q3}\n> Ｃ：{q4}\n> Ｄ：{q5}", color=discord.Colour.random())
            x1embed.set_image(url=q6)
            x1embed.set_footer(text=f"每{秒}秒會切換下一題，願智慧之神祝福各位！")
            await wmsg.edit(embed=x1embed,view=view)
            await asyncio.sleep(秒)
            knowans.clear()
        embed=discord.Embed(title=f"{config['嵌入標題']}", description=f"遊戲已經結束囉!", color=discord.Colour.random())
        ba.disabled = True
        bb.disabled = True
        bc.disabled = True
        bd.disabled = True
        await wmsg.edit(embed=embed,view=view)
        
        sortedlist = {}
        
        
        def get_sortest_key(a: dict, o: dict):
            v = None
            k = None
            for key, value in a.items():
                if v is None:
                    v = value
                    k = key
                    continue
                if v < value:
                    v = value
                    k = key
            o.update({k: v})
            a.pop(k)
            if a:
                get_sortest_key(a, o)
            else:
                return
        
        get_sortest_key(playerpoint,sortedlist)
        
        print(sortedlist)
        print(answer)
        
        point2 = ''
        
        for ansersss in answer:
            point2 = point2+f"<@{ansersss}> — {sortedlist[ansersss]}：{answer[ansersss]}\n"
            
        print('-----作答紀錄\n')
        print(point2)
        
        
        point = ''
        max = 0
        
        maxnum = len(answer)
        
        if maxnum > shownum :
            maxnum = shownum
        
        for ansersss in sortedlist:
            if max < maxnum :
                point = point+f"<@{ansersss}> — {sortedlist[ansersss]}\n"
                max = max + 1
                
        conchannel = config['遊戲統計訊息傳送頻道ID']
        dechannel = self.bot.get_channel(int(conchannel))
        embed=discord.Embed(title="遊戲結果統計", description=f"{point}", color=discord.Colour.random())
        await dechannel.send(embed=embed)
        
        print('-----遊戲結果統計\n')
        print(point)
        
        conchannel = config['遊戲統計訊息傳送頻道ID']
        dechannel = self.bot.get_channel(int(conchannel))
        embed=discord.Embed(title="作答紀錄", description=f"{point2}", color=discord.Colour.random())
        await dechannel.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(event(bot))
