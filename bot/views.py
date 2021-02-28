from django.shortcuts import render

# Create your views here.
import random
name=""
def signup(request):
        return render(request, 'signup.html')
def calendar(request):
        fo=open("details.txt","r")
        l=fo.readlines()
        global name
        for i in l:
                if name in i:
                        s=i.split()
        sd=s[4][:2]
        freq=s[5] 
        return render(request, 'calender.html', {"sd":sd,"freq":freq})
def home(request):
    if request.method=="POST":
        if request.POST['h']:
                r=ord(request.POST['h'])
                print(r)
                if r==128512:
                        s="That's Great! Keep seeking positivity. Use the bot to share your happiness."
                        return render(request, 'home.html',{"r":s})
                if r==128557:
                        s="Hope you feel better soon. Remember, these sad times too shall pass. Try using our bot to express yourself."
                        return render(request, 'home.html',{"r":s})
                if r==128545:
                        s="Take some deep breaths. Count to ten. Once you feel less frustrated, do a deep introspection. Also try using our bot to vent your anger."
                        return render(request, 'home.html',{"r":s})
                if r==128561:
                        s="Evaluate what caused feelings of shock in you. Use the bot to introspect."
                        return render(request, 'home.html',{"r":s})
                if r==128560:
                        s="Think happy thoughts and take deep breaths. Try to compose yourself. You have the strength in yourself to overcome your fear. Use the bot to feel lighter."
                        return render(request, 'home.html',{"r":s})
                print(r)
    else:
            return render(request, 'home.html')

def web(request):
        if request.method=="POST":
                print("yo")
                global name
                name=request.POST["name"]
                psd=request.POST["psd"]
                dn=request.POST["dn"]
                dd=request.POST["dd"]
                sd=request.POST["sd"]
                freq=request.POST["freq"]
                fo=open("details.txt","a")
                fo.write(name+" "+psd+" "+dn+" "+dd+" "+sd+" "+freq+"\n")
                fo.close()
                return render(request, 'home.html')
        else:
                return render(request, 'home.html')
