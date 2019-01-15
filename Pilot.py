#
#  P i l o t . p y
#
#  Copyright 2011, 2018 by Edward Forgacs.
#

import sys


class Inventory:
    have_rifle = False
    have_handgun = False
    have_supplies = False
    have_machete = True
    have_bucket = False
    ar_ammo = 0
    handgun_ammo = 0


class NPCs:
    bear_alive = True
    woman_met = False
    woman_alive = True
    woman_dying = False
    caveman_alive = True


class Settings:
    debug_mode = False


def choose_path(number_of_paths, type_=int, min_=None, range_=None):
    max_ = number_of_paths
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input('1 to ' + str(number_of_paths) + '> ')
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                if Settings.debug_mode:
                    print(
                        "Input type must be of type {0}.".format(
                            type_.__name__))
                else:
                    print("Please input a number.")
                continue
        if max_ is not None and ui > max_:
            print(
                "The path chosen must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print(
                "The path chosen must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "The path must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "The path must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join(
                        (", ".join(map(str, range_[:-1])), str(range_[-1])))))
        else:
            return ui


def pause():
    print('Press enter to continue.')
    input()


def intro():
    print('You are a pilot.')
    print('After suffering a mechanical failure, you have crash landed in the middle of the deep wilderness.')
    print('You look back at the smoldering remains of your airplane and realize you have no time to lose.')
    print('As dusk sets in, you hastily calculate your next move.')
    print('')
    pause()
    airplane()


def airplane():
    print('You are standing outside the wreckage of your airplane.')
    print('Smoke is billowing into the crimson sky.')
    print('On your left is an opening that leads to a swamp.')
    print('On your right is a steep hill.')
    print('')
    print('What will you do?')
    print('  1 Go into the opening.')
    print('  2 Climb up the hill.')
    print('  3 Look inside your airplane.')
    path = choose_path(3)
    if path == 1:
        swamp()
    if path == 2:
        hilltop()
    if path == 3:
        inside_of_plane()


def swamp():
    if NPCs.woman_dying:
        return followed_and_killed_by_dying_woman()
    print('You are knee-deep in swamp water.')
    print('There is a large tree in the middle of the swamp that towers above the forest.')
    print('There is another opening that is somewhat elevated above the swamp water.')
    print('')
    print('What will you do?')
    print('  1 Go to the airplane wreckage.')
    print('  2 Climb the tree.')
    print('  3 Go into the elevated opening.')
    path = choose_path(3)
    if path == 1:
        airplane()
    if path == 2:
        tree()
    if path == 3:
        elevated_opening()


def followed_and_killed_by_dying_woman():
    print('On your way back into the swamp, you think you are being followed.')
    print('An arrow slices through the air and makes contact with your chest.')
    print('')
    print('You are dead.')
    return


def inside_of_plane():
    if Inventory.have_rifle:
        if Inventory.have_supplies:
            if NPCs.woman_alive:
                if NPCs.woman_met:
                    inform_player_that_woman_is_mechanic()
                    pause()
                    if Inventory.have_bucket:
                        return end_game()
                    else:
                        inform_player_that_fire_needs_extinguishing()
                else:
                    wonder_who_can_fix_airplane()

            else:
                return die_of_starvation()
        else:
            inform_player_need_supplies()
    else:
        smoldering_airplane_with_ar()


def inform_player_that_fire_needs_extinguishing():
    print('You need to put out the fire somehow. Is there something nearby with which you could extinguish it?')
    print('')
    input()
    airplane()


def inform_player_need_supplies():
    print('You need supplies to fix the airplane.')
    print('')
    input()
    airplane()


def wonder_who_can_fix_airplane():
    print('You see no reason to return to your burning shell of an aircraft.')
    print('If only you knew someone who could fix it...')
    print('')
    input()
    airplane()


def smoldering_airplane_with_ar():
    print('The fire in your airplane has subsided and the fuselage has begun to smolder.')
    print('Inside the baggage compartment is your Rock River Arms AR-15.')
    print('It has not been damaged by the fire.')
    print('')
    print('What will you do?')
    print('  1 Walk away from your airplane.')
    print('  2 Take your AR-15.')
    path = choose_path(2)
    if path == 1:
        airplane()
    if path == 2:
        take_ar()


def end_game():
    inform_player_that_woman_is_mechanic()
    input()
    print('You fill the bucket with swamp water and put out the fire.')
    print('After making sure that the fire is completely extinguished,')
    print('the woman goes to work on your airplane.')
    print('')
    input()
    print('After fixing the airplane, the both of you push the airplane into the large field together.')
    input()
    print('You take off and fly back to society.')
    input()
    print('You write a book together telling your story of survival.')
    input()
    print('The two of you get married, have children and live happily ever after.')
    input()
    print('')
    print('')
    print('THE END')
    print('')
    print('')
    pause()
    return


