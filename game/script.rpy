default sandwich_ingredients = []
default finished_making_sandwich = False

label start:
    "Let's make a sandwich!"
    show screen sandwich
    jump choose_sandwich_ingredients
    return

label choose_sandwich_ingredients:
    menu:
        "What would you like to add to your sandwich?"
        "Lettuce" if not "lettuce" in sandwich_ingredients:
            call add_ingredient("lettuce") from _call_add_ingredient
        "Tomato" if not "tomato" in sandwich_ingredients:
            call add_ingredient("tomato") from _call_add_ingredient_1
        "Cheese" if not "cheese" in sandwich_ingredients:
            call add_ingredient("cheese") from _call_add_ingredient_2
        "Ham" if not "ham" in sandwich_ingredients:
            call add_ingredient("ham") from _call_add_ingredient_3
        "I'm all set!" if sandwich_ingredients:
            jump admire_sandwich
    jump choose_sandwich_ingredients

label add_ingredient(ingredient=None):
    $ sandwich_ingredients.append(ingredient)
    return

label admire_sandwich:
    $ finished_making_sandwich = True
    "What a nice sandwich you made!"
    $ ingredients_str = ', '.join(sandwich_ingredients)
    "Let's see what you chose...[ingredients_str]...yum!"
    return

transform sandwich_ingredient_slot(i):
    anchor (0.5, 0.5)
    pos (0.5, 450)
    yoffset i*-30-800
    linear 0.85 yoffset i*-30

transform off_to_side:
    anchor (0.5, 0.5)
    yalign 0.5
    xpos 1000

transform slide_to_center:
    anchor (0.5, 0.5)
    yalign 0.5
    xpos 1000
    easein_back 0.5 xpos 640

screen sandwich():
    fixed:
        if finished_making_sandwich:
            at slide_to_center
        else:
            at off_to_side
        add "bread_bottom" at sandwich_ingredient_slot(0)
        for i in range(len(sandwich_ingredients)):
            add sandwich_ingredients[i] at sandwich_ingredient_slot(i+1)
        if finished_making_sandwich:
            add "bread_bottom" at sandwich_ingredient_slot(len(sandwich_ingredients)+1)
