def choice(question,op1,op2,out1,out2):
    done = False
    while not done:
        if not done:
            userinput = input(question)
            if userinput == op1:
                print(out1)
                done = True
            elif userinput == op2:
                print(out2)
                done = True
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
question1 = "Are you nice to your father or mean? "
q1option1 = "mean"
q1option2 = "nice"
q1outcome1 = '''
You say, "Hell yeah it's a long time. And a great time too since I haven't seen you
in five years."

Your father's face turns bright red. He is very mad. You were very rude, which he
isn't used to because all of his employees bow down to him.

"I have terminal breast cancer, Beatrice (pronounced bee-uh-treese). I am going to
die soon. I was going to give you all of my millions from my dog shampoo formula
business for which I have become known for, but now, I don't know. You will need
to prove yourself to me. Why would I give my inheritance to someone who doesn't
love me?"

Beatrice (pronounced bee-uh-treese) regrets her decision to be mean.
'''
q1outcome2 = '''
You say, "What happened?? Are you okay? I've missed you, my dear father."

Your father's gaunt face brightens when he hears your loving tone. He isn't used
to so much love, only respect due to fear.

"I've missed you too, daughter. I have terminal breast cancer, Beatrice
(pronounced bee-uh-treese). I am going to die soon. I am planning on giving you
all of my millions from my dog shampoo formula business for which I have become
known for. I want to give my inheritance to someone who loves me, and it feels
like that's you, Beatrice (pronounced bee-uh-treese)."

Beatrice (pronounced bee-uh-treese) is happy with her decision to be nice.
'''
# first choice: Nice or mean to father?
print(intro)
choice(question1, q1option1, q1option2, q1outcome1, q1outcome2)

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

question2 = "Do you stare back or glance away? "
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
choice(question2, q2option1, q2option2, q2outcome1, q2outcome2)
