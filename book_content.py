# -*- coding: utf-8 -*-
"""
Old, Old Tales Retold — transcribed page-by-page from the author's
photographs of the Volland Edition (P. F. Volland Company, 1923),
illustrated by Frederick Richardson.

Text is kept faithful to the photographed copy. Only obvious printer's
errors (a dropped word, a missing closing quote/period) have been
silently corrected.

Markup conventions for the builder:
  - A page-chunk is a list of blocks.
  - A block starting with "> " on every line is a verse / refrain block
    (lines kept separate, indented).
  - [[BIG:...]] / [[MED:...]] / [[WEE:...]] reproduce the original's
    graded capital sizes for the Three Bears' voices.
"""

BOOK_TITLE = "Old, Old Tales Retold"
BOOK_SUBTITLE = "Eight Best-Beloved Folk Stories for Children"
ILLUSTRATOR = "Frederick Richardson"

DEDICATION = (
    "Because he planned this book upon his knowledge of what children "
    "love and of the changeless popularity of the old, old stories it "
    "presents, it is appreciatively dedicated to"
)
DEDICATION_TO = "P. F. V."

INTRO_TITLE = "To All Children Who Love Stories"
INTRO_PAGES = [
    [
        "Long, long ago there were no story books for children. But the children of those days loved the same kind of stories that you do today. All their stories, however, were told to them, not read aloud. Some of the very best of the stories which they heard were afterward written down and are here in this book.",
        "We do not know who first told many of these old, old stories. But we can imagine the way some of them came into existence. Let us pretend that many hundreds of years ago there was a good mother, and that early one cold winter evening her children gathered about her and one of them said:",
        "“Mother, please tell us a story.”",
        "Of course, the mother knew many stories, and had told all of them many times to her children. But that did not make any difference. Children liked to hear stories retold then just as you do today.",
    ],
    [
        "Some people wonder why these simple folk-tales have been loved by so many boys and girls. Isn’t it because they are happy stories? You like the days best through which you feel like singing; through which you smile and laugh and are busy. All these stories seem to be part of the cheerfulness of long ago.",
        "Another reason why these stories are loved is because of the wonderful humor in them. Not only are the characters happy and active, but they also have something in them which will make you chuckle inside. To begin with, all of the stories happened “once upon a time” in the happy land of “Let’s Pretend.” And the happenings in this land are not as serious or as solemn as they are in our every-day world. In the “Land of Let’s Pretend” a great deal of fun happens where it is not expected. Animals always talk in this “Land of Let’s Pretend,” and when animals talk the way these do, the stories are sure to be full of fun.",
    ],
]

STORIES = [
    {
        "title": "The Three Bears",
        "title_plate": 8,
        "vignette_page": 9,
        "pages": [
            ([
                "In a far-off country, once upon a time, there was a little girl who was called Goldilocks because of her beautiful golden curls.",
                "Goldilocks loved to romp and play. She loved to run into the woods to gather wild flowers, or to chase butterflies through the open fields.",
                "One day she ran here and she ran there, until at last she found herself in a strange and lonely wood. In the wood she saw a snug little house in which three bears lived. But Goldilocks did not know that three bears lived in this house. One was a Great Big Bear, and one was a Middle-sized bear, and one was a Wee Little Bear.",
                "The door of the little house was open; so Goldilocks peeped in and saw that it was quite empty. She stepped inside to look about a bit; no one was home. The three bears had just gone out for a walk. They had left their three bowls of porridge on the table to cool.",
            ], 10),
            ([
                "The porridge smelled very good, and Goldilocks thought that she would like to taste it. So she tasted the porridge in the great big bowl, which belonged to the Great Big Bear, but she found it too hot.",
                "Then she tasted the porridge in the middle-sized bowl, which belonged to the Middle-sized Bear, but she found it too cold.",
                "Then she tasted the porridge in the wee little bowl, which belonged to the Wee Little Bear. This porridge was just right, and she ate it all.",
                "Goldilocks then looked about the room and saw three chairs. She thought she would try the great big chair, which belonged to the Great Big Bear, but she found it too hard.",
                "She then tried the middle-sized chair, which belonged to the Middle-sized Bear, but she found it too soft.",
                "So she tried the wee little chair, which belonged to the Wee Little Bear, and she found it just right. But when she sat in the wee little chair, she broke it.",
            ], 12),
            ([
                "By this time Goldilocks was very tired, and she went into another room where she saw three beds. She tried the great big bed, which belonged to the Great Big Bear, but she found it too high at the head for her.",
                "Then she tried the middle-sized bed, which belonged to the Middle-sized Bear, but she found it too high at the foot for her.",
                "She then tried the wee little bed, which belonged to the Wee Little Bear, and she found it just right; so she lay down upon it and fell fast asleep.",
                "While Goldilocks was lying fast asleep, the three bears came home from their walk, and they went quickly to the kitchen to get their porridge.",
                "The Great Big Bear looked into his bowl and said in his great big voice, [[BIG:“SOMEBODY HAS BEEN TASTING MY PORRIDGE!”]]",
                "Then the Middle-sized Bear looked into her bowl and said in her middle-sized voice, [[MED:“SOMEBODY HAS BEEN TASTING MY PORRIDGE!”]]",
                "And the Wee Little Bear looked into his bowl and cried in his wee little voice, [[WEE:“SOMEBODY HAS BEEN TASTING MY PORRIDGE, AND HAS EATEN IT ALL UP!”]]",
            ], 14),
            ([
                "Then they looked at their chairs and the Great Big Bear said, [[BIG:“SOMEBODY HAS BEEN SITTING IN MY CHAIR!”]]",
                "And the Middle-sized Bear said, [[MED:“SOMEBODY HAS BEEN SITTING IN MY CHAIR!”]]",
                "And the Wee Little Bear cried, [[WEE:“SOMEBODY HAS BEEN SITTING IN MY CHAIR AND HAS BROKEN IT ALL TO PIECES!”]]",
            ], 16),
            ([
                "The three bears then went into their bedroom, and the Great Big Bear said, [[BIG:“SOMEBODY HAS BEEN LYING IN MY BED!”]]",
                "And the Middle-sized Bear said, [[MED:“SOMEBODY HAS BEEN LYING IN MY BED!”]]",
                "And the Wee Little Bear cried, [[WEE:“SOMEBODY HAS BEEN LYING IN MY BED, AND HERE SHE IS!”]]",
                "At that, Goldilocks woke in a fright and jumped out of the nearest window. She ran away as fast as her legs could carry her, and she never went again to the snug little house of the Three Bears.",
            ], 18),
        ],
    },
    {
        "title": "The Little Red Hen",
        "title_plate": 20,
        "vignette_page": 21,
        "pages": [
            ([
                "One day as the Little Red Hen was scratching in a field, she found a grain of wheat.",
                "“This wheat should be planted,” she said. “Who will plant this grain of wheat?”",
                "> “Not I,” said the Duck.\n> “Not I,” said the Cat.\n> “Not I,” said the Dog.",
                "“Then I will,” said the Little Red Hen. And she did.",
            ], 22),
            ([
                "Soon the wheat grew to be tall and yellow.",
                "“The wheat is ripe,” said the Little Red Hen. “Who will cut the wheat?”",
                "> “Not I,” said the Duck.\n> “Not I,” said the Cat.\n> “Not I,” said the Dog.",
                "“Then I will,” said the Little Red Hen. And she did.",
            ], 24),
            ([
                "When the wheat was cut, the Little Red Hen said, “Who will thresh this wheat?”",
                "> “Not I,” said the Duck.\n> “Not I,” said the Cat.\n> “Not I,” said the Dog.",
                "“Then I will,” said the Little Red Hen. And she did.",
            ], 26),
            ([
                "When the wheat was all threshed, the Little Red Hen said, “Who’ll take this wheat to the mill?”",
                "> “Not I,” said the Duck.\n> “Not I,” said the Cat.\n> “Not I,” said the Dog.",
                "“Then I will,” said the Little Red Hen. And she did.",
            ], 28),
            ([
                "She took the wheat to the mill and had it ground into flour. Then she said, “Who will make this flour into bread?”",
                "> “Not I,” said the Duck.\n> “Not I,” said the Cat.\n> “Not I,” said the Dog.",
                "“Then I will,” said the Little Red Hen. And she did.",
                "She made and baked the bread. Then she said, “Who will eat this bread?”",
                "> “Oh! I will,” said the Duck.\n> “And I will,” said the Cat.\n> “And I will,” said the Dog.",
                "“No, no!” said the Little Red Hen. “I will do that.” And she did.",
            ], 30),
        ],
    },
    {
        "title": "The House on the Hill",
        "title_plate": 32,
        "vignette_page": 33,
        "pages": [
            ([
                "Once upon a time a curly-tailed pig said to his friend the sheep, “I am tired of living in a pen. I am going to build me a house on the hill.”",
                "“Oh! may I go with you?” said the sheep.",
                "“What can you do to help?” asked the pig.",
                "“I can haul the logs for the house,” said the sheep.",
                "“Good!” said the pig. “You are just the one I want. You may go with me.”",
            ], 34),
            ([
                "As the pig and the sheep walked and talked about their new house, they met a goose.",
                "“Good morning, pig,” said the goose. “Where are you going this fine morning?”",
                "“We are going to the hill to build us a house. I am tired of living in a pen,” said the pig.",
                "“Quack! quack!” said the goose. “May I go with you?”",
                "“What can you do to help?” asked the pig.",
                "“I can gather moss, and stuff it into the cracks to keep out the rain.”",
                "“Good!” said the pig and the sheep. “You are just the one we want. You may go with us.”",
            ], 36),
            ([
                "As the pig and the sheep and the goose walked and talked about their new house, they met a rabbit.",
                "“Good morning, rabbit,” said the pig.",
                "“Good morning,” said the rabbit. “Where are you going this fine morning?”",
                "“We are going to the hill to build us a house. I am tired of living in a pen,” said the pig.",
                "“Oh!” said the rabbit, with a quick little jump. “May I go with you?”",
                "“What can you do to help?” asked the pig.",
                "“I can dig holes for the posts of your house,” said the rabbit.",
                "“Good!” said the pig and the sheep and the goose. “You are just the one we want. You may go with us.”",
            ], 38),
            ([
                "As the pig and the sheep and the goose and the rabbit walked and talked about their new house, they met a cock.",
                "“Good morning, cock,” said the pig.",
                "“Good morning,” said the cock. “Where are you going this fine morning?”",
                "“We are going to build us a house. I am tired of living in a pen,” said the pig.",
                "The cock flapped his wings three times. “Oh, Oh, Oh, O-O-Oh!” he crowed. “May I go with you?”",
                "“What can you do to help?” asked the pig.",
                "“I can be your clock,” said the cock. “I will crow every morning and waken you at daybreak.”",
                "“Good!” said the pig and the sheep and the goose and the rabbit. “You are just the one we want. You may go with us.”",
            ], 40),
            ([
                "Then they all went happily to the hill. The pig found the logs for the house. The sheep hauled them together. The rabbit dug the holes for the posts. The goose stuffed moss in the cracks to keep out the rain. And every morning the cock crowed to waken the workers. When at last the house was finished, the cock flew to the very top of it, and crowed and crowed and crowed.",
            ], 42),
        ],
    },
    {
        "title": "The Three Little Pigs",
        "title_plate": 44,
        "vignette_page": 45,
        "pages": [
            ([
                "Long ago there lived a pig who had three little pigs. The mother pig was very poor, and at last she had to send her little pigs out to seek their fortunes.",
                "The first little pig that went away met a man with a bundle of straw, and he said to him, “Please, man, give me that straw to build me a house.”",
                "The man gave the straw to the little pig. Then the pig built a house of the straw, and lived in the house.",
            ], 46),
            ([
                "By and by a wolf came along and knocked at the door of the little straw house.",
                "“Little pig, little pig, let me come in!” called the wolf.",
                "“No, no, by the hair of my chinny, chin, chin, I’ll not let you in,” answered the pig.",
                "“Then I’ll huff and I’ll puff and I’ll blow your house in,” said the wolf.",
                "So he huffed and he puffed and he blew the house in. Then he ate up the little pig.",
            ], 48),
            ([
                "The second little pig that went away met a man with a bundle of sticks, and he said to the man, “Please, man, give me your bundle of sticks to build me a house.”",
                "The man gave the sticks to the little pig. Then the pig built a house of the sticks, and lived in the house.",
                "By and by the wolf came along and knocked at the door of the little house of sticks.",
                "“Little pig, little pig, let me come in!” called the wolf.",
                "“No, no, by the hair of my chinny, chin, chin, I’ll not let you in,” answered the pig.",
                "“Then I’ll huff and I’ll puff and I’ll blow your house in,” said the wolf.",
                "So he huffed and he puffed and he blew the house in. Then he ate up the little pig.",
            ], 50),
            ([
                "The third little pig that went away met a man with a load of bricks, and he said to the man, “Please, man, give me your load of bricks to build me a house.”",
                "The man gave the bricks to the little pig. Then the pig built a house with the bricks and lived in the house.",
                "At last the wolf came along and knocked at the door of the brick house.",
                "“Little pig, little pig, let me come in!” called the wolf.",
                "“No, no, by the hair of my chinny, chin, chin, I’ll not let you in,” answered the pig.",
                "“Then I’ll huff and I’ll puff and I’ll blow your house in,” said the wolf.",
                "So he huffed and he puffed and he puffed and he huffed, but he could not blow the little brick house in.",
            ], 52),
            ([
                "The wolf rested a few minutes, and then he said, “Little pig, little pig, will you let just the tip of my nose in?”",
                "“No,” said the little pig.",
                "“Little pig, little pig, will you let just my paw in?”",
                "“No,” said the little pig.",
                "“Little pig, little pig, will you let just the tip of my tail in?”",
                "“No,” said the little pig.",
                "“Then I will climb up on the roof and come down through the chimney,” said the wolf.",
                "But the little pig made the fire very hot, so when the wolf came down the chimney he was burned up, and that was the end of him.",
                "The little pig then went and fetched his mother, and they still live happily in their little brick house.",
            ], 54),
        ],
    },
    {
        "title": "Chicken Licken",
        "title_plate": 56,
        "vignette_page": 57,
        "pages": [
            ([
                "One day when Chicken Licken was scratching among the leaves, an acorn fell out of a tree and struck her on the tail.",
                "“Oh,” said Chicken Licken, “the sky is falling! I am going to tell the King.”",
                "So she went along and went along until she met Henny Penny.",
                "“Good morning, Chicken Licken, where are you going?” said Henny Penny.",
                "“Oh, Henny Penny, the sky is falling and I am going to tell the King!”",
                "“How do you know that the sky is falling?” asked Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears, and a piece of it fell on my tail!” said Chicken Licken.",
                "“Then I will go with you,” said Henny Penny.",
                "So they went along and went along until they met Cocky Locky.",
            ], 58),
            ([
                "“Good morning, Henny Penny and Chicken Licken,” said Cocky Locky, “where are you going?”",
                "“Oh, Cocky Locky, the sky is falling, and we are going to tell the King!”",
                "“How do you know the sky is falling?” asked Cocky Locky.",
                "“Chicken Licken told me,” said Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears and a piece of it fell on my tail!” said Chicken Licken.",
                "“Then I will go with you,” said Cocky Locky, “and we will tell the King.”",
                "So they went along and went along until they met Ducky Daddles.",
            ], 60),
            ([
                "“Good morning, Cocky Locky, Henny Penny, and Chicken Licken,” said Ducky Daddles, “where are you going?”",
                "“Oh, Ducky Daddles, the sky is falling and we are going to tell the King!”",
                "“How do you know the sky is falling?” asked Ducky Daddles.",
                "“Henny Penny told me,” said Cocky Locky.",
                "“Chicken Licken told me,” said Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears, and a piece of it fell on my tail!” said Chicken Licken.",
                "“Then I will go with you,” said Ducky Daddles, “and we will tell the King.”",
                "So they went along and went along until they met Goosey Loosey.",
            ], 62),
            ([
                "“Good morning, Ducky Daddles, Cocky Locky, Henny Penny, and Chicken Licken,” said Goosey Loosey, “where are you going?”",
                "“Oh, Goosey Loosey, the sky is falling and we are going to tell the King!”",
                "“How do you know the sky is falling?” asked Goosey Loosey.",
                "“Cocky Locky told me,” said Ducky Daddles.",
                "“Henny Penny told me,” said Cocky Locky.",
                "“Chicken Licken told me,” said Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears, and a piece of it fell on my tail!” said Chicken Licken.",
                "“Then I will go with you,” said Goosey Loosey, “and we will tell the King!”",
                "So they went along and went along until they met Turkey Lurkey.",
            ], 64),
            ([
                "“Good morning, Goosey Loosey, Ducky Daddles, Cocky Locky, Henny Penny, and Chicken Licken,” said Turkey Lurkey, “where are you going?”",
                "“Oh, Turkey Lurkey, the sky is falling and we are going to tell the King!”",
                "“How do you know the sky is falling?” asked Turkey Lurkey.",
                "“Ducky Daddles told me,” said Goosey Loosey.",
                "“Cocky Locky told me,” said Ducky Daddles.",
                "“Henny Penny told me,” said Cocky Locky.",
                "“Chicken Licken told me,” said Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears, and a piece of it fell on my tail!” said Chicken Licken.",
                "“Then I will go with you,” said Turkey Lurkey, “and we will tell the King!”",
                "So they went along and went along until they met Foxy Woxy.",
            ], 66),
            ([
                "“Good morning, Turkey Lurkey, Goosey Loosey, Ducky Daddles, Cocky Locky, Henny Penny, and Chicken Licken,” said Foxy Woxy, “where are you going?”",
                "“Oh, Foxy Woxy, the sky is falling and we are going to tell the King!”",
                "“How do you know that the sky is falling?” asked Foxy Woxy.",
                "“Goosey Loosey told me,” said Turkey Lurkey.",
                "“Ducky Daddles told me,” said Goosey Loosey.",
                "“Cocky Locky told me,” said Ducky Daddles.",
                "“Henny Penny told me,” said Cocky Locky.",
                "“Chicken Licken told me,” said Henny Penny.",
                "“I saw it with my own eyes, I heard it with my own ears, and a piece of it fell on my tail,” said Chicken Licken.",
                "“Then we will run, we will run to my den,” said Foxy Woxy, “and I will tell the King.”",
                "So they all ran to Foxy Woxy’s den, but the foolish birds never came out again, and the King was never told that the sky was falling.",
            ], 68),
        ],
    },
    {
        "title": "The Old Woman and Her Pig",
        "title_plate": 70,
        "vignette_page": 71,
        "pages": [
            ([
                "An old woman found a crooked sixpence while sweeping her door-yard. “What shall I do with this sixpence?” she said. “I will go to the market and buy a pig.”",
                "Then the old woman went to the market and bought a pig. On her way home she came to a stile and then the pig would not go over the stile.",
                "> “Pig, pig, get over the stile,\n> Or I can not get home tonight.”",
                "But the pig would not.",
                "Then she went a little further and met a dog; and she said to the dog:",
                "> “Dog, dog, bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the dog would not.",
            ], 72),
            ([
                "Then she went a little farther and met a stick; and she said to the stick:",
                "> “Stick, stick, beat the dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the stick would not.",
                "Then she went a little farther and met a fire; and she said to the fire:",
                "> “Fire, fire, burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the fire would not.",
            ], 74),
            ([
                "Then she went a little farther and met some water; and she said to the water:",
                "> “Water, water, quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the water would not.",
                "Then she went a little farther and met an ox; and she said to the ox:",
                "> “Ox, ox, drink water;\n> Water won’t quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the ox would not.",
            ], 76),
            ([
                "Then she went a little farther and met a butcher; and she said to the butcher:",
                "> “Butcher, butcher, kill ox;\n> Ox won’t drink water;\n> Water won’t quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the butcher would not.",
                "Then she went a little farther and met a rope; and she said to the rope:",
                "> “Rope, rope, hang butcher;\n> Butcher won’t kill ox;\n> Ox won’t drink water;\n> Water won’t quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the rope would not.",
            ], 78),
            ([
                "Then she went a little farther and met a rat; and she said to the rat:",
                "> “Rat, rat, gnaw rope;\n> Rope won’t hang butcher;\n> Butcher won’t kill ox;\n> Ox won’t drink water;\n> Water won’t quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the rat would not.",
            ], 80),
            ([
                "Then she went a little farther and met a cat; and she said to the cat:",
                "> “Cat, cat, kill rat;\n> Rat won’t gnaw rope;\n> Rope won’t hang butcher;\n> Butcher won’t kill ox;\n> Ox won’t drink water;\n> Water won’t quench fire;\n> Fire won’t burn stick;\n> Stick won’t beat dog;\n> Dog won’t bite pig;\n> Pig won’t get over the stile;\n> And I can not get home tonight.”",
                "But the cat said to her, “If you will get me a saucer of milk, I will kill the rat.” Then the old woman gave a wisp of hay to a cow that was near, and the cow gave her a saucer of milk. Then the old woman gave the saucer of milk to the cat and this is what happened:",
                "The cat began to kill the rat; the rat began to gnaw the rope; the rope began to hang the butcher; the butcher began to kill the ox; the ox began to drink the water; the water began to quench the fire; the fire began to burn the stick; the stick began to beat the dog; the dog began to bite the pig; the pig got over the stile; and the old woman got home that night.",
            ], 82),
        ],
    },
    {
        "title": "Little Tuppens",
        "title_plate": 84,
        "vignette_page": 85,
        "pages": [
            ([
                "Long, long ago an old hen and her one little chicken went into the woods. The little chicken was named Tuppens. Scratch, scratch, they were busy all day among the leaves finding seeds to eat.",
                "“Do not eat the big seeds,” said the old hen to Little Tuppens, “for they will make you choke.”",
                "But by and by little Tuppens found a big seed and ate it. Then little Tuppens began to choke. The old hen was frightened at this and ran to the spring. She said:",
                "> “Please, spring, give me some water,\n> Little Tuppens is choking.”",
                "The spring said:",
                "> “Get me a cup and then I will give you some water.”",
            ], 86),
            ([
                "The old hen ran to the oak-tree and said:",
                "> “Please, oak-tree, give me a cup;\n> Then the spring will give me some water.\n> Little Tuppens is choking.”",
                "The oak-tree said:",
                "> “Shake me. Then I will give you a cup.”",
                "The old hen ran to the little boy and said:",
                "> “Please, little boy, shake the oak-tree;\n> Then the oak-tree will give me a cup;\n> And the spring will give me some water.\n> Little Tuppens is choking.”",
                "The little boy said:",
                "> “Give me some shoes. Then I can shake the oak-tree for you.”",
            ], 88),
            ([
                "The old hen ran to the shoe-maker and said:",
                "> “Please, good shoe-maker, give me some shoes for the little boy;\n> Then the little boy will shake the oak-tree;\n> And the oak-tree will give me a cup;\n> And the spring will give me some water.\n> Little Tuppens is choking.”",
                "The shoe-maker said:",
                "> “Get me some leather and then I will make some shoes for the little boy.”",
                "The old hen ran to the cow and said:",
                "> “Please, cow, give me some leather;\n> Then the shoe-maker will make shoes for the little boy;\n> And the little boy will shake the oak-tree;\n> And the oak-tree will give me a cup;\n> And the spring will give me some water.\n> Little Tuppens is choking.”",
                "The cow said:",
                "> “Get me some corn and then I will give you some leather.”",
            ], 90),
            ([
                "The old hen ran to the farmer and said:",
                "> “Please, good farmer, give me corn for the cow;\n> Then the cow will give me some leather for the shoe-maker;\n> And the shoe-maker will make shoes for the little boy;\n> And the little boy will shake the oak-tree;\n> And the oak-tree will give me a cup;\n> And the spring will give me some water.\n> Little Tuppens is choking.”",
                "The farmer said:",
                "> “Get me a plow and then I can give you some corn.”",
            ], 92),
            ([
                "The old hen ran to the blacksmith and said:",
                "> “Please, good blacksmith, give me a plow for the farmer;\n> Then the farmer will give me some corn for the cow;\n> And the cow will give me some leather for the shoe-maker;\n> And the shoe-maker will give me some shoes for the little boy;\n> And the little boy will shake the oak-tree;\n> And the oak-tree will give me a cup;\n> And the spring will give me some water;\n> Little Tuppens is choking.”",
                "The blacksmith said:",
                "> “Get me some iron and then I can give you a plow.”",
                "The old hen ran to the dwarfs and asked for some iron for the blacksmith.",
            ], 94),
            ([
                "When she had told her story about Little Tuppens to the dwarfs, they wanted to help. They went into their cave and brought out some iron for the blacksmith.",
                "> Then the blacksmith made a plow for the farmer;\n> And the farmer gave some corn for the cow;\n> And the cow gave some leather for the shoe-maker;\n> And the shoe-maker made some shoes for the little boy;\n> And the little boy shook the oak-tree;\n> And the oak-tree gave a cup;\n> And the spring gave some water;\n> And the old hen gave the water to Little Tuppens\n> And Little Tuppens stopped choking.",
            ], 96),
        ],
    },
    {
        "title": "The Gingerbread Boy",
        "title_plate": 98,
        "vignette_page": 99,
        "pages": [
            ([
                "A little old woman and a little old man once lived in a cottage by the roadside. One morning the little old woman made a gingerbread boy.",
                "When the gingerbread boy was taken out of the oven, looking all brown and good to eat, he jumped quickly out of the pan and ran through the open door.",
                "Yes, he ran away from the little old woman and the little old man. He ran and ran and ran. But the little old woman and the little old man ran after him. By and by the gingerbread boy met a dog. He said:",
                "> “I am a gingerbread boy, I am, I am.\n> I ran away from the little old woman,\n> I ran away from the little old man,\n> I can run away from you, I can, I can.”",
                "So the gingerbread boy ran and ran, and the dog ran after him.",
            ], 100),
            ([
                "By and by he met a cat. He said:",
                "> “I am a gingerbread boy, I am, I am.\n> I ran away from the little old woman,\n> I ran away from the little old man,\n> I ran away from the dog,\n> I can run away from you, I can, I can.”",
                "So the gingerbread boy ran and ran, and the cat ran after him.",
            ], 102),
            ([
                "By and by he met a pig. He said:",
                "> “I am a gingerbread boy, I am, I am.\n> I ran away from the little old woman,\n> I ran away from the little old man,\n> I ran away from the dog,\n> I ran away from the cat,\n> I can run away from you, I can, I can.”",
                "So the gingerbread boy ran and ran, and the pig ran after him.",
            ], 104),
            ([
                "By and by he met a little boy. He said:",
                "> “I am a gingerbread boy, I am, I am.\n> I ran away from the little old woman,\n> I ran away from the little old man,\n> I ran away from the dog,\n> I ran away from the cat,\n> I ran away from the pig,\n> I can run away from you, I can, I can.”",
                "So the gingerbread boy ran and ran, and the boy ran after him.",
            ], 106),
            ([
                "By and by he met a fox. He said:",
                "> “I am a gingerbread boy, I am, I am.\n> I ran away from the little old woman,\n> I ran away from the little old man,\n> I ran away from the dog, I ran away from the cat,\n> I ran away from the pig, I ran away from the boy,\n> I can run away from you, I can, I can.”",
                "Then the fox said:",
                "> “You ran away from the little old woman,\n> You ran away from the little old man,\n> You ran away from the dog, you ran away from the cat,\n> You ran away from the pig, you ran away from the boy,\n> But you cannot run away from me.”",
                "And the fox ran after him and snapped him up.",
                "The poor little gingerbread boy cried:",
                "> “Oh, dear! I am quarter gone. Oh, dear! I am half gone.\n> Oh, dear! I am three-quarters gone. Oh, dear! I am all gone.”",
                "And he never spoke again.",
            ], 108),
        ],
    },
]

# Text pages (photo numbers) whose lower line-art procession is extracted
# (page 45's tall man-and-pig drawing does not extract cleanly, so it is omitted)
LINE_ART_PAGES = [15, 17, 21, 23, 25, 27, 33, 35, 41, 47, 59, 91, 101, 103, 105]
