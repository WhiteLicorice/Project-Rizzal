label script_act2_lian:
    play music "audio/bgm/heart.ogg" loop

    pause 1.0
    
    scene modern dapitan hut2:
        matrixcolor SaturationMatrix(0)
    with dissolve

    show lian openeyes argue at center_sprite_named
    """

    Lian warily surveys her surroundings.
    
    A man approaches.
    
    The man seems so dignified from his posture and his stride. 
    
    Lian squints, and stares at the approaching figure.
    
    The man looks so familiar.
    
    Is it? It can’t be.
    
    Is that Jose Rizal? How did this happen?

    """
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL "¡Hola! Quien eres? Que haces aqui?"
    hide rizal

    show lian openeyes ee at center_sprite_named
    LIAN "N–No hablo."
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Ah, lo siento.
    
    I’m sorry.
    
    I’m Dr. Jose Rizal and this is my property.
    
    What brings you here?
    """
    hide rizal

    show lian openeyes normal at center_sprite_named
    LIAN "We wanted to be your students."
    hide lian

    RIZAL """
    ¡Magnífico! I’m delighted to have new students.
    
    Come, let me show you around.
    """
    hide rizal
    
    show lian openeyes normal at center_sprite_named
    LIAN "Gracias, Maestro."
    hide lian

    scene modern dapitan hut1:
        matrixcolor SaturationMatrix(0)
    with dissolve

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Buenos días mi estudiantes, we have new guests joining us.
    
    So today, we’ll start small and show them the ropes."""
    hide rizal

    show lian openeyes normal at center_sprite_named
    LIAN "Here Maestro, let me help you!"
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL "You seem so knowledgeable about this, Lian."
    hide rizal

    show lian openeyes normal at center_sprite_named
    LIAN "I’m quite interested in science, Maestro."
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL """
    That’s good to know!
    
    Do you plan on pursuing a career in the medicine field?
    """
    hide rizal

    show lian openeyes normal at center_sprite_named
    LIAN "I’m not as skilled and smart as you, Maestro."
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL """
    Nonsense! You are more than capable.
    
    Tomorrow, you shall accompany me to the poblacion and observe while I treat my patients.
    """
    hide rizal

    scene modern dapitan hut4:
        matrixcolor SaturationMatrix(0)
    with dissolve
    
    show rizal smile at center_rizal_greyscale
    RIZAL """
    Mi estudiante, have you seen the village? 
    
    Most of the people here are quite poor.
    
    There is never a loss when I help my fellow countrymen.
    
    Providing medicine gratis is the least I can do for everyone here.
    
    It is our sacred mission to help those who are less fortunate than us.
    
    To share our talents and knowledge with our motherland.
    """
    hide rizal

    show lian openeyes normal at center_sprite_named
    LIAN """
    Muchas gracias, Maestro.
    
    Someday, I would like to be a doctor who serves the people.
    
    Just like you.
    """
    hide lian

    show rizal smile at center_rizal_greyscale
    RIZAL "I look forward to seeing that soon, mi estudiante."
    hide rizal