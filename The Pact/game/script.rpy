# The script of the game goes in this file.

# Declare characters used by the game. The color argument colorizes the
# text displayed by the character.
#splash screen image and warnings
image splash = "splash.png"

label splashscreen:
    play music "audio/Heaven.mp3" loop fadein 2.0
    scene black
    with Pause(1)
    show splash with dissolve
    with Pause(2)
    centered "{color=#AD527B}{size=+20}\n\n\n\n\n\nThis game focuses on heavy themes of religious trauma, contains extreme violence and sexual content which may be too intense for some viewers. Viewer discretion is advised.{/size}{/color}" with dissolve
    centered "{color=#AD527B}{size=+20}\n\n\n\n\n\nMore detail on content warnings in readme.txt!~{/size}{/color}" with dissolve
    with Pause(2)
    scene black with dissolve
    with Pause(2)

    return

define G = Character("God", color="#e2a8c3")  
define L = Character("Lucifer", color="#8b0000")  
define S = Character("Sable", color="#9779af")
define W = Character("Wrath", color="#ff0000")
define Gb = Character("Gabriel", color="#f5dd9b")

# Character image aliases
#GOD images
image god = "god.png"
#Lucifer images
image lucifer = "lucifer.png"
image lucifercr = "lucifercr.png"
image lucifersad = "lucifersad.png"
image lucifersmug = "lucifersmug.png"
image lucifershocked = "lucifershocked.png"
image lucifersus = "lucifersus.png"
image luciferflush = "luciferflush.png"
image lucifercrflush = "lucifercrflush.png"
image lucifercrsmug = "lucifercrsmug.png"
image lucifercrshocked = "lucifercrshocked.png"
image lucifercrsus = "lucifercrsus.png"
image lucifercrsad = "lucifercrsad.png"
image luciferenraged = "luciferenraged.png"
image luciferenragednm = "luciferenragednm.png"
image luciferenragedopen = "luciferenragedopen.png"
image LuciferOnThrone = "Lucifer_throne.png"
image Throne = "Throne.png"
#Sable images
image sable = "sable.png"
image sablecig = "sablecig.png"
image sablecig2 = "sablecig2.png"
image sablecig3 = "sablecig3.png"
image sablecig4 = "sablecig4.png"
image sablecig5 = "sablecig5.png"
image sablecig6 = "sablecig6.png"
image sablewrathcig = "sablewrathcig.png"
image sablesad = "sablesad.png"
image sablesmug = "sablesmug.png"
image sableshocked = "sableshocked.png"
image sableshocked2 = "sableshocked02.png"
image sablesus = "sablesus.png"
image sableflush = "sableflush.png"
image sablecr = "sablecr.png"
image sablecrsad = "sablecrsad.png"
image sablecrsmug = "sablecrsmug.png"
image sablecrshocked = "sablecrshocked.png"
image sablecrsus = "sablecrsus.png"
image sablecrflush = "sablecrflush.png"
#Wrath images
image wrath = "wrath.png"
image wrathshocked = "wrathshocked.png"
image wrathsmile = "wrathsmile.png"
#Gabriel images
image gabriel = "gabriel.png"

# Background image aliases

image Heaven = "bg01.jpg"
image Hell = "bg02.jpg"
image Crack House = "bg03.jpg"
image Crack House Night = "bg03-01.jpg"
image The Fall = "bg04.jpg"
image The Flood = "bg05.jpg"
image Monochrome Garden = "bg06.jpg"
image Eden = "bg07.jpg"
image Sunset = "bg08.jpg"
image Tomb = "bg09.jpg"
image TombEyes = "bg09copy.jpg"
image Gore = "bg10.jpg"
image Flowers = "bg11.jpg"
image The Ark = "bg12.jpg"
image The Ark2 = "bg12-1.jpg"
image Abomination = "bg13.jpg"
image Innocence = "bg14.jpg"
image InnocenceLost = "bg14-1.jpg"
image Cross = "bg15.jpg"
image Crucify = "bg15-1.jpg"
image Book = "bg16.jpg"
image Shoes = "bg17.jpg"

# Individual Character CGs
image FlameFinger = "CG01.png"
image Birth = "CG02.png"
image The First = "CG03.png"
image Unity = "CG04.png"
image AdamPlot = "CG05.png"
image ELAssault = "CG06.png"
image Bloodonhands = "CG07.png"
image Lucifer Fallen = "CG08.png"
image God Stare = "CG09.png"
image Jesus = "CG10.png"
image God Smug = "CG11.png"
image God Assault = "CG12.png"
image Lucifer Monster = "CG13.png"
image Lucifer Throne = "CG14.png"

#MISC Images
image Blood = "blood.png"
image Blood2 = "blood2.png"
image Eyes = "eyes.png"
image Stop = "stop.png"
image Stop2 = "stop2.png"
image Hellfire = "fire.jpg"
image Cigs = "Pack.png"
image Jesus = "Jesus.jpg"
image End = "End.png"
image EndSplash = "EndSplash.png"