def bot(request):
    if request.method=="POST":
        n=0
        s=""
        m=request.POST["m"]
        m=m.lower()
        m=" "+m
        print(m)
        if "kill" in m or "suicide" in m or "suicidal" in m or "self harm" in m or "harm" in m:
            s= "You matter. Even if everything else seems otherwise, you matter. You are loved. You can get through this. Take a deep breath. If you have somebody you can talk to please call them right now. Use the helpline number mentioned below:\n 91-9820466726. Take care"
        elif "heal" in m:
            s="Type the number corresponding to the technique you would like to participate in: 1. Recieve a complement 2. Positive affirmation for the day 3. Gratitude check"
        elif m==" 1":
            l=["The world needs more people like you! You have so many gifts and so much to offer. Your determination is a testament to your character", "You inspire others to be better people. You are valued. You matter","Your strength is truly inspiring! You fight so hard and I have no doubt that there is lots of success and happiness coming your way"]
            s= random.choice(l)
        elif m==" 2":
            n=1
            l=["I am better than what I used to be. I am better than what I was yesterday. But not as good as I will be tomorrow! Every time I do something, I come out a better version of myself.","I am enough. I am amazing and I am grateful for all the things that I have. I love myself through thick and thin and am a magnet for all good things. I attract healthy people into my life and am capable for anything I set my mind to!","In this moment I feel peaceful and content. I always seek positivity in everyone and everything. I am happy, joyous and free, exactly as I was born to be!"]
            s="Positivity starts from within. Repeat the following to yourself: "+random.choice(l)
        elif m==" 3":
            s="Type something that you are grateful for "
        elif "grateful" in m:
            s="That's wonderful! Keep reminding yourself of all the good things happening in your life and use it to motivate yourself and keep fighting. You're doing really well, and you're incredibly strong"
        elif m in [" hello"," hi"," hey"]:
            s="Hi! How are you feeling?"
        elif "manager" in m or "boss" in m or "student" in m or "teacher" in m or "acquaintance" in m or "relative" in m or "wife" in m or "husband" in m or "boyfriend" in m or "girlfriend" in m or "bf" in m or "gf" in m or "neighbour" in m or "child" in m or "daughter" in m or "son" in m or "colleague" in m or "mom" in m or "dad" in m or "friend" in m or "mother" in m or "father" in m or "amma" in m or "appa" in m or "mommy" in m or "daddy" in m or "mummy" in m or "mum" in m or "brother" in m or "sister" in m or "grandma" in m or "grandpa" in m or "aunt" in m or "uncle" in m or "cousin" in m or "grandmother" in m or "grandfather" in m:
                l=["mother","father","mom","mum","dad","mummy","mommy","daddy","brother","sister","friend","aunt","uncle","grandpa","grandma","grandfather","grandmother","amma","appa","cousin","colleague","neighbour","son","daughter","child","girlfriend","boyfriend","gf","bf","husband","wife","relative","acquaintance","teacher","student","boss","manager"]
                for i in l:
                    if i in m:
                        s="Tell me more about your "+i
        elif " he " in m or " she " in m or " her " in m or " him " in m or " his " in m or " they " in m or " them " in m or " their " in m:
            if "he" in m or "him" in m or "his" in m:
                s="If he means a lot to you, cherish your relationship with him. If he helps you grow as a person, work on your relationship with honesty, trust and respect. But if his actions ever cause a toxic influence on your life, stand up for yourself and make your voice heard.\n Remember, you should be your first priority."
            elif "she" in m or "her" in m:
                s="If she means a lot to you, cherish your relationship with her. If she helps you grow as a person, work on your relationship with honesty, trust and respect. But if her actions ever cause a toxic influence on your life, stand up for yourself and make your voice heard.\n Remember, you should be your first priority."
            elif "they" in m or "them" in m or "their" in m:
                s="If they means a lot to you, cherish your relationship with them. If they help you grow as a person, work on your relationship with honesty, trust and respect. But if their actions ever cause a toxic influence on your life, stand up for yourself and make your voice heard.\n Remember, you should be your first priority."
        elif "new" in m:
                i=m.find("new")
                m2=m[i+4:]
                s="Changes are up to you and the unpredictable events in life. You are in charge of your own destiny. Be your best self and do what you think is right. Hope you get a new "+m2+"!"
        elif ("good" in m and "not good" not in m) or "not bad" in m:
            s="That's nice to hear! Any progress is an achievement worth celebrating no matter how big or small it is"
        elif ("bad" in m and "not bad" not in m) or "not good" in m:
            s="Don't worry too much. Take things one day at a time, one step at a time"
                
        elif "yes" in m or " no " in m:
            if "yes" in m:
                  s="Only do what you feel is right for you. Tell me more about your day."
            if "no" in m:
                  s="Only do what you feel is right for you. Tell me more about your day."
        elif ' i ' in m:
            m1="you"
            if "feeling" in m:
                i=m.find("feeling")
                m2=m[i+8:]
                s="What makes "+m1+" feel "+m2+"?"
            elif "feel" in m:
                i=m.find("feel")
                m2=m[i+5:]
                s="What made "+m1+" feel "+m2+"?"
            elif " don't " in m or "can't" in m:
                s="Your peace of mind should hold precedence over all external factors. Don't do something just because you're forced to. Do it if you WANT to. Don't exert yourself."
            elif "want to" in m:
                i=m.find("to")
                m2=m[i+3:]
                if "my" in m2:
                    m2=m2.replace("my","your")
                s="What would getting to "+m2+" mean to "+m1+"?"
            elif "need" in m:
                i=m.find("need")
                m2=m[i+5:]
                s="Are you sure "+m2+" will help you?"
            elif "have to" in m:
                i=m.find("have to")
                m2=m[i+8:]
                s="Does the environment you're in play a role in you having to "+m2+"?"
            elif " will " in m or " am " in m:
                s="Work hard and prioritize yourself. When you have a positive outlook on life, good things start happening."
            elif "should" in m or "shall" in m:
                if "should i" in m:
                    i=m.find("should i")
                    m2=m[i+9:]
                    s="Why do you think you should "+m2+"?"
                elif "i should" in m:
                    i=m.find("should")
                    m2=m[i+7:]
                    s="Why do you think you should "+m2+"?"
                elif "i would" in m:
                    i=m.find("would")
                    m2=m[i+7:]
                    s="Why do you think you would "+m2+"?"
                elif "shall i" in m:
                    i=m.find("shall i")
                    m2=m[i+8:]
                    s="Why do you think you should "+m2+"?"
                elif "would i" in m:
                    i=m.find("would i")
                    m2=m[i+8:]
                    s="Why do you think you would "+m2+"?"
                elif "i shall" in m:
                    i=m.find("shall")
                    m2=m[i+7:]
                    s="Why do you think you should "+m2+"?"
            elif " can " in m or "could" in m or " may " in m or " might " in m:
                s="Prioritze your well being. Go ahead with your decision if you are confident and comfortable with it."
            elif "hate" in m:
                s="Hate is a strong word. Introspect and look for positivity. I recommend using some of our healing techniques"
            elif "love" in m:
                s="Remember to stay positive and look our for yourself"                
            else:
                s="Please elaborate if you wish to express more. Never forget that your happiness comes above everything else."
        elif "thank you" in m:
            s="Always there for you"
        elif "sorry" in m:
            s="Don't be sorry. I'm always here to help you!"
        else:
            s="Please elaborate if you wish to express more. Never forget that your happiness comes above everything else."
        
        if n==0:    
            s=s.replace(" i ","you")
            s=s.replace("my","your")
            s=s.replace("mine","yours")
        print(s)
        return render(request, 'bot.html',{"rep":s})
    else:
        return render(request, 'bot.html')
