import random
##dict of response for each type of intent

intent_response_dict = {
    "intro": ["This is a GST FAQ bot. One stop-shop to all your GST related queries"],
    "greet":["Hey","Hello","Hi"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"],
    "thanks": ["You're welcome", "Of course"],
}

fact_response_list = [
    "The first computer programmer was a female, named Ada Lovelace.",
    "The first computer “bug” was identified in1947 as a dead moth.",
    "Did you know how many total programming languages? – it’s 698.",
    "Python was named after the comedy troupe Monty Python. That is why you will often see spam and eggs used as variables in examples (a little tip of the hat to Monty Python’s Flying Circus)",
    "Python is an interpretive language, meaning you don’t need to compile it. This is great for making programs on the fly, but does make the code rather slow compared to compiled languages",
    "Python is part of the open source community, meaning plenty of independent programmers are out there building libraries and adding functionality to Python.",
    "Python is one of the official languages at Google"
]

def get_fact_response():
    # rand_num = random.choice(len(fact_response_list)-1)
    return random.choice(fact_response_list)