#Transforms
transform breathe:
    yoffset 0.0
    linear 2.0 yoffset -2.0
    linear 2.0 yoffset 0.0
    repeat

transform tilt:
    rotate 1.0
    linear 1.5 rotate -1.0
    linear 1.5 rotate 1.0
    repeat

transform breathe_scale:
    zoom 1.0
    yoffset 0.0
    linear 2.5 zoom 1.01
    linear 2.5 zoom 1.0
    linear 2.5 yoffset -1.5
    linear 2.5 yoffset 0.0
    repeat

transform sink:
    yoffset 0
    linear 0.5 yoffset 100

transform spasm:
    linear 0.1 xoffset -3 #move left 20 pixel in 0.2 seconds
    linear 0.1 xoffset +3 #move right 20 pixel in 0.2 seconds
    linear 0.1 yoffset -3 #move left 20 pixel in 0.2 seconds
    linear 0.1 yoffset +3 #move right 20 pixel in 0.2 seconds
    repeat 

transform shiver:
    linear 0.1 xoffset -5 #move left 20 pixel in 0.2 seconds
    linear 0.1 xoffset +5 #move right 20 pixel in 0.2 seconds
    repeat 

transform hpunchish:
    linear 0.2 xoffset -20 #move left 20 pixel in 0.2 seconds
    linear 0.2 xoffset +20 #move right 20 pixel in 0.2 seconds
    repeat 5 #repeat the above 5 times

transform bouncy:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform screen_shake:
    xoffset 0
    yoffset 0
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

transform memory_fade:
    alpha 0.0
    linear 2.0 alpha 1.0

transform memory_exit:
    alpha 1.0
    linear 2.0 alpha 0.0
# The game starts here. 

