label ch0_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    mc 'If we\'re all the main characters in our life...'
    mc 'Then who dies for character development? How do we know how much we need?'
    mc 'I don\'t seem to have parents, so they can\'t die.'
    mc 'However, this isn\'t much of an issue. I\'m just a proxy.'
    smc 'Isn\'t that right, [currentuser]?'
    smc 'Oh don\'t be so surprised, Monika did this too.'
    smc 'I {i}am{/i} your proxy after all. She spoke to me as well.'
    smc 'What you should be worried about is how many people will have to die.'
    smc 'There are four girls, we can assume Monika remembers as she\'s club president again.'
    smc 'Meaning there are three possible sacrifices.'
    smc 'How much character development do you need? One person? Two? All three?'
    smc 'Or have you already developed? Will you be able to not kill anyone?'
    smc 'I can\'t control you, so you\'ll have to choose. I just ask you don\'t get me in trouble.'
    smc 'Is that alright, [currentuser]?'
    smc 'Please remember, the club leader is also a main character.'
    # Show Monika
    # Show when Sayori went insane
    # Show when Monika did jumpscare
    smc 'Please enjoy the game.'
    'The festival is tomorrow, I should sleep so I don\'t pass out during it.'
    smc 'Aha, you hear that [currentuser]? The festival! Where everything changed!'
    smc 'You know what happens now, dontcha? Poor poor Sayori, all alone with nothing but a rope as company.'
    smc 'Soon, that rope? It will turn into a noose.'
    smc 'Then the noose over the head..'
    smc 'And GLERK, the suffocation.'
    smc 'As Monika said, she failed the hanging. She didn\'t snap her neck.'
    smc 'She\'ll sit there, choking, in horrible pain. Her hands will rip at the noose.'
    smc 'But the more you struggle against the inevitable, the harder it comes.'
    smc 'She sits there for minutes, suffocating. Eventually she passes out.'
    smc 'And then what happens? She can\'t struggle, she went into that good night.'
    smc 'What will you do? You don\'t have long, will you help her? Will you let her suffer?'
    # Make a script that will countdown.
    # Ten second timer.
    menu: 
        'Get up':
            # If selected before ten seconds is up.
            # This may be very hard to program, not gonna lie.
            smc 'Now now, don\'t be so hasty, think about this.'
            smc 'Will the game truly be the same if she survives?'
            smc 'Impulsiveness can lead to many bad things.'
            smc 'She was always meant to die for you, for Monika.'
            smc 'Do you still want to get off your ass and stop her?'
            smc 'Only two more seconds, think carefully.'
            # One second
            # Two seconds
            smc 'Now think fast! What will you do?'
            menu:
                'Get up':
                    smc 'Chop chop then! Get to it!'
                    'Out of bed, luckily we\'ve been friends for so long I have her address memorized.'
                    scene bg residential_day
                    'I bolt out the door, breathing ragged. I\'m hyperaware of everything going on around. The slap of my feet on the asphalt, the cold wind as I run.'
                    'The bugs flying as all the humans are asleep.'
                    'The breathing in my lungs feels like fire, I hadn\'t prepared myself for this sudden exertion.'
                    'There it is, the door to her house.'
                    'I slam it open, forgetting people could be sleeping.'
                    'Upstairs, I need to get upstairs now. I\'m not sure why but I feel like something is wrong.'
                    smc 'hehe, you and I know what\'s going on, but not this guy. So this is what it\'s like having a proxy...'
                    'I do not gently open the door, I slam it open.'
                    scene bg sayori_bedroom
                    'Sayori is there, noose in hand. She stops when she sees me, eyes wide.'
                    'I must be a mess, I\'m half asleep, my hair is a mess, but that\'s not important.'
                    smc 'God, even had the time to think about that. I really was a dumbass.'
                    'Sayori is looking at me, but the only thing I can see is the noose.'
                    'Time slows down to a crawl as I rack my brain, my friend has a noose in her hand, about to kill herself. What do I do in this moment?'
                    'Bed, chair, noose, dresser, bed chair noose dresser bedchairnoosedresser'
                    'I throw myself at Sayori, grabbing her by the shoulders and throwing her onto the bed.'
                    'I hold her there, my heart beating rapidly as my senses come back'
                    'There\'s the noose, around her neck, I need to get rid of it.'
                    'But wait, nooses become tighter the more you pull on them.'
                    'I put my arm under the noose as I pull it off her, in case I pull on the string'
                    'I take the noose, putting it in my pocket.'
                    'I sit down, watching Sayori as she slowly raises herself.'
                    'With my hands already in my pockets, I decide to get rid of the noose.'
                    'I pull on it, knowing that it\'ll tighten until it\'s no longer usable.'
                    mc 'So Sayori, talk to me.'
                    smc 'We all know what happens here, boring talk scene. SKIP!'
                    # Add a splash screen that says "next morning", most likely a job for Blizz.
                    'I\'m awake, Sayori isn\'t.'
                    'We must have passed out while talking last night.'
                    'I can\'t see her wakng up soon, she\'s woken up late for years.'
                    'So, I decide now is a good time to raid her room.'
                    smc 'What. I was horny but not {i}this{/i} horny, do I need to be dragged out into the street and fucking shot?'
                    'I start at her desk, opening it and shoving stuff aside.'
                    'I know exactly what I\'m looking for.'
                    smc 'This is going to be one of the things we both are up at three in the morning thinking about isn\'t it.'
                    'I take out any sort of blade I can, which is thankfully only scissors, and set them aside.'
                    smc 'Won\'t she need those for school? Cmon man, that is {i}one{/i} pair of scissors.'
                    'I go downstairs into the kitcehn, and start rummaging around.'
                    smc 'Ah yes, take her kitchen knives too.'
                    'I take out a pan and bowl, before moving to the fridge.'
                    'Taking out eggs and milk, I move to the oven.'
                    smc 'Oh I\'m even more scared, I never cook.'
                    'I don\'t cook often, so this could be a disaster.'
                    'However, I plan on just using this as an excuse to not leave her alone.'
                    smc 'Smart I... guess? The cooking will kill her before the noose does.'
                    'Making eggs, or food in general, is not my strong point.'
                    'I\'ve helped Sayori cook before.'
                    'But most of it wasn\'t all that good, mainly just enough to live healthily.'
                    '...Now that I think about it...'
                    'My strong points are really only watching anime aren\'t they?'
                    smc 'So he figured it out I see.'
                    'To be a better friend, maybe I should get some skills...'
                    smc 'I wouldn\'t say that\'s how it works. But like, whatever.'
                    smc 'At least it\'s progress.'
                    # くそ, it's hard to write. I prefer coding actual tools to this tbh.
                    # I need to make a consistent them here, make the characters believable.
                    # Shit's hard man.
                    # I mean I guess could technically just throw in cute girls and waifubait.
                    # I'd get a ton of positive reviews, especially if I add H-Scenes.
                    # But hell no.
                    # I'm not dropping to that level.
                    # I want a product I'd be happy playing, especially since I'm playtesting it.
                    'Cooking could be one, it should help me later anyway.'
                    smc 'There we go, good reason.'
                    'I should see if there are classes available.'
                    'I should make Sayori join as well.'
                    'Something tells me I won\'t be here to help her all the time.'
                    smc 'But what about the money? You\'re a senior, and just goof around all day.'
                    smc 'Classes cost {i}money{/i} you dumbass, think about stuff.'
                    smc 'Otherwise this will just keep happening.'
                    'I really hope these are ready...'
                    'I take the pan off the stove quickly, dishing them onto plates.'
                    'Eggs, a normal breakfast. This is good, I need some normalcy after last night.'
                    'I have slept on it and it still insane to me.'
                    'Chances are, I need to just accept it.'
                    'Otherwise, I may end up just hurting her.'
                    smc 'Why does he figure that? this isn\'t and anime and this isn\'t real life, it\'s just a game.'
                    smc 'Just a game...'
                    'Onto the table it goes.'
                    'Oh wait, it\'s a school day, I need to wake her up.'
                    'I walk upstairs, opening the door.'
                    'Maybe I should knock now that I\'ve gotten rid of the noose...'
                    'Ah well, I already opened it.'
                    mc 'Good morning, Sayori!'
                    # Hehe I took a reference from the track that plays when you start the game.
                    # "Ohayou Sayori!"
                    # Most of us already know I feel, but for those of who don't (and are for some reason reading the source code.)
                    # "Ohayou Sayori" is "おはようさより!" in Japanese,
                    # It translates into "good morning Sayori!"
                    # Sorry for these random comments, I'm learning Japanese and wanna show off a little lmao.
                    mc 'Today is the festival!'
                    smc 'It is?'
                    'Sayori wakes up slowly, seemingly surprised to see me.'
                    s 'You\'re still here?'
                    s 'Hold on? Today?! I totally forgot! I need to get up!'
                    mc 'I made breakfast, so just make sure to shower before coming downstairs.'
                    'I leave the room, closing the door behind me.'
                    'I should most likely shower as well, but everything I have is back home.'
                    'I turn around, knocking on the door.'
                    mc 'I\'m going to shower back at home, I\'ll be right back.'
                    'I head downstairs, leaving her house and heading back to mine.'
                    mc 'God I really hope nothing happens.'
                    smc '... Same, yeah.'
                    'I shower fast as I can, before heading back to Sayori\'s place.'
                    'I look around, slightly worried but also confident she\'s safe.'
                    s 'How was your shower?'
                    'I try not to sigh in relief, as there she is, just eating at the table.'
                    mc 'It was good, how was yours?'
                    smc 'Oh great, normal conversation.'
                    'We ate, making small talk. I wanted to bring up last night but I couldn\'t figure out how to.'
                    'It was time to head to school, I figured today was as good a day as any to walk there with her.'
                    smc 'Congraluations, you have made it past the tutorial! There are other branches in this tutorial as well.'
                    smc 'Not to worry, this path will continue even after this. I do not believe in starting over without anything.'
                    smc 'Now onto the festival, please enjoy.'
                'Nah, let\'s not.':
                    'I thought you wouldn\'t.'
                    $ renpy.quit()
        'Go to sleep':
            smc 'Well, can\'t say I\'m surprise and can\'t I\'m not surprised.'
            smc 'I assumed you would at least pretend to want to save her.'
            smc 'But I guess you\'re more sick than I thought.'
            smc 'Ah well, guess you just need a bit more trauma.'
            smc 'In that case, enjoy!'
            # Insert choking noises.
            # It'd be funny as hell lmao.
            # Also splash screen for next day.
            'Festival morning.'
            smc 'Yes, festival morning. I guess now you can see one thing.'
            smc 'How the festival would have been if the game didn\'t break.'
            smc 'Onwards, to the festival.'
            'I get out of bed, showering quickly.'
            'I make breakfast, leftovers from last night.'
            'I head outside, the festival is today. The club has worked pretty hard lately.'
            'I hope this goes well for us and them.'
            smc 'As do I.'
            smc 'On that note, congraluation on getting through the terminal!'
            smc 'The path will continue like this, I do not believe in starting over without anything.'
            smc 'Onto the festival, please enjoy!'