def inform_player_that_woman_is_mechanic():
    print('The woman informs you that she has experience as an aviation mechanic.')
    print('She says that she will be able to repair the aircraft, but that the fire needs to be put out first.')
    print('')


def die_of_starvation():
    print('You have a backpack filled with tools, but you have no idea how to')
    print('use them. You die of starvation before you are able to fix the plane.')
    print('')
    print('You are dead')
    pause()
    return


def take_ar():
    print('You pick up your AR-15 and pull the strap around your shoulder.')
    print('There are 30 rounds left in the magazine.')
    Inventory.have_rifle = True
    Inventory.ar_ammo = 30
    print('')
    pause()
    airplane()


def hilltop():
    print('You are standing on the hilltop.')
    print('You can see what appear to be large footprints.')
    print('')
    print('What will you do?')
    print('  1 Follow the footprints.')
    print('  2 Climb back down the hill.')
    path = choose_path(2)
    if path == 1:
        footprints()
    if path == 2:
        airplane()


def tree():
    if Inventory.have_handgun:
        print('You take in the view for a while, ')
        print('but prudently decide that you do not want a repeat')
        print('of your last tree-related incident.')
        input()
        print('You slowly climb down the tree, making sure your footing is secure.')
        print('')
        input()
        swamp()
    print('You are on top of the highest branch of the tree. You can see for miles,')
    print('but all you see is the expansive canopy of the forest.')
    print('Something shiny is at the end of the branch.')
    print('')
    print('What will you do?')
    print('  1 Try to get the shiny object.')
    print('  2 Climb down the tree.')
    path = choose_path(2)
    if path == 1:
        take_handgun()
    if path == 2:
        swamp()


def take_handgun():
    print('You slowly approach the object. It is a .45 ACP handgun.')
    input()
    print('You grab the handgun, but the branch snaps and you begin to fall to the ground.')
    input()
    print('On the way to the ground,')
    print('you make impact with several tree branches before a long, uninterrupted fall.')
    print('')
    print('You land with a thud.')
    input()
    print('After several hours of unconsciousness, you luckily emerge nearly unscathed.')
    print('')
    print('You see the loaded M1911 next to you and realize the fall was worth it.')
    input()
    print('You pick it up, wondering what it was doing up in that tree.')
    input()
    print('There are 7 rounds in the magazine and 1 in the chamber.')
    print('You consider yourself fortunate that the handgun did not discharge,')
    print('or you might have been wounded.')
    print('')
    Inventory.have_handgun = True
    Inventory.handgun_ammo = 7
    pause()
    swamp()


def footprints():
    if not NPCs.bear_alive:
        look_at_bear_corpse()
        hilltop()
    else:
        if Inventory.have_rifle and Inventory.ar_ammo > 5:
            kill_bear_with_ar()
        else:
            if Inventory.have_handgun:
                fire_handgun_at_bear()
            else:
                return killed_by_bear()


def killed_by_bear():
    print('You follow the footsteps until you see a large grizzly bear.')
    input()
    print('The bear notices you immediately. It is surrounded by cubs.')
    input()
    print('You try to escape the bear, but it catches you.')
    input()
    print('As the bear begins to maul you, you begin to bleed profusely.')
    input()
    print('The bear slashes into you.')
    print('You lose consciousness from shock and loss of blood as the bear viciously tears you apart.')
    input()
    print('You are dead.')
    input()
    return


def kill_bear_with_ar():
    print('You follow the footsteps until you see a large grizzly bear.')
    input()
    print('The bear notices you immediately. It is surrounded by cubs.')
    input()
    print('You raise your AR-15 to a low ready as the bear lets out a low snarl.')
    input()
    print('The bear launches toward you.')
    input()
    print('You fire off five rounds into the chest of the bear.')
    input()
    print('The bear roars loudly and collapses, causing the ground to shake.')
    input()
    print('The cubs scurry away. You notice a human corpse behind where the bear was standing.')
    input()
    print('The corpse has been rotting for quite some time.')
    input()
    print('There is nothing of use on the corpse\'s body except for a small bucket in the corpse\'s hand.')
    input()
    print('You take the bucket and head back toward the hilltop.')
    input()
    print('')
    Inventory.have_bucket = True
    NPCs.bear_alive = False
    Inventory.ar_ammo = Inventory.ar_ammo - 5
    hilltop()


def fire_handgun_at_bear():
    print('You follow the footsteps until you see a large grizzly bear.')
    input()
    print('The bear notices you immediately. It is surrounded by cubs.')
    input()
    print('You pull out your handgun and shoot at the bear.')
    input()
    print('The bear takes a few rounds to the chest but keeps coming at you.')
    input()
    print('You empty your magazine into the bear.')
    print('It slows down the bear long enough for you to escape.')
    input()
    Inventory.handgun_ammo = 0
    hilltop()


