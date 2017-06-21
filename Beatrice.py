def choice(question,op1,op2,out1,out2):
    done = False
    while not done:
        if not done:
            userinput = input(question)
            if userinput == op1:
                print(out1)
                done = True
                return "outcome1"
            elif userinput == op2:
                print(out2)
                done = True
                return "outcome2"
            else:
                done = False

intro = '''
    -------------------- START ---------------------

    You are Beatrice (pronounced bee-uh-treese). Your celebrity father (famous for his
    fabulous dog shampoo brand) has asked you to visit him for the first time in years.
    He tells you to visit him in the hospital, and you are confused.

    You walk into his room. He sits up omniscently in a hospital bed and stares at you
    expectantly as you sit down.

    "Hello, Beatrice (pronounced bee-uh-treese), it's been a long time."
'''
question1 = "- Are you nice to your father or mean? "
q1option1 = "mean"
q1option2 = "nice"
q1outcome1 = '''
    You say, "Hell yeah it's a long time. And a great time too since I haven't seen you
    in five years."

    Your father's face turns bright red. He is very mad. You were very rude, which he
    isn't used to because all of his employees bow down to him.

    "I have cancer from accidentally injesting too much dog shampoo, Beatrice
    (pronounced bee-uh-treese). I am going to die soon. I was going to give you all
    of my millions from my dog shampoo formula business for which I have become known
    for, but now, I don't know. You will need to prove yourself to me. Why would I
    give my inheritance to someone who doesn't love me?"

    Beatrice (pronounced bee-uh-treese) regrets her decision to be mean.
'''
q1outcome2 = '''
    You say, "What happened?? Are you okay? I've missed you, my dear father."

    Your father's gaunt face brightens when he hears your loving tone. He isn't used
    to so much love, only respect due to fear.

    "I've missed you too, daughter. I have cancer from accidentally injesting too much
    dog shampoo, Beatrice (pronounced bee-uh-treese). I am going to die soon. I am
    planning on giving you all of my millions from my dog shampoo formula business for
    which I have become known for. I want to give my inheritance to someone who loves
    me, and it feels like that's you, Beatrice (pronounced bee-uh-treese)."

    Beatrice (pronounced bee-uh-treese) is happy with her decision to be nice.
'''
# first choice: Nice or mean to father?
print(intro)
if choice(question1, q1option1, q1option2, q1outcome1, q1outcome2) == "outcome1":
    fatherMad = True
else:
    fatherMad = False

story1 = '''
    After speaking with your father, you rush outside to get some fresh air. You see
    a strange sight. It's your dopplegangers! THREE of your dopplegangers. You've
    met these bitches before, and they tried screwing up your life. They're probably
    trying again. You go talk to them.

    As you walk up, you can distinguish each of them. The first doppleganger is
    Beatrice (pronounced normally). She always wears the color gray, which matches
    her gray personality. You have never seen her smile or frown. She looks dead
    inside. One time the two other dopplegangers threw her a surprise birthday party.
    She didn't even blink.

    The second doppleganger is Beatriz (Beatrice in Spanish). She always wears the
    color red, which is the color of anger and passion. You think back to the time
    she stole your boi. You still have scorch marks on your wall from the resulting
    fight. She always looks like the hotter version of you, and you hate it.

    The last doppleganger is Beatris (yes, spelled like that). She always wears
    sunshine yellow, to match her manic happiness. She is a very joyful person,
    especially when she's tormenting you. You wonder if she is sane, and you think
    she would look amazing in a padded room (Especially after the time she fried a
    goldfish. Yes. A real goldfish. Not the snack that smiles back. No smiles.).

    "Hello, Beatrice (pronounced bee-uh-treese)," the dopplegangers say in unison.

    "Hello, evil bitches," you retort.

    "Actually, we go by 'the B-Dops' now," Beatriz (the one wearing red) says sassily,
    "Short for Beatrice (pronounced bee-uh-treese) dopplegangers"

    "What do you want?" you ask, fiercely.

    "We want your insanely famous father's bling bling, if you know what I mean. The
    mulah. The ka-ching ka-ching" emphasizes Beatris (the one wearing yellow).

    You briefly make eye contact with each of them, finally landing on Beatrice
    (pronounced normally, the one wearing gray). Her stare seems never ending and as
    deep as the sea.
'''

question2 = "- Do you stare back or glance away? "
q2option1 = "stare back"
q2option2 = "glance away"
q2outcome1 = '''
    You stare intensely back at Beatrice (pronounced normally), and for the first
    time in your life, you see a flicker of emotion. The emotion is pure hatred. You
    feel as though you've entered the depths of hell as you stare into her eyes.

    Maybe you've made a mistake...
'''
q2outcome2 = '''
    You glance away, but before you do for the first time in your life you see a
    flicker of emotion. The emotion is self-doubt. You feel like Beatrice (pronounced
    normally) looks regretful. Maybe she regrets all the evil in her life.

    Beatrice (pronounced bee-uh-treese) feels like she's made the right decision.
'''

# second choice: stare or glance away
print(story1)
if choice(question2, q2option1, q2option2, q2outcome1, q2outcome2) == "outcome1":
    beatriceMad = True
else:
    beatriceMad = False