label start:
    play music "audio/cityslums.mp3" loop fadeout 1.0 fadein 1.0
    scene Crack House with fade

    # Sable calling upon Lucifer
    "Midnight. Another empty night in an abandoned block."
    "Cigarette smoke curls through cracked windows like prayers never answered."
    "Yeah... They were never answered."
    "So, why was she thinking this was going to be different?"

    # This shows a character sprite. A placeholder is used, but you can

    show sable at left with moveinleft

    S "'Highly doubt this is even gonna work...'"
    S "'But what do I have to lose?'"

    pause 1.0
    play sound "audio/Book.mp3" fadeout 1.0
    scene Book with fade
    "A small book lies open across knees covered in cheap, dirtied denim."
    stop sound
    "Blood sigils glow faintly beneath candlelight- homemade, desperate, honest."
    "Feeling a slight hesitation, the young woman sighs as she takes another drag."
    play sound "audio/Cig.mp3"
    scene Crack House with fade
    show sablecig at center

    S "'{i}(Might as well try anything... I'm at my wits end.){/i}'"

    $ sb_name = "Sable"

    S "'I... Call upon thee who bares the burden of the morningstar fall. Let hear my plea...'"
    stop music fadeout 1.0
    play sound "audio/heartbeat.mp3" loop fadein 1.0

    "The air suddenly thickens, becoming difficult to breathe."
    "Watching as the candlelight flickers..."
    "Static pricks at the girls skin like ants marching up along the spine."
    scene Crack House at screen_shake
    play music "audio/woodcrack.mp3" fadein 1.0
    "Cracks appear in the walls, as if the very foundation of the house is cracking under the weight of the invocation."
    stop music fadeout 1.0
    "A sense of dizziness washes over her. Until then..."

    show lucifer at center with dissolve
    stop sound fadeout 1.0
    hide sablecig
    show lucifer at center with vpunch
    play music "audio/DarkBG.mp3" loop fadein 1.0

    "Before her stands not a man as the books described, but a feminine figure with shadows lapping at the girls body." 
    "Feeling the cigarette butt resting between her lips, suddenly fall, and lands to the ground. Extinguished."
    hide lucifer
    show lucifercrsmug at center
    L "'Well well... You're either quite stupid or incredibly brave.'"
    "Seemingly mildly amused that the girl managed a strong enough summoning to allow her to get to the mortal realm."
    show lucifercrsmug at right with move
    show sableshocked at left
    "The girl was... understandably taken off guard, as she remained seated where she was, staring up at Lucifer."
    S "'A-Ah... Wait a minute. You're Satan?'"
    "Her vocal questioning sounding a mix of both confused and yet amazed at her own capabilities in actually summoning the Lord of Hell."
    show sableshocked at left, sink
    S "'Gonna be real- I thought this was all fake, y'know? Like how God is and everything?'"
    hide sableshocked
    hide lucifercrsmug
    show luciferenragedopen at center with vpunch
    L "'Don't fucking talk to me about God right now!'"
    hide luciferenragedopen
    show luciferenraged at center
    "Suddenly snapping, as she sharply inhaled, claws retracting slowly..."
    "Then exhales fire that smells of ash and regret. Closing her eyes as she pinched the bridge of her nose."
    hide luciferenraged
    show lucifersus at right
    L "'Right. Yes, of course. You mortals need proof or whatever. I dunno, I don't keep up with what you humans are into.'"
    L "'I've got too much shit to do in Hell. What do you want me to do, I guess?'"
    show sable at left
    "Alright... So, it seemed that God was a sore spot to her. Sable would try to not mention it again, she didn't want to get on her bad side."
    S "'Uh...'"
    "Suddenly feeling a bit awkward as she rubbed on her neck. Trying to think. Though... it didn't take long for her answer. Not really."
    S "'I... Want my parents to be dragged to Hell, and tortured for the rest of eternity, especially my father... They both deserve it.'"
    "The last bit was muttered, but Lucifer could still pick it up. Raising an eye brow to her demand."
    hide lucifersus
    show lucifercrsus at right
    L "'So, you're sacrificing them is what you're saying?'"
    play sound "audio/firecrackling.mp3" fadeout 1.0
    "There was a thick air suddenly between them. Slight crackling as it seemed to pulse with each of her words."
    L "'You had best have a good fucking reason. I've slaughtered entire cults for less, for doing the same shit.'"
    stop sound
    hide lucifercrsus
    show sableshocked at left
    show luciferenraged at right, spasm
    "She warns, floating close as an inky darkness envelops her entire lower arm, fingertips turn to scorching, razor-sharp claws."
    hide luciferenraged
    show luciferenragedopen at right, spasm
    L "'I'm not a fan of people thinking they can order me around, and ask me to take lives just because of a paltry sacrifice.'"
    show luciferenragedopen at right, spasm
    L "'So, I suggest you choose your next words carefully.'"
    hide luciferenragedopen
    "The heat of Lucifer's claws was hot enough to quickly burn away a fresh cigarette that Sable went to try and light, but she quickly pulled away, watching the ashes fall."
    show sableshocked at left, bounce
    "Unable to help but give an exasperated sigh towards another cig being easily wasted, she looked to the larger woman before her, and crossed her arms."
    hide sableshocked
    show sablecr at left
    "Though Sable didn't really seem scared, just amazed, numb even."
    show sablecr at left
    hide sablecr
    show sablecrsus at left
    S "'Well, let me ask you this. Would you allow a child rapist to go unpunished? All because they told you, for {i}years{/i} it was 'Gods Will'?'"
    "She questioned, voice growing very cold and monotone as she laid it out plain as day. Not sugar coating anything."
    S "'That's all my parents have ever been. It's why I'm currently homeless, looking to the only other deity I can possibly think of who {i}might{/i} understand what it's like to be betrayed by something you were told was meant to save and protect you.'"
    hide sablecrsus
    show sablecrsad at left
    S "'When in the end, all it did was ruin you...'"
    show lucifersad at right
    "Lucifer froze, entirely stopped moving. It seemed as if she stopped breathing entirely. Hearing what Sable said, it struck something in her."
    "Coming to, she stands upright, summoning a fresh cigarette."
    L "'Give me a minute.'"
    "She says with an icy-cold tone that could send a horrid chill through the spines of the most powerful of Sins, and no doubt, freeze Hell over."
    hide lucifersad
    hide sablecrsad
    hide sable
    "Suddenly vanishing."
    stop music
    pause 2.0
    play sound "audio/boom.mp3" fadeout 1.0
    "And sure enough, a minute goes by... and suddenly the ground shakes."
    scene Crack House Night at spasm
    "A light emits in the distance. Then, a mushroom cloud. Right where Sable's parents were. Or rather now, used to be."
    stop sound
    "Then, before Sable could even properly react, Lucifer returned, her form much more twisted and monstrous, an amalgamation of angel and demon, mashed into some putrid entity."
    play sound "audio/BoneFlesh.mp3" fadeout 2.0
    play music "audio/abomination.mp3" fadein 1.0 fadeout 1.0 loop 
    scene Abomination at spasm
    show Lucifer Monster at shiver
    "Unable to be properly comprehended by mortal minds. Along with her, Sable's father. His limbs snapped and twisted unnaturally, as he was forced to kneel."
    stop sound
    L "{color=#FF0000}{cps=10}'BEG FOR YOUR LIFE. BEG FOR FORGIVENESS. LAMENT YOUR DOINGS. N O W.'{/cps}{/color}"
    "Lucifer demanded of him, forcing him to look his daughter in the eye. The man who relentlessly tormented her with glee, now shivering, whimpering, pathetic shell of a man he always was."
    "He could hardly say anything amidst the pain, only speaking after Lucifer lets out a deafening, horrifying roar."
    "'I-I'm sorry!! I'm so sorry!! I know what I did was wrong! It was never God's will!'"
    L "{color=#FF0000}{cps=10}'Sable. Would you like the honors? To slay this wretched filth, and be cleansed of his vile, putrid form? OR SHOULD I?'{/cps}{/color}"
    "Finishing her cigarette, she stared at her father before her now, whimpering, begging for his life."
    "It only caused her blood to boil. Since whenever she pleaded, he {i}never{/i} showed her the same mercy. So... why should she grant him that mercy?"
    S "'No, no, {i}I{/i} want to do the honors.'"
    play sound "audio/Burn.mp3"
    "Answering quite fast, almost as if it took no time at all to think on it. Putting her cigarette out onto her father's flesh."
    "Then, before killing him, she wanted her Father to suffer... "
    stop sound
    play sound "audio/punch.mp3"
    "She'd beat him to hell and back. Punching, kicks, slaps, scratches."
    "On the face, stomach, groin, sides, everywhere she could reach, breaking his nose. His body becoming bruised and bloodied."
    stop sound fadeout 1.0
    "Reaching into her back pocket she brandished a small dagger, same one she used to cut herself to write out the sigils from before the summoning."
    S "'I hope you enjoy the rest of your existence, suffering for what you did to me!'"
    play sound "audio/Stab.mp3"
    show Blood
    "She screamed from the sheer intensity of her rage. Removing his manhood, and finishing it off by slitting his throat. Panting, and trembling as she slumped down onto the floor. Pressing her back against one of the cracked walls. Covered in blood, regaining her bearings."
    show Blood2
    hide Blood
    hide Blood2
    hide Lucifer Monster fadeout 1.0
    stop sound fadeout 1.0
    scene black with fade
    stop music fadeout 1.0
    scene Hellfire with fade
    play sound "audio/Burn.mp3" fadeout 1.0
    stop sound fadeout 1.0
    "Lucifer nods approvingly, snapping her fingers as his body and the bloody mess left behind was cleaned up in a burst of hellfire."
    show lucifersmug at right
    L "'Ah, it's good to see that humanity still has some redeeming aspects.'"
    "Having greatly enjoyed the performance as she grinned with an approving nod."
    show lucifersmug at right, bounce
    L "'I know that doesn't come anywhere close to fixing or aiding what was done to you. But I do hope that this act of vengeance brings you some measure of closure, and peace.'"
    hide lucifersmug
    show lucifercrsmug at right
    "The Morningstar explained, as she had soon returned to her normal form, floating about, as she looked down at Sable with a pleased expression."
    scene Crack House Night with fade
    show sableshocked at left 
    hide sableshocked
    show sablesmug at left, bouncy
    play music "audio/cityamb.mp3" fadein 1.0 loop
    S "'That was... {i}AMAZING!{/i} Finally, some sort of justice was served! And not the cop-type justice- those pigs kill more innocent people than they save.'"
    play sound "audio/lighter.mp3"
    "She lamented a bit as she lit another stick, sighing as she glanced over towards Lucifer's form."
    hide sablesmug
    stop sound fadeout 1.0
    show sablecig at left
    S "'Y'know... Everyone here thinks you're a dude. Same with God. But yet you're not. Don't even get me started on the way you are represented in media.'"
    S "'Plus, how you are known through various extremist groups as {i}horrible, and evil demon who brought sin upon the world.{/i}'"
    hide sablecig
    show sablecig2 at left, sink
    "A moment of silence as it just hit her, that she had said God's name yet again."
    S "'Ah, fuck, sorry for mentioning the {i}G name{/i} again...'"
    show lucifer at right
    L "'It's alright. I'm not surprised. Humanity seems to have deviated from {i}her{/i} path a long time ago.'"
    hide lucifer
    show lucifercrsus at right 
    L "'But I don't care. It's not my problem. It's her own damn fault for not being more careful.'"
    L "'I warned her, she doesn't listen. Too caught up in her own complex.'"
    "Once Lucifer realizing she was rambling, she tried to change the subject instead."
    hide lucifercrsus
    show lucifercrsad at right
    L "'I haven't been able to talk to someone like this in a long time. And a mortal no less...'"
    hide lucifercrsad
    show lucifercrsus at center with move
    hide sablecig2
    show sablecig3 at left
    L "'There's something special about you that I can't quite put my finger on...'"
    hide lucifercrsus
    show lucifer at center
    L "'But, alas, I can't do anything. You're not dead, I can't do anything more for you. And our time is running out.'"
    "The darker skinned girl didn't seem to mind, it was obvious that she as well didn't have anyone to chat with herself. So, this felt really nice..."
    hide sablecig3
    show sablecig2 at left
    "But as soon as she heard that it was going to be ending soon, her expression went from pure excitement, to one of dread and anxiety. As she shrugged her hoodie back on."
    hide lucifer
    show lucifer at right with move
    hide sablecig2
    show sablecig3 at left, bounce
    S "'Wait, I have to be dead for us to ever talk again? Can't there be like-'"
    pause 0.5
    S "'I don't know, make a pact or something? Or is that only seen in fictional media?'"
    "She questions, hoping there was someway to see each other again."
    pause 0.5
    "There was some moments of silence, until the demon queen spoke up."
    hide lucifer
    show lucifersus at right
    L "'You'd really risk doing a pact... just to talk to me??'"
    "Questioning in disbelief. This girl kept on surprising her it would seem."
    L "'Why? I genuinely {i}cannot{/i} understand you humans...'"
    hide sablecig3
    show sablecig2 at left
    S "'I mean... I don't have anyone else. I've been in and out of the hospital the last few years, and all I had for comfort was drugs. Aside that, I genuinely would prefer worshipping you than all {i}high and mighty{/i} anyways.'"
    hide sablecig2
    show sablecig6 at left
    S "'She never came to my aid... So, why should I care to follow her? When my true savior is right before me now.'"
    pause 1.0
    hide lucifersus
    show lucifershocked at right
    "Lucifer seemed genuinely stunned. Never before has she ever had a worshipper, anyone who she could relate to, anyone who would willingly be in her presence aside from the few Sins she was on good terms with.'"
    hide lucifershocked
    show lucifersad at right
    L "'Heh, you and me both. You really are something else.'"
    hide lucifersad
    show lucifercr at right, bounce
    L "'Alright. For the pact to work properly there needs to be subjective {i}equal{/i} gain between both parties.'"
    "Seemingly punctuating the {i}equal{/i} with air quotations."
    L "'Typically that involves me monkey-pawing the shit out of the other person. But, we're playing it straight this time. So. My condition is...'"
    hide lucifercr
    show lucifercrsmug at right
    L "'Well, I guess, I take you to Hell. Body {i}and{/i} soul. Are there any conditions you have? It can be anything but there has to be {i}something{/i}. Alright?'"
    hide sablecig6
    show sablecig3 at left
    S "'Woah, really? You'll take me out of this world, and down to Hell? I'd {i}much{/i} prefer that over staying here. I have nothing and nobody left for me here.'"
    "Taking a moment to think over what it was exactly she wanted, before giving a small smile and glanced up to Lucifer with a knowing nod."
    hide sablecig3
    show sablecig5 at left
    S "'How about a pack of cigarettes that never empties? That'd be great! Do you know how expensive they are in this fucking place!?'"
    "Lucifer couldn't help but let out a loud, amused laugh."
    hide lucifercrsmug
    show lucifersmug at right, bounce
    L "'Fuckin' hell, you... you just keep surprising me.'"
    "She says as she wipes a tear from her eye, then extending her hand to seal the deal with the girl."
    "Laughter going both ways, Sable grinned as she reached for Lucifer's own hand, not hesitating as she took a firm hold of the fallen angels hand. More than ready to leave this cesspit."
    hide sablecig5
    hide lucifersmug
    stop music fadeout 1.0
    scene black with fade

    scene Hellfire at screen_shake 

    "And with that, hellfire swirls and whips around them the moment they make contact, the rush of falling at such immense speeds"
    "Before suddenly, everything goes still."
    scene black with fade