def look_at_bear_corpse():
    print('You see the motionless corpse of the grizzly bear.')
    input()
    print('You return down the path you came, not wanting to encounter any more bears.')
    input()
    print('')


def elevated_opening():
    print('You are in front of a cave. There is a path that goes around the cave toward an open field.')
    print('')
    print('What will you do?')
    print('  1 Go inside the cave.')
    print('  2 Go to the swamp.')
    print('  3 Go toward the field.')
    path = choose_path(3)
    if path == 1:
        cave()
    if path == 2:
        swamp()
    if path == 3:
        field()


def field():
    print('You are standing in a vast field.')
    print('It is almost completely flat.')
    print('There appears to be a small fire at the far end of the field.')
    print('')
    print('What will you do?')
    print('  1 Go to the front of the cave.')
    print('  2 Go toward the fire.')
    path = choose_path(2)
    if path == 1:
        elevated_opening()
    if path == 2:
        camp_outskirts()


def camp_outskirts():
    print('You are standing in front of a small camp.')
    print('Several large logs have been placed around a campfire in a square.')
    if not Inventory.have_supplies:
        print('There is a small makeshift tent and some basic supplies, including')
        print('a first-aid kit, a knife, and a backpack.')
        print('')
        print('What will you do?')
        print('  1 Take the supplies and leave.')
        print('  2 Stay overnight at the camp.')
        print('  3 Go to the other side of the field.')
        path = choose_path(3)
        if path == 1:
            if NPCs.woman_alive:
                caught_stealing_supplies()
            else:
                got_away_stealing_supplies()
        if path == 2:
            camp()
        if path == 3:
            field()
    else:
        print('There is a small makeshift tent.')
        print('')
        print('What will you do?')
        print('  1 Stay overnight at the camp.')
        print('  2 Go to the other side of the field.')
        path = choose_path(2)
        if path == 1:
            camp()
        if path == 2:
            field()


def caught_stealing_supplies():
    print('You begin to take the supplies.')
    input()
    print('As you are picking up the last item,')
    print('an arrow sears through the air and pierces through your body.')
    input()
    print('You are dead.')
    input()
    print('')
    return


def got_away_stealing_supplies():
    print('You take the supplies and run away to the other side of the field.')
    return field()


def camp():
    print('You set up camp for the night. There is a blanket made of animal fur.')
    if NPCs.woman_alive:
        print('You pull it over yourself and go to sleep.')
        print('')
        input()
    if not NPCs.woman_alive:
        print('You see the woman\'s corpse')
        print('and decide that maybe you should just leave.')
    if NPCs.woman_alive and NPCs.woman_met:
        print('You and the woman sit down together next to the fire.')
        print('At dawn, the reality of your situation dawns on the two of you.')
        print('You and the woman catch a fish in a nearby brook.')
        print('You cook it on the fire, eat it and begin your new day.')
        print('')
        input()
        camp_outskirts()
    if NPCs.woman_alive:
        print('Upon waking up, you see a woman tending to the fire.')
        input()
        print('She is armed with a crossbow.')
        NPCs.woman_met = True
        input()
        print('')
        print('What will you do?')
        print('  1 Talk to the woman.')
        print('  2 Kill the woman.')
        print('  3 Leave.')
        path = choose_path(3)
        if path == 1:
            dialogue_with_woman()
        if path == 2:
            attempt_kill_woman()
        if path == 3:
            attempt_leave_camp()


def dialogue_with_woman():
    print('You explain your situation to the woman.')
    print(
        'She sympathizes, \
        and concedes that the two of you would have a much better chance of survival if you worked together.')
    print('She decides to join forces with you.')
    input()
    print('After sharing some food with you, the woman picks up her backpack and supplies.')
    print('The two of you leave camp together after eating.')
    print('')
    NPCs.woman_alive = True
    Inventory.have_supplies = True
    pause()
    camp_outskirts()


def attempt_kill_woman():
    if not Inventory.have_handgun:
        if not Inventory.have_rifle:
            return attempt_kill_woman_no_weapon()
        else:
            return attempt_kill_woman_with_ar()
    else:
        shoot_woman_with_handgun()


def shoot_woman_with_handgun():
    print('You grab your M1911 underneath your blanket.')
    input()
    print('One round is already racked.')
    input()
    print('While staying nearly motionless, you fire six rounds.')
    input()
    print('The last round makes contact with the woman\'s chest.')
    input()
    print('The woman lays on the ground, gasping for air.')
    input()
    Inventory.handgun_ammo = Inventory.handgun_ammo - 6
    print('')
    print('What will you do?')
    print('  1 Finish her off and take her supplies.')
    print('  2 Take her supplies and leave her for dead.')
    print('  3 Leave her for dead and leave the supplies.')
    path = choose_path(3)
    if path == 1:
        finish_woman()
    if path == 2:
        take_supplies_of_dying_woman()
    if path == 3:
        leave_woman_for_dead()