story2 = '''
---
    You wake up suddenly. It is the next day, now. You remember yesterday's events
    and decide to go visit your father again. You want to make sure the B-Dops aren't
    causing any trouble.
'''
story2_1 = '''
    You decide to bring your father a gift because of how mean you were to him. You
    want his inheritance, but more importantly, his love.
'''
story2_2 = '''
    You decide to bring your father a gift. His reaction to your kindness yesterday
    was so satisfying, so you want to be as kind as possible again.
'''

question3 = "- Do you bring flowers or chocolate? "
q3option1 = "flowers"
q3option2 = "chocolate"
q3outcome1 = '''
    You stop by the florist on the way to the hospital and buy some beautiful roses.
'''
q3outcome2 = '''
    You stop by the candy store on the way to the hospital and buy some delicious
    chocolate.
'''

print(story2)
if fatherMad:
    print(story2_1)
else:
    print(story2_2)
# choice between flowers and chocolate
choice(question3, q3option1, q3option2, q3outcome1, q3outcome2)

story3 = '''
    When you arrive at the hospital, you enter your father's room and stand in shock.
    The B-Dops are back. You scoff. Beatrice-Dops?? More like BISH-Dops.

    Not only have they returned, they have all donned the exact same outfit as you.
    They must have seen you while you were out shopping for a gift.

    Your father looks very bewildered.

    "I regret tripping so much in college. The hallucinations haven't stopped," he
    says under his breath.

    "Dad, this is real life. Sadly." You say sternly as you glare over at the B-Dops.

    "What???" he gasps, "Then who's my real daughter?"

    "I AM!" You and the B-Dops say in unison.

    "I REALLY shouldn't have tripped so much in college," your father stares up at
    the ceiling in regret. "If this isn't a hallucination, you must sort this out
    immediately because I will die soon. Real soon."

    You realize how to prove you're his real daughter: with a paternity test!

    "I'll go to the DNA testing center! (if it's a thing)" you say.

    "Haha!! We already put traps there," say the B-Dops.

    "What, how?" you ask increduously.

    "We plan ahead! We're notoriously evil because of it!"

    You all rush out of the hospital and head to the nearest DNA Test Center. This
    particular test center was recently featured on the latest episode of "Who's the
    Daddy?!" hosted by Dr. Bhil. That particular episode was also sponsored by your
    dad's dog shampoo business.

    When you arrive, you know this is going to be a hard task to complete. This is
    indicated by the huge army of landsharks with guns. Both types of guns: the
    muscle type and the shooty type.

    You see that the only ways to escape the army is via the bridge over sharky water
    or a tunnel that may be populated with spiders.

'''

question4 = "- Do you take the bridge or the tunnel? "
q4option1 = "bridge"
q4option2 = "tunnel"
q4outcome1 = '''
    You take the bridge, tediously crawling across the creaky and unstable planks.
    On the other side you see two guys. One is hot and one is not.
'''
q4outcome2 = '''
    You take the tunnel, sure that you avoided the traps your dopplegangers left. You
    see a spider and gasp. It attacks your face. You are now dead.
'''
print(story3)

if choice(question4, q4option1, q4option2, q4outcome1, q4outcome2) == "outcome2":
    print("-----------------GAME OVER-------------------")
else:
    question5 = "- Do you talk to the hot guy or the not guy? "
    q5option1 = "hot guy"
    q5option2 = "not guy"
    q5outcome1 = '''
    You say hello and he immediatley proposes. You are now dead. Ain't nobody got
    time for commitment.
    '''
    q5outcome2 = '''
    You say hello and the not guy answers with a question. The not guys asks "If I
    were in danger, would you rescue me?"

    You think it is a strange question, but since it is not the stangest thing
    that you've ever been asked, you answer.
    '''
    if choice(question5, q5option1, q5option2, q5outcome1, q5outcome2) == "outcome1":
        print("-----------------GAME OVER-------------------")
    else:
        question6 = "- Do you answer yes or no? "
        q6option1 = "yes"
        q6option2 = "no"
        q6outcome1 = '''
    You say "yes" and the not guy smiles. He gives you the key to the final door
    to the lab because of your chivalry.
        '''
        q6outcome2 = '''
    You say "no" and the not guy grimaces. He pulls out the key to the final door
    and says, "You could've gotten this, but you playin". Then he swallows the key
    and dies. You failed.
        '''
        if choice(question6, q6option1, q6option2, q6outcome1, q6outcome2) == "outcome2":
            print("-----------------GAME OVER-------------------")
        else:
            story4 = '''
    You use the key to the door and are appalled to see a wall in front of you.
    After you walk a few steps, you realize you are in a maze. Those B-Dops are
    truly evil.

    There is a gray pathway pointing right and a red pathway pointing to the left.

    The colors remind you of two of the B-Dops. You shudder with disgust and
    wonder which way to go.
    '''
            question7 = "Do you go right or left?"
            q7option1 = "right"
            q7option2 = "left"
            q7outcome1 = '''

            '''
            q6outcome2 = '''

            '''
            if choice(question6, q6option1, q6option2, q6outcome1, q6outcome2) == "outcome2":
                print("-----------------GAME OVER-------------------")
