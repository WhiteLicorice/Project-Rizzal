define flash = Fade(0.1, 1.0, 0.1, color="#FFFFFF")

label script_act3:
    play music "audio/bgm/trust.ogg" loop

    scene modern dapitan hut4:
        matrixcolor SaturationMatrix(0)
    with dissolve

    "Weeks later."

    show ren disagree at center_sprite_named
    REN "Where is he? Is Rizal playing a prank on us?"
    hide ren

    show gia openeyes hmm at center_sprite_named
    GIA "Let’s wait for a while, maybe the Maestro will come soon."
    hide gia

    show ren normal at center_sprite_named
    REN "Let's do that."
    hide ren

    "There's a sudden flash of light."

    scene black with flash
    pause 1

    scene modern dapitan museum entrance
    with Pixellate(5, 5)

    play music "audio/bgm/town.ogg" loop

    show man hat and coat at center_sprite_silhoutte_shrink
    CHUDS "You’re all awake! How are you feeling?"
    hide man

    show ren aha at center_sprite_named
    REN "Chuds?"
    hide ren

    show gia openeyes worry at center_sprite_named
    GIA "So, was it all a dream? It felt soooo real!"
    hide gia
 
    show jim confident4 at center_sprite_named
    JIM "I know right! It felt like we've been there for months already."
    hide jim

    show man hat and coat at center_sprite_silhoutte_shrink
    CHUDS """
    I don’t know what you’re all talking about.
    
    But please follow Mr. Aseniero.
    
    He's the custodian of the Rizal Park and Shrine.
    
    He says you can rest in a private room while you recover.
    """
    hide man

    show lian openeyes talk at center_sprite_named
    LIAN "Aseniero?"
    hide lian

    show man waving hello at center_sprite_silhoutte_shrink
    JOSE_ASENIERO """
    Hello, everyone! It’s nice to see you again.
    
    Did you learn a lot from the Maestro?
    """
    hide man