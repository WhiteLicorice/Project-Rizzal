label script_act2_ren:
    play music "audio/bgm/forest.ogg" loop

    pause 1.0

    scene modern dapitan hut1:
        matrixcolor SaturationMatrix(0)
    with dissolve

    show ren disagree2 at center_sprite_named
    REN """
    Oh, Lord, I have 20/20 vision.
    
    What is happening now?
    
    And why can’t I see anything clearly?
    
    Where are my classmates?
    """
    hide ren

    "As the light stops, he is too surprised to even speak."
     
    show ren mysterious at center_sprite_named

    "Ren steps back on his right foot, preparing to run from whatever he sees."

    scene modern dapitan pathway1:
        matrixcolor SaturationMatrix(0)
    with dissolve

    show ren disagree at center_sprite_named
    REN """
    This is not the same at all.

    Where am I? 
    
    This place is filled with people wearing medieval clothes, and the men wear long pants even though it is so hot.
    
    Is this a prank by my stupid classmates?
    """
    hide ren

    show rizal smile at center_rizal_greyscale

    """

    A sudden voice speaks up, and when Ren looks at where it is coming from, he is shocked at what he sees.
    
    The guy looks like Dr. Jose Rizal.
    
    Of course, he knows because, in his elementary days, Ren was tasked with printing out Rizal's face and pasting it on the classroom walls. 
    
    And, of course, Rizal’s face is forever imprinted on every peso coin he uses.

    """

    RIZAL """
    Are you a new student here?
    
    We will start making bricks today, so prepare yourself and change your attire, too, young boy.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN "Uhm..."

    show ren disagree2
    """
    Ren looks at his shirt, which has been replaced with a thin cloth that is not enough to cover his whole body.
    
    In his disbelief, he runs and tries to seek help.
    """
    hide ren
    
    scene modern dapitan hut4:
        matrixcolor SaturationMatrix(0)
    with dissolve

    """
    Instead of help, he sees a village with houses made of bamboo and nipa grass.
     
    There are also street lights that allow the villagers to work until dawn.
    
    While the children run freely, trying to catch the chickens and chicks in the street.
    """
    
    show rizal smile at center_rizal_greyscale
    """Rizal appears behind a clueless Ren, gazing at the village as well."""

    RIZAL """
    It may not be as grand, but this is a good start, eh?
    
    Your other classmates helped me create this place as well.
    
    Bueno, I will be heading to the site now, and you might like to join me on your first day at the dam site, eh? 
    """
    hide rizal

    show ren normal at center_sprite_named
    REN """
    I didn't notice you were there.
    
    Also, whose classmates?
    
    Where are my classmates?
    """ 

    "But before Ren can hear Rizal’s answers, a sudden flash of light envelops him, transporting him to an entirely different place."

    show ren disagree
    REN "Oh shit, here we go again." 

    "He closes his eyes and shouts."
    hide ren

    scene modern dapitan waterworks:
        matrixcolor SaturationMatrix(0)
    with dissolve

    """
    As they arrive at Talisay, Rizal and Ren are greeted warmly by the people at the site.
    
    Upon reaching the location, Ren notices the familiar brick wall, albeit now not fully constructed, unlike the one he had seen at Rizal Park.
    
    Surrounding the area are lush trees and the soothing sound of flowing water coming from the water bodies.
    
    Meanwhile, the people gather in one place, working together with the wooden brick maker.
    """

    show muscular man duffel bag at center_sprite_silhoutte_shrink
    MUSCLE_MAN """
    Ahay, when using this machine, I always follow what Dr. Rizal taught me, which always works.
    
    See? We can make thousands of bricks daily that are being used to create waterworks here in Talisay.
    """
    hide muscular

    """
    Ren finds himself drawn to the machine, intrigued by its appearance and its function.
    
    Engrossed in the tasks at the site, he momentarily forgets his desire to flee.
    """

    show rizal laugh at center_rizal_greyscale
    RIZAL """
    We only have wood than metal, but it is powerful enough to make thousands of bricks.
    
    I learned the craft of brick-making abroad, during my expedition in Belgium. 
    
    I witnessed bricks being made outdoors without needing ovens.
    """
    hide rizal

    show ren provoke at center_sprite_named
    REN "Without an oven, how can you make it cooked and hard?"
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL """
    At Baden, I saw a pile of bricks in the field.
    
    They used the heat from the sun to harden the bricks.
    
    You see, young boy, you learn more about these things as you explore and meet people."""
    hide rizal

    show ren normal at center_sprite_named
    REN "Well, that is much more exciting than Google."
    hide ren

    show rizal resignedlaugh at center_rizal_greyscale
    RIZAL "Goo-jel?" 
    hide rizal

    "Rizal looks confused."

    show ren aha at center_sprite_named
    REN "Nothing... nothing."
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "After all, all of our labors are for the community as well."
    hide rizal

    show ren normal at center_sprite_named
    REN "Community?"
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Indeed.
    
    Were you aware that this place, our community, has been grappling with a health crisis due to a lack of clean water?
    
    The people have been left to fend for themselves, as the resources and tools left behind by the Spaniards are useless.
    
    Little to no assistance has been offered for the betterment of the people who dutifully pay their taxes.
    """
    hide rizal

    show ren smile2 at center_sprite_named
    REN """
    Oh, those Spanish bread.
    
    But oh wait, are you saying that what we are constructing now will be the lifeline for the people here in Talisay?
    """
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "Indeed."
    hide rizal

    """
    Growing up, Ren had always believed that creation was confined only to the realm of his computer games...
    
    Where he could easily construct virtual spaces in games like Minecraft.
    
    However, under Rizal’s advice, he realizes that the waterworks they’re building will serve the entire community.
    
    It is a revelation for Ren, discovering the joy in an unexpected task and an unexpected place.
    """

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Would you assist me in measuring the upper layer of the arranged bricks?
    
    This will help us determine the number of blocks we must make.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN "Sure, we could utilize the surplus bricks and use them in the soil land as protection for our clay pipes."
    hide ren

    "Ren points at the clay pipes in the soil."

    show rizal laugh at center_rizal_greyscale
    RIZAL """
    That is a splendid idea!

    You have a mind for building things, Ren.
    
    In the days to come, you’ll surely create more, perhaps even more than a dam.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN "I doubt it. I'm not always confident in my ideas."
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "Hmmm. I have something to show you, young boy. Follow me!"
    hide rizal

    "With curiosity piqued, Ren is about to follow Rizal, but the light appears once again."

    show ren giveup at center_sprite_named
    REN "This is causing me enough jetlags, but ok."

    """Ren sighs and scratches his ear."""

    hide ren
    REN "Aaaaaaaaaaah!" 
    
    scene modern dapitan waterworks2:
        matrixcolor SaturationMatrix(0) 
    with dissolve

    """
    Leaving the construction site behind, they arrive at Calle Marquez de Pena Plata, just a stone’s throw from the Talisay village.
    
    Ren’s eyes are drawn to a fountain adorned with a majestic lion’s head faucet and crystal-clear water coming from the lion’s mouth.
    """

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Behold the Fuente de Nuestra Senora del Carmen, the heart of the Linao water system.
    
    Dapitan, despite being surrounded by bodies of water, has always faced the challenge of obtaining clean water.
    
    That’s why this fountain is a blessing.
    
    And soon, we’ll create a new one, a water system at our own Talisay.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN "Is it the one we're building? The Talisay Dam?"
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "Yes, indeed."
    hide rizal

    show ren normal at center_sprite_named
    REN "It’s remarkable. Even in present times, this marvel does not exist."
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "But this is our present, eh?"

    "Rizal gestures towards the fountain, urging Ren to quench his thirst."

    RIZAL "Here, take a sip. You look thirsty, my young friend."

    scene black with dissolve

    scene modern dapitan hut3:
        matrixcolor SaturationMatrix(0)
    with dissolve

    show ren smile2 at center_sprite_named
    REN """
    Back in Talisay Dam, having marveled at the wonders of the place, I'm now convinced that I stand in the presence of a true hero, Dr. Jose Rizal.
    
    With a newfound sense of purpose, I join the construction efforts at the dam, eager to both lend a hand to the workers and engage in meaningful conversation with Rizal.
    """
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL """
    With just a few final touches, our Talisay dam will be complete.
    
    I am grateful for the assistance of my students and the people of Talisay, who helped bring this project to fruition for our community.
    """
    hide rizal

    show ren smile2 at center_sprite_named
    """
    Ren smiles as he surveys the towering brick wall of the dam.
    
    His hands, now roughened and stained with clay, speak of his dedication to the task at hand.
    
    And deep within him, Ren knows that this is where he belongs — building something meaningful.
    """
    hide ren

    show ren normal at center_sprite_named
    REN "What if someday, in the future, our dam falls into ruins?"
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Then, I guess we should remind ourselves that what matters is we continue to build for the betterment of others.

    That spirit will endure, Ren.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN"Indeed. Well then, I’ll go back to my work."
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "Oh..."
    hide rizal

    scene modern dapitan waterworks:
        matrixcolor SaturationMatrix(0)
    with dissolve

    """
    As the last layer of the bricks are laid atop the dam and the clay pipes are secured, the reservoir fills with flowing water.
    
    Ren has fulfilled his mission: to embrace his passion for building, instilled in him by Rizal, and to carry the wisdom gained deep within his heart.
    """

    show ren smile2 at center_sprite_named
    REN "Our work here is done. Soon, the farmers and the households will reap the rewards of our community’s labor."
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Here, have some kakanin given by the elders of Talisay.

    And remember, the calluses on your hands will soon fade, replaced by the sense of fulfillment.
    """
    hide rizal

    show ren normal at center_sprite_named
    REN "My hands are here for the people, for our community. That’s the lesson you taught me, eh?"
    hide ren

    show rizal smile at center_rizal_greyscale
    RIZAL "Indeed, Ren. You’ve been an attentive student."
    hide rizal

    stop music

    scene black with dissolve

    play music "audio/bgm/rest.ogg" noloop

    return