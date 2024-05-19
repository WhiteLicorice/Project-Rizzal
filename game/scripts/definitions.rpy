#@override
transform center_sprite_named:
    zoom 0.5
    pos (0.5, 1.0)
    anchor (0.5, 1.0)

#@override
transform center_sprite_silhoutte_enlarge:
    zoom 1.4
    pos (0.5, 1.0)
    anchor (0.5, 1.0)

    #@override
transform center_sprite_silhoutte_shrink:
    zoom 1.0
    pos (0.5, 1.0)
    anchor (0.5, 1.0)

##   Named Characters   ##

define JIM = Character("Jim", image="jim")
define GIA = Character("Gia", image="gia")
define REN = Character("Ren", image="ren")
define LIAN = Character("Lian", image="lian")
define STUDENT4 = Character("Student 4", image="student4")
define STUDENT3 = Character("Student 3", image="student3")
define OLD_MAN = Character("Old Man", image="old_man")

##   Generics   ##

define SCHOOL_KID = Character("Student", image="schoolkid")
define SCHOOL_GIRL = Character("Student", image="schoolgirl")
define OLD_MAN = Character("Old Man", image="man")