## ------ gstfaq ----
import random
##dict of response for each type of intent
# I think this is the knowledge base?
intent_response_dict = {
    "intro": ["This is a GST FAQ bot. One stop-shop to all your GST related queries"],
    "greet":["Hey","Hello","Hi"],
    "goodbye":["Bye","It was nice talking to you","See you","ttyl"],
    "affirm":["Cool","I know you would like it"]

}

gstinfo_response_dict = {
    "GST": " Goods and Service Tax (GST) is a destination based tax on consumption of goods and services.",
    "benefits":"GST consumes more than a dozen taxes, thus making it hassle free and efficient.",
    "faq_link":'You can check all the answers here <a href="http://www.cbec.gov.in/resources//htdocs-cbec/deptt_offcr/faq-on-gst.pdf</a>'
}

gst_query_value_dict = {
    "12%":"Non-AC hotels, business class air ticket, frozen meat products, butter, cheese, ghee, dry fruits in packaged form, animal fat, sausage, fruit juices, namkeen and ketchup",
    "5%":"railways, air travel, branded paneer, frozen vegetables, coffee, tea, spices, kerosene, coal, medicines",
    "18%":"AC hotels that serve liquor, telecom services, IT services, flavored refined sugar, pasta, cornflakes, pastries and cakes",
    "28%":"5-star hotels, race club betting,wafers coated with chocolate, pan masala and aerated water",
    "exempt":"education, milk, butter milk, curd, natural honey, fresh fruits and vegetables, flour, besan"
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

def gst_info(entities):
    if entities == None:
        return "Could not find out specific information about this ..." +  gstinfo_response_dict["faq_link"]
    if len(entities) == 1:
        return gstinfo_response_dict[entities[0]]
    return "Sorry.." + gstinfo_response_dict["faq_link"]

def gst_query(entities):
    if entities == None:
        return "Could not query this ..." + gstinfo_response_dict["faq_link"]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        if qtype == "gst-query-value":
            return gst_query_value_dict[qval]

        return gstinfo_response_dict[entities[0]]
    return "Sorry.." + gstinfo_response_dict["faq_link"]