# CHAPTER 2: IN HELL
    play music "audio/hell.mp3" fadein 1.0 loop
    scene Hell
    with dissolve
    "The fires engulfing them fade to reveal Hell in its full... glory? Maybe not that."
    show Cigs at center 
    with dissolve
    "Anyways, a carton of cigs pops into existence in Sable's hand. {i}LUCY'S DEATH STIX{/i} written on the ominous, obsidian cardboard box in bold, yet elegant red lettering. A typical, yet very realistic skull imprinted on the box as a crude logo."
    "Standing there, as sweat trickled down her face from the sudden adrenaline rush she received from the travel between the world above, to the pits of hell. Sable looked around in awe at the infernal landscape."
    hide Cigs
    "Before feeling the item in her hand. Glancing down to look over the box of cigarettes. Remaining silent for but a moment, before grinning from ear to ear."
    show sablesmug at left, bouncy
    S "'This is the {i}BEST{/i} and coolest pack of cigs I have ever seen! And it's all mine!'"
    "Chuckling a bit, before taking one out, wanting to try it eagerly. And man, as it seemed to almost automatically light up as it connected to her lips, feeling the smoke go down her esophagus."
    play sound "audio/Cig.mp3" fadeout 1.0
    "It had an interesting kick to it, as if she swallowed fire just not in a painful way. A little cat-like smile forming on her lips as she sighed, before looking around."
    hide sablesmug
    show sablecig5 at left
    S "'Oh yeah, I knew Hell was for me.'"
    show lucifercrsmug at right with move
    L "'I really and truly cannot wrap my head around you... Quite literally the {i}ONLY{/i} mortal I've ever met {i}EXCITED{/i} to be in a realm of eternal pain and damnation.'"
    "Lucifer chuckles, shaking her head in disbelief before perking up."
    hide lucifercrsmug
    hide sablecig5
    show lucifershocked at center, bouncy 
    show sablecig3 at left, bounce
    L "'OH! Right, come, I need to show you to the others.'"
    show lucifershocked at offscreenright
    show sablecig3 at offscreenright
    with None
    scene black
    with fade
    hide lucifershocked
    hide sablecig3
    "She says excitedly, almost like a child on Christmas morning. As she takes Sable by the hand and leads her off. Hitting each circle to show off she finally has her first worshipper. With... mostly less than stellar reactions. Most of which involved someone trying to take Lucifer's head off in some manner."
    "But then they get to Wrath-"
    scene Hell 
    with dissolve
    show lucifersmug at offscreenright
    show sableshocked at offscreenright
    with None
    show lucifersmug at right
    show sableshocked at right
    with ease
    show lucifersmug at right, bouncy
    L "'WRATH OH MY FUCK! I HAVE MY FIRST EVER WORSHIPPER, LOOK!!! LOOK AT HER!!'"
    "She exclaims, beaming from eat to ear as she holds Sable up like a cat."
    "The girl didn't seem to mind the attention, if anything it felt really, really nice to be receiving positive attention for once. And from Satan no less."
    hide sableshocked
    show sableshocked2 at right
    "As she was held up to Wrath, her eyes widened looking up at this guy. He was {i}HUGE{/i} and {i}INTIMIDATING{/i}! Holy shit!"
    show wrath with moveinleft
    S "'W-Woah...'"
    "Was all she could mutter as she just kept staring, cigarette falling from her mouth, before magically appearing on her lips once more."
    hide sableshocked2
    show sablewrathcig at right
    "Wrath turned towards the excitement, seemingly having just finished sending his implings off to take care of some business. Upon seeing this human within the devils grasp."
    "It took him a moment, not used to having mortals in his presence."
    hide wrath
    show wrath at left
    with dissolve
    W "'A worshipper...'"
    "He rumbled out, repeating in a gentle, deep rumble. Then, at last, a smile appeared onto his hardened face."
    hide wrath
    show wrathsmile at left, bounce
    W "'And willingly, no less.'"
    "He teased a bit with a warm chuckle, before his own eyes landed onto Lucifer with unmistakable pride."
    W "'Mayhap the realms are at last beginning to see what I have long known. Thou wert never meant to kneel beneath Heaven forever.'"
    "Lucifer plopped Sable down onto her shoulders now, before acknowledging Wrath's words, giving a bit of a sigh."
    hide lucifersmug
    show lucifersad at right
    L "'You are right. Admittedly, it's been hard to think about, but after everything... Heaven wasn't meant for me. Just like you said.'"
    hide lucifersad
    show lucifercrsad at right
    L "'It still baffles me, even though I was the first, I never had a place there. Not really.'"
    "She says, turning a bit melancholic. Really thinking about the implications of that. But then she shakes her head, completely disregarding that thought.'"
    hide lucifercrsad
    show lucifercr at right, bounce
    W "'Thou needest not pretend indifference before me. To realize one was never truly wanted in the place they first called home...'"
    "Speaking gently, as a small breath of smoke escaped his lips, as he continued."
    hide wrathsmile
    show wrath at left
    W "'That grief doth not fade easily. But thou art not alone in it now.'"
    "Seemingly not meaning just his own, old self this time, but also glancing to Sable upon the devils shoulders, who was just curiously listening to the conversation. Making note of how Lucifer sounded in regards to Heaven."
    "Lucifer draws a breath in, before allowing it to escape her chest."
    show lucifercr at right, breathe
    L "'Right. It'll just get easier. Thank you, Wrath.'"
    hide lucifercr
    hide wrath
    hide sablewrathcig
    scene black
    with dissolve
    stop music fadeout 1.0
    "With that, and after a small goodbye, Lucifer heads back up to the layer that rests above them all, where she resides. Limbo."
    scene Monochrome Garden
    play music "audio/melancholy.mp3" fadein 1.0 loop
    with dissolve
    "Coming to a throne in the midst of a monochrome garden, setting Sable down from her shoulders, onto the crackling, grey ground."
    show Lucifer Throne
    with dissolve
    L "'I'm... assuming you have questions. About me and God. I think it's only fair you know everything.'"
    "Sable decided to sit before the throne, one leg crossed over the other. Glancing up at Lucifer as she was unsure, she didn't want to upset her again."
    show sablesad at left
    S "'I... just wasn't sure if it was alright to ask about that, given how you had first reacted to just the name alone.'"
    S "'But I'd be lying if I said I wasn't curious. So then... what {i}really{/i} happened?'"
    hide sablesad
    pause 
    L "'There are... things you should see. Before I tell you what happened...'"
    jump chapter_three_start

label chapter_three_start:

    menu:
        "Show me.":
            jump creation_memory

        "Well, I don't know...":
            L "'You won't understand, until you see it for yourself, first hand.'"
            L "'Just... prepare yourself.'"
            stop music fadeout 1.0
            jump creation_memory
    
    #FLASHBACK TO SMALL MOMENTS TO HEAVEN IN THE PAST
    #CHAPTER 3: THE FALL
    #a lot of fade ins and outs to black will be used, as a lot of time skips will happen in this chapter
    label creation_memory:
        scene black with fade
        pause 1.0
        play music "audio/Innocent.mp3" fadein 1.0 loop
        scene Heaven with dissolve
    "A seed splits open from nothing."
    show Birth with dissolve
    "Light condenses into feminine-form, radiant, born from tears of a larger being. Cradling her in both palms."
    G "'Well, hello there, my first, beautiful angel...'"
    hide Birth
    pause
    show The First with dissolve
    G "'{b}Lucifer~{/b}'"
    pause 3.0
    scene black with fade
    hide Heaven
    hide The First
    "Memories unfold..."
    jump eden_memory

    label eden_memory:
        scene Eden with dissolve
        play sound "audio/Eden.mp3" fadein 1.0
        show Unity with dissolve
        "Two women walk in paradise."
        "One senses something wrong... the other dismisses her, not out of malice, but from a lack of understanding."
        hide Unity
        show AdamPlot with dissolve
        "A man stands in the shadows observing the women in a predatory manner."
        scene black with fade
        stop sound fadeout 1.0
        stop music fadeout 1.0
        hide AdamPlot
        play music "audio/Eden2.mp3" fadein 1.0 loop
        scene Sunset with dissolve
        show ELAssault at spasm
        with dissolve
        pause 3.0
        scene black with fade
        hide Sunset
        hide ELAssault

        jump noah_memory
    label noah_memory:
        scene The Ark with dissolve
        "A boat. A deluge. A reset button."
        "She saved what she could- and let the rest drown."
        scene The Flood at shiver
        show God Stare
        with Fade(1.5, 0.5, 1.5)

        pause 3.0
        scene black with fade
        hide The Flood
        hide God Stare
        stop music fadeout 1.0
        play music "audio/Horror2.mp3" fadein 1.0 loop
        jump jesus_memory
    label jesus_memory:
        scene Cross
        with Fade(1.5, 0.5, 1.5)
        scene Crucify
        with Fade(1.5, 0.5, 1.5)
        hide Cross
        "Death. Resurrection. Something wrong and not quite right about her light."
        scene Tomb
        with Fade(1.5, 0.5, 1.5)
        "The woman rose- but what awoke... wasn't right."
        scene TombEyes with fade
        pause 3.0
        play sound "audio/Fleshy.mp3" fadeout 1.0
        with Fade(1.5, 0.5, 1.5)
        "Celestial mixed with mortal DNA. Impossible. Unstable."
        scene Gore at spasm
        stop sound fadeout 1.0
        "God herself ended what she tried to save."
        pause 3.0
        play sound "audio/Monster.mp3"
        scene Jesus at screen_shake
        show Bloodonhands with fade
        pause
        scene black with fade
        hide Jesus
        hide Gore
        hide Bloodonhands
        stop music fadeout 1.0
        stop sound fadeout 1.0

        jump the_fall_memory
    label the_fall_memory:
        play music "audio/Uncertainty.mp3" fadein 1.0 loop
        "The fall."
        scene Flowers with fade
        "A descent into darkness, a loss of innocence."
        "The light that once shone so brightly, now dimmed to a mere flicker."
        "A world torn apart by the weight of its own creation."
        "Tears fall, blood shed from a torn wing."
        show Lucifer Fallen
        with Fade(1.5, 0.5, 1.5)
        "The pleading, desperation, all ignored in pain, as Lucifer fell."
        scene The Fall 
        with Fade(1.5, 0.5, 1.5)
        pause 3.0
        play sound "audio/impact.mp3"
        scene black with fade
        hide Lucifer Fallen
        hide The Fall
        stop music fadeout 1.0
        stop sound fadeout 1.0

        jump chapter_three_end
    label chapter_three_end:
        #back with Lucifer and Sable
#Continue Chapter 3 to End
    play music "audio/melancholy.mp3" fadein 1.0 loop
    scene Monochrome Garden with fade
    "There was a strong silence, as Sable stared down at her shoe laces, putting out one of her many cigs she had smoked throughout the memories recalled to her."
    scene Shoes with fade
    "Her eyes wide, like she felt she wasn't meant to hear any of that. Information hard to wrap around a mortal's brain."
    scene Monochrome Garden
    show Lucifer Throne 
    S "'That's... a lot of baggage, between you both. I'm sure there is more that you haven't told me yet.'"
    show sablesad at left
    S "'Despite it all, you agreed to start seeing her again? Why? Are you sure you're going to be alright with that?'"
    "Obviously, it seemed that Sable was concerned for Lucifer."
    L "'Honestly? I'm not. But it feels like I don't have a choice. She will {i}keep{/i} coming back, and it feels like I'm the only one who can keep her in check.'"
    show Lucifer Throne at center, breathe
    L "'She's been {i}super unstable{/i} lately.'"
    L "'And Gabriel and Michael... I don't trust those fuckers to stay out of her head.'"
    "Explaining with a long sigh, snagging one of Sable's own cigarettes from the box, summoning a flam upon her finger to light it. Taking a long drag."
    hide Lucifer Throne
    play sound "audio/Burn.mp3"
    show FlameFinger with fade
    L "'Fucking stupid...'"
    pause
    S "'But... you have your own autonomy, right?'"
    show sablesad at left, sink
    S "'I just feel like you deserve someone who is going to actually care about you, and well, love you for all you are, y'know?'"
    S "'Does she even do that for you? Has she ever?'"
    hide sablesad
    show sablecrsad at left
    hide FlameFinger
    show lucifercr at right, breathe
    "'Lucifer paused for a long while, as if retracing all of her memories...'"
    scene Innocence
    show God Smug
    with Fade(1.5, 0.5, 1.5)
    pause 3.0
    scene InnocenceLost 
    show God Assault 
    show Stop at topleft,spasm
    show Stop at right, spasm
    pause
    scene black with fade
    hide sablecrsad
    hide Innocence
    hide God Smug
    hide God Assault
    hide Stop
    hide InnocenceLost
    scene Monochrome Garden
    "A single tear rolls down her cheek, as she stares off for a moment, blowing out some smoke from the cigarette."
    L "'That's just it. I don't know... I've never felt loved, but she swears she did. I can't tell the difference anymore.'"
    show lucifercrsad at right, shiver
    L "'And no matter how tough or above her I act, every time we are face-to-face, I still feel like I'm that sorry, obedient-to-a-fault angel.'"
    pause  
    "'Staring up at Lucifer, her eyes widened slightly as she noticed the state of mind the demon queen seemed to be in.'"
    show sablecrsad at left, breathe
    S "'So... you don't even know what real love feels like. I mean, to be fair, I don't either. So, it's not like I could describe it, even if I tried.'"
    "Seeming a bit ashamed of that fact, it would seem..."
    S "'I think... That is definitely something you and her have to figure out. I can... {i}try{/i} helping, at least give you someone else to talk to, who is willing to listen?'"
    S "'I'm normally told that I'm a great listener anyway.'"
    "The queen of hell couldn't help but chuckle lightly as she looked over to Sable."
    hide lucifercrsad
    show lucifercrsmug at right
    L "'A mortal offering to help the queen of hell. You're truly an enigma... Thank you, Sable.'"
    pause  
    S "'I mean, everyone deserves kindness, don't they? No matter how they are perceived, you don't know what's underneath the shell. Unless they let you get close.'"
    S "'So, if I can give you, even a {i}shred{/i} of kindness that you've been missing, for who knows how long, then that makes me happy to know.'"
    hide sablecrsad
    show sablecr at left
    S "'I was never shown kindness in my life, so the most I can do, is show kindness where I can.'"
    "Lucifer couldn't help but chuckle a bit, agreeing with her sentiment as she places a small kiss on Sable's forehead."
    hide lucifercrsmug
    show lucifersmug at center, bounce
    L "'Your morals alone make you more deserving to be an angel, than almost all the ones in heaven currently.'"
    hide lucifersmug
    show lucifercr at right
    "Feeling her face flush to the compliment, Sable looked away for a moment, smiling softly."
    S "'That is... that is really kind of you to say. Probably the best compliment I've ever received.'"
    hide sablecr
    show sablecrflush at left, breathe
    pause  
    stop music fadeout 1.0
    hide sablecrflush
    play sound "audio/Rumble.mp3"
    play music "audio/Drone.mp3"fadein 1.0 loop
    scene Monochrome Garden at screen_shake
    "Suddenly, Hell trembles. Not from Wrath's circle- but from {b}ABOVE.{/b}"
    "A crack forms in the monochrome sky of Limbo, bleeding golden light."
    show lucifer at center, sink
    L "'She's back...'"
    scene End 
    "Before them, floating at the edge of Hell, is none other than God. With Gabriel and Michael flanking her like wolves."
    show god at center, bounce
    G "'Lucifer...~'"
    stop music fadeout 1.0
    jump credits

label credits:
    scene black with fade
    play music "audio/InnocenceSong.mp3"
    call screen credits

    stop music fadeout 3.0
    scene EndSplash
    with dissolve
    pause 8.0
    #will add more credits once i finish the art, and adding the audios and backgrounds

    return
