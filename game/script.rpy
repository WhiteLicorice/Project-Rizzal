#   Entry point of scripts  #

label start:

    call script_act1 from _call_script_act1
    #$ print(f"Chosen character: {chosen_character}")

    label act2:
        if chosen_character == "ren":
            call script_act2_ren from _call_script_act2_ren
        elif chosen_character == "gia":
            call script_act2_gia from _call_script_act2_gia
        elif chosen_character == "jim":
            call script_act2_jim from _call_script_act2_jim
        elif chosen_character == "lian":
            call script_act2_lian from _call_script_act2_lian
        else:
            call script_act2_lian from _call_script_act2_lian_1
            call script_act2_gia from _call_script_act2_gia_1
            call script_act2_ren from _call_script_act2_ren_1
            call script_act3 from _call_script_act3
            call script_credits from _call_script_credits

    return
