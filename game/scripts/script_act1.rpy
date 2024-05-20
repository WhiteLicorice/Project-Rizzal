label script_act1:
    play music "audio/bgm/town.ogg" loop

    scene modern dapitan museum entrance with dissolve

    "Rizal Park and Shrine, Dapitan."
    
    "Four yellow buses stop at the designated parking lot near the entrance of Rizal Shrine." 
    
    #"Senior high students in their blue and white uniforms step out of the bus carrying handbags and backpacks."

    """
    Senior highschool students in colorful outfits step out of the bus carrying handbags and backpacks. 
    
    To cap off their history class, their instructor — with the support of the school — organized a tour in Rizal Shrine.
    
    The tour was arranged so that the students could be more in touch with their history and learn beyond the four walls of the classroom.

    While the tour guide was showing them around, a group of friends strayed from their class.
    """

    show jim normal at center_sprite_named
    JIM "What are we even doing here?"
    hide jim

    show gia openeyes normal at center_sprite_named
    GIA "It’s not like learning about Rizal can help us prepare for our future."
    hide gia

    show ren mysterious at center_sprite_named
    REN "True! It’s just boring history. He can’t even help me decide on my college application."
    hide ren

    show lian openeyes normal at center_sprite_named
    "Lian sighs at Ren's words."
    LIAN "I wish we could just go back home. I’m not learning anything from this tour."
    hide lian

    show ren normal at center_sprite_named
    REN "I’m bored, too. In the meantime, let’s explore for a while."
    hide ren

    scene modern dapitan hut2 with dissolve

    """
    As the friends roam around, they eventually come upon the Casa Residencia, Rizal’s main residence when he was staying in Dapitan.
    
    It seems like their tour group had moved on to other places because the four friends are the only ones in the vicinity.
    
    They climb the wooden staircase to take a look inside.
    """

    scene modern dapitan hut3 with dissolve

    show schoolgirl totebag at center_sprite_silhoutte_enlarge
    SCHOOL_GIRL "I can’t imagine living in Rizal’s time."
    hide schoolgirl

    show jim normal at center_sprite_named
    JIM "Though it must have been nice because they didn’t have to learn about Rizal himself."
    hide jim

    "Everyone laughs at the joke."

    show schoolkid walking at center_sprite_silhoutte_enlarge
    SCHOOL_KID "It’s kinda pointless. What would Rizal even teach us?"
    hide schoolkid

    show man waving hello at center_sprite_silhoutte_shrink
    OLD_MAN "I think he’ll teach you a lot of things. He was a great maestro who made us work day and night."
    hide man

    """
    The group of friends are startled at the old man who appears suddenly out of nowhere.
    
    Hunched near the open door, he's carrying a cane.
     
    He's wearing a white camisa de chino with the sleeves rolled up to his elbows and black slacks.
    """

    show gia openeyes normal at center_sprite_named
    GIA "Excuse me po, are you a historian?"
    hide gia
    
    show man waving hello at center_sprite_silhoutte_shrink
    OLD_MAN "Oh no! I just live in the area. I’ve been living here for quite a long time. That’s why I know a lot about the maestro. Dr. Jose Rizal greatly helped the small town of Dapitan and its people."
    hide man

    show gia openeyes normal at center_sprite_named
    GIA "Are you well acquainted with Jose Rizal and his life story po? We’re here on a field trip."
    hide gia

    show jim normal at center_sprite_named
    JIM "Though it’s a bit boring already."
    hide jim

    show gia openeyes mad2 at center_sprite_named
    "Gia  glares at Jim."
    hide gia

    show man waving hello at center_sprite_silhoutte_shrink
    "The old man chuckles."
    OLD_MAN "Well, I hope you’ll enjoy your tour and learn a lot from the maestro. I’ll take my leave now!"
    hide man

    "The old man suddenly disappears."

    show lian openeyes normal at center_sprite_named
    LIAN "What a weird old man!"
    hide lian

    show ren normal at center_sprite_named
    REN "The maestro? Why did he call Rizal that?"
    hide ren

    show gia openeyes normal at center_sprite_named
    GIA "I don’t know either."
    hide gia

    show jim normal at center_sprite_named
    JIM "Come on! Let’s just go and get some food outside."
    hide jim

    play music "audio/bgm/critical.ogg" loop

    "As the three friends climb down the stairs, they feel weirdly nauseous."
    
    "The ground shakes uncontrollably."

    scene modern dapitan hut3
    with hpunch
    
    "The shaking doesn't stop and becomes even more violent."

    scene modern dapitan hut3
    with hpunch

    "Their surroundings seem to be spinning."

    scene modern dapitan hut3
    with hpunch
    
    "They feel so dizzy that it seems like they had just been on a roller coaster."

    scene modern dapitan hut3
    with hpunch
    
    "The four friends try to hold on to the wooden railing but the shaking continues and they are thrown off balance."

    scene modern dapitan hut3
    with hpunch
    
    "They hit their heads on the ground and collapse."

    play music "audio/bgm/rest.ogg" noloop

    scene black
    with Pixellate(5, 5)
    
    "Ren, Lian, Jim, and Gia briefly lose consciousness."

    scene modern dapitan hut1
    with fade

    "As soon as they open their eyes, they are still in front of the Casa Residencia."
    
    "But somehow, something has changed in their surroundings."

    scene modern dapitan hut1:
        matrixcolor SaturationMatrix(0)
    with Pixellate(5, 5)

    #   TODO: verify is this should be here
    # show ren normal at center_sprite_named
    # REN "Are we at the same place?"
    # hide ren

    # show jim normal at center_sprite_named
    # JIM "I think so, that’s still the Casa Residencia. But there’s something weird about it."
    # hide jim

    # show gia openeyes normal at center_sprite_named
    # GIA "Yeah. This isn't how I remember it when I got here."
    # hide gia

    # show lian openeyes normal at center_sprite_named
    # LIAN "Did we just — did we just travel back to Rizal's time!"
    # hide lian

    scene black with dissolve

    play music "audio/bgm/trust.ogg" loop

    "Before proceeding with the rest of the story, choose which character you would like to follow."

    menu:

            "Jim":
                $ chosen_character = "jim"
                "You chose Jim."

            "Gia":
                $ chosen_character = "gia"
                "You chose Gia."

            "Ren":
                $ chosen_character = "ren"
                "You chose Ren."

            "Lian":
                $ chosen_character = "lian"
                "You chose Lian."

    return