class Card:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.rarity = kwargs.get('rarity')
        self.positionEffect=kwargs.get('positionEffect')
        self.type=kwargs.get('type')
    


    def display(self):
        print('-----------------------------------------')
        print("Title:", self.title)
        print("Description:", self.description)
        print("rarity:", self.rarity)
        print("positionEffect:", self.positionEffect)
        print("type:", self.type)
        print('-----------------------------------------')
        # 打印其他属性...

cardLibrary={}
# 染血的野蛮兽人
cardLibrary['0001'] = Card(title="残忍爪击", description="造成3点伤害", rarity="normal",positionEffect="",type=["伤害牌"])
cardLibrary['0002'] = Card(title="蓄力一击", description="[额外伤害臂章]+3（你的下一张被结算的伤害牌伤害+3）", rarity="normal",positionEffect="队中：该卡同时被视为伤害牌，造成1点伤害",type=["臂章牌"])
cardLibrary['0003'] = Card(title="染血的双刃剑", description="[染血臂章]+2(本回合你所有的伤害牌伤害+2，结算时对你自身造成2点伤害)", rarity="normal",positionEffect="对位normal卡片：该卡同时被视为伤害牌，造成1点伤害",type=["臂章牌"])
cardLibrary['0004'] = Card(title="野蛮投石", description="造成2点伤害.当此卡于主要阶段被返回到牌组底部时，造成1点伤害", rarity="normal",positionEffect="对位Uncommon卡片：造成2点伤害",type=["伤害牌"])
cardLibrary['0005'] = Card(title="连击", description="造成1点伤害.如果对位卡片触发了对位效果，额外造成4点伤害", rarity="normal",positionEffect="对位Uncommon卡片：造成1点伤害",type=["伤害牌"])


cardLibrary['0006'] = Card(title="兽群的围攻", description="你获得一个结界，每当你对对手造成伤害时，该伤害+1", rarity="Uncommon",positionEffect="",type=["结界牌"])
cardLibrary['0007'] = Card(title="盾反", description="此卡结算前对对方造成你本回合所受的总伤害。造成1点伤害", rarity="Uncommon",positionEffect="对位Rare卡片：[染血臂章]+3，此卡同时视为臂章牌。",type=["伤害牌"])
cardLibrary['0008'] = Card(title="染血的群斗", description="造成2点伤害.如果此卡结算时造成了大于等于5点伤害:[染血臂章]+3，此卡同时视为臂章牌", rarity="Uncommon",positionEffect="对位UR卡片：造成5点伤害。",type=["伤害牌"])

cardLibrary['0009'] = Card(title="血流成河", description="造成1点伤害，[染血臂章]+3", rarity="Rare",positionEffect="队中：[额外伤害臂章]+3",type=["伤害牌","臂章牌"])
cardLibrary['0010'] = Card(title="嗜血", description="对对方造成x点伤害，x等于你的[染血臂章]计数。造成1点伤害", rarity="Rare",positionEffect="队中：[染血臂章]+3，此卡同时视为臂章牌",type=["伤害牌"])
cardLibrary['0011'] = Card(title="染血的围猎", description="如果你的结算队列中只有伤害牌，造成5点伤害", rarity="Rare",positionEffect="队中：[额外伤害臂章]+3，此卡同时视为臂章牌",type=["伤害牌"])
cardLibrary['0012'] = Card(title="兽人的荣耀", description="本回合你每结算过一张臂章牌就造成4点伤害。造成1点伤害", rarity="Rare",positionEffect="对位Uncommon卡片：无效对位的卡片。",type=["伤害牌"])

cardLibrary['0013'] = Card(title="人体炸弹", description="造成3点伤害.当此卡于主要阶段被返回到牌组顶部时，你受到3点伤害", rarity="UR",positionEffect="队尾：造成5点伤害",type=["伤害牌"])
cardLibrary['0014'] = Card(title="弱肉强食", description="造成1点伤害，如果你的生命值高于对手，[额外伤害臂章]+5，此卡同时视为臂章牌。如果此卡结算时造成了大于等于5点伤害，造成3点伤害", rarity="UR",positionEffect="",type=["伤害牌"])
cardLibrary['0015'] = Card(title="残忍的理由", description="如果此卡结算时你受到了超过10点伤害，造成10点伤害并让此卡被视为伤害牌", rarity="UR",positionEffect="",type=[])


# 变异的虫群
cardLibrary['0016'] = Card(title="虫蛰", description="造成1点伤害，[变异能力]+2。如果此卡在主要阶段被返回牌组底部，[变异能力]+1", rarity="normal",positionEffect="",type=["能力牌","伤害牌"])
cardLibrary['0002'] = Card(title="虫群之力", description="如果本回合你的结算队列中有超过3张牌，造成5点伤害,此卡同时视为伤害牌。如果此卡在主要阶段被返回牌组底部，[变异能力]+1", rarity="normal",positionEffect="对位Rare牌：[变异能力]+3",type=[])
cardLibrary['0003'] = Card(title="能量吸取", description="无效对位的伤害牌", rarity="normal",positionEffect="队首:[变异能力]+1",type=[])
cardLibrary['0004'] = Card(title="吸血的本能", description="造成2点伤害，回复2点生命值，如果你的[变异能力]大于20，额外造成5点伤害", rarity="normal",positionEffect="队尾:[变异能力]+1",type=["伤害牌"])
cardLibrary['0005'] = Card(title="被污染的次元", description="[变异能力]+2。如果此卡对位的卡片触发了对位效果，[变异能力]+5", rarity="normal",positionEffect="对位Uncommon卡片：造成1点伤害",type=["能力牌"])


cardLibrary['0006'] = Card(title="惊骇的辐射", description="你获得一个结界，每当你结算能力牌时，该能力+1", rarity="Uncommon",positionEffect="对位UR牌：[变异能力]+5，此卡同时被视为能力牌",type=["结界牌"])
cardLibrary['0007'] = Card(title="诡异的愈合", description="如果你的[变异能力]大于等于5，[变异能力]-5并回复x点生命值，x等于你的变异能力", rarity="Uncommon",positionEffect="对位Rare卡片：无效该卡",type=[])
cardLibrary['0008'] = Card(title="蛰伏", description="如果本回合你的结算队列中没有伤害牌，恢复x点生命值，x为你结算队列中卡片数量乘以5", rarity="Uncommon",positionEffect="队首：[变异能力]+2，此卡同时被视为能力牌",type=[])

cardLibrary['0009'] = Card(title="血流成河", description="造成1点伤害，[染血臂章]+3", rarity="Rare",positionEffect="队中：[额外伤害臂章]+3",type=["伤害牌","臂章牌"])
cardLibrary['0010'] = Card(title="嗜血", description="对对方造成x点伤害，x等于你的[染血臂章]计数。造成1点伤害", rarity="Rare",positionEffect="队中：[染血臂章]+3，此卡同时视为臂章牌",type=["伤害牌"])
cardLibrary['0011'] = Card(title="染血的围猎", description="如果你的结算队列中只有伤害牌，造成5点伤害", rarity="Rare",positionEffect="队中：[额外伤害臂章]+3，此卡同时视为臂章牌",type=["伤害牌"])
cardLibrary['0012'] = Card(title="兽人的荣耀", description="本回合你每结算过一张臂章牌就造成4点伤害。造成1点伤害", rarity="Rare",positionEffect="对位Uncommon卡片：无效对位的卡片。",type=["伤害牌"])

cardLibrary['0013'] = Card(title="人体炸弹", description="造成3点伤害.当此卡于主要阶段被返回到牌组顶部时，你受到3点伤害", rarity="UR",positionEffect="队尾：造成5点伤害",type=["伤害牌"])
cardLibrary['0014'] = Card(title="弱肉强食", description="造成1点伤害，如果你的生命值高于对手，[额外伤害臂章]+5，此卡同时视为臂章牌。如果此卡结算时造成了大于等于5点伤害，造成3点伤害", rarity="UR",positionEffect="",type=["伤害牌"])
cardLibrary['0015'] = Card(title="残忍的理由", description="如果此卡结算时你受到了超过10点伤害，造成10点伤害并让此卡被视为伤害牌", rarity="UR",positionEffect="",type=[])
# ...

# 打印卡片的内容
for k,v in cardLibrary.items():
    cardLibrary[k].display()