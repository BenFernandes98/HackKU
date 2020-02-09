import random

def main():
    textFile=open('Ramsay Insults + Hawaiian', 'w+')

    insults=["This is a really tough decision, because you're both crap.\n",
             "Your cooking is so terrible you can't even apply for McDonalds.\n",
             "You both are an idiot cornwhich.\n",
             "The fish is so raw he's still finding nemo.\n",
             "The crab is so undercooked it's singing under the sea.\n",
             "I wish you'd jump in the oven! That would make my life a lot easier!\n",
             "I wouldn't trust you running a bath, let alone a corn restaurant.\n",
             "This lamb is so undercooked, it's following Mary to school.\n",
             "There's enough garlic in here to kill every vampire in Europe.\n",
             "Why did the chicken cross the road? Because you didn't flippin cook it!\n",
             "This pizza is so disgusting, if you take it to Italy you'll get arrested.\n"]
   
    randomGen=random.randint(0,len(insults)-1)
    

    hawaiian=["He hoʻoholo paʻakikī loa kēia, no ka mea ʻoi oulua ʻelua",
              "Eia nō kā mākou kuke ʻai ʻana ke hiki ʻole iā ʻoe ke noi no McDonalds.",
              "ʻO ʻoe ʻelua kahi ʻāpala ʻōlelo ʻole.",
              "He ʻala ka iʻa a ke ʻike ʻo ia i ka nemo.",
              "Puka ka lalo, ua mele ʻia ma lalo o ke kai.",
              "Makemake wau e lele i loko o ka umu! E hōʻoluʻolu ʻia koʻu ola!",
              "ʻAʻole au e hilinaʻi iā ʻoe e holo ana i ka ʻauʻau, e waiho ʻoe i kahi hale ʻai palaoa.",
              "Hana ʻia kēia keikikāne e hahai ana iā Mary ma ke kula.",
              "Ua nui kahi keokeo ma aneʻi e pepehi i kēlā me nā vampire ma ʻEulopa.",
              "No ke aha i lele ai ke moa i ke ala? No ka mea, ʻaʻole ʻoe i flippin e kuke ai!",
              "He mea ʻinoʻino kēia pizza, inā lawe ʻoe ia i Italia e hopu ʻia ai ʻoe."]
              
    textFile.write(insults[randomGen])

    textFile.write("Here is your insult in Hawaiian:" + hawaiian[randomGen])

    
    textFile.close()
main()
             
             
             
             
             