def attempt_kill_woman_with_ar():
    print('You reach for your AR-15.')
    input()
    print('As you try to take aim, the woman effortlessly')
    print('fires an arrow into your head, and continues tending to the fire.')
    input()
    print('')
    print('You are dead.')
    input()
    return


def attempt_kill_woman_no_weapon():
    print('You run at the woman and attempt to kill her with your bare hands.')
    print('As you are running toward her, she shoots you with her crossbow.')
    print('')
    print('You are dead.')
    input()
    return


def finish_woman():
    print('You fire one last round into the woman\'s head.')
    print('The sound echoes for miles.')
    input()
    print('You take the crossbow and the other supplies.')
    print('')
    input()
    Inventory.handgun_ammo = Inventory.handgun_ammo - 1
    Inventory.supplies = True
    NPCs.woman_alive = False
    camp_outskirts()


def take_supplies_of_dying_woman():
    print('You take the crossbow and the other supplies from the dying woman.')
    Inventory.supplies = True
    print('As you walk across the field, you are attacked by a mountain lion.')
    print('')
    print('You are dead.')
    return


def leave_woman_for_dead():
    print('You leave the gasping woman at the camp.')
    print('As you walk across the field, you are hit with an arrow.')
    print('')
    print('You are dead.')
    return


def attempt_leave_camp():
    print('You stealthily creep out from under the blanket.')
    print('The woman appears to notice but remains silent and continues to')
    print('go about her business.')
    print('')
    camp_outskirts()


def cave():
    print('You are standing in the entrance to an enormous cave. There is a rope ladder leading upward above you.')
    print('There is also an opening in the stalagmites that leads downward.')
    print('')
    print('What will you do?')
    print('  1 Climb the rope ladder.')
    print('  2 Leave the cave.')
    path = choose_path(3)
    if path == 1:
        rope_ladder()
    if path == 2:
        elevated_opening()


def rope_ladder():
    if not NPCs.caveman_alive:
        print('You see no reason to visit the cave dweller\'s corpse.')
        print('')
        pause()
        cave()
    if not NPCs.woman_alive and not NPCs.woman_met:
        if not Inventory.have_rifle:
            if not Inventory.have_handgun:
                killed_by_caveman()
                return
            else:
                kill_caveman_with_handgun()
        else:
            kill_caveman_with_ar()
    else:
        if Inventory.have_handgun:
            woman_kills_caveman_with_handgun()
        else:
            woman_kills_caveman_with_arrow()


def woman_kills_caveman_with_handgun():
    print('Before climbing up the rope ladder, you pass the M1911 to the woman.')
    print('The two of you climb the ladder and see a beastly man with a machete.')
    print('He lunges at you, but both you and the woman unload on him until')
    print('he stops moving. The woman blows on the barrel of the M1911 and hands it to you.')
    print('')
    pause()
    print('You take the machete.')
    print('')
    Inventory.have_machete = True
    pause()
    cave()


def woman_kills_caveman_with_arrow():
    print('You climb the rope ladder.')
    input()
    print('Once at the top, you see a beast of a man with a machete.')
    input()
    print('He lunges at the woman, but she fires an arrow into his shoulder, stunning him.')
    print('She pulls the arrow out of his shoulder and fires it between his eyes.')
    input()
    print('')
    NPCs.caveman_alive = False
    pause()
    print('You take the machete.')
    print('')
    Inventory.have_machete = True
    pause()
    cave()


def kill_caveman_with_ar():
    print('You climb the rope ladder.')
    print('Once at the top, you see a beast of a man with a machete.')
    print('He lunges at you, but you blow a gaping hole in his head with your AR-15.')
    print('')
    pause()
    print('You take the machete.')
    print('')
    Inventory.have_machete = True
    pause()
    cave()


def kill_caveman_with_handgun():
    print('You climb the rope ladder.')
    input()
    print('Once at the top, you see a beast of a man with a machete.')
    input()
    print('He lunges at you, but you blast him with the M1911.')
    print('')
    NPCs.caveman_alive = False
    pause()
    print('You take the machete.')
    Inventory.have_machete = True
    pause()
    cave()


def killed_by_caveman():
    print('You climb the rope ladder.')
    input()
    print('Once at the top, you see a beast of a man with a machete.')
    input()
    print('He lunges at you and lops off your head in one clean slice.')
    input()
    print('')
    print('You are dead.')


def query_yes_no(question, default=None):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' "
                "(or 'y' or 'n').\n")


while True:

    # Start the game
    intro()

    playAgain = query_yes_no('Would you like to play again?')
    if playAgain:
        continue
    else:
        break
