#   Entry point of scripts  #

label start:

    call script_act1
    #$ print(f"Chosen character: {chosen_character}")

    label act2:
        if chosen_character == "ren":
            call script_act2_ren
        elif chosen_character == "gia":
            call script_act2_gia
        elif chosen_character == "jim":
            call script_act2_jim
        elif chosen_character == "lian":
            call script_act2_liam
        else:
            pass

    return
