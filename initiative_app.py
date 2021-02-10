import pandas as pd
import numpy as np 
import streamlit as st

#create the header for the app
st.header('Carus Campaign: Initiative Tracker')

#write some text to the app
st.write("This app will re-create initiative rolls for all PCs and NPCs at the end of a combat round.")


#load in the class for PCs
#always recreate PC initiatives
#default initiatives in self

#low value is inclusive, high value is exclusive
#nested for loop to generate random numbers between 1 and 20 for each character and add their initiative modifier
#make the output of the for loop a dictionary to be used in dataframe creation

class Milfnitiative:
    
    def __init__(self, alain_init=3, alain_name='Alain', 
                 cass_init=4, cass_name='Cassandra', 
                 wildhrt_init=1, wildhrt_name='Wildheart', 
                 idalia_init=1, idalia_name='Idalia'):
        self.alain_init = alain_init
        self.alain_name = alain_name
        self.cass_init = cass_init
        self.cass_name = cass_name
        self.wildhrt_init = wildhrt_init
        self.wildhrt_name = wildhrt_name
        self.idalia_init = idalia_init
        self.idalia_name = idalia_name
    
    #create new initiative for each PC
    def pc_initiative(self):
        pc_init_dict = {}
        #name's of the PC's for dict keys
        pc_list = [self.alain_name, self.cass_name, self.wildhrt_name, self.idalia_name]
        for char in pc_list:
            pc_init_dict[char] = (np.random.randint(low=1, high = 21))
            
            #print('The pc dictionary before modifier addition.')
            #print(pc_init_dict)
            
            #if statement to add in the modifier for each pc
            if char == 'Alain':
                pc_init_dict[char] = pc_init_dict[char] + self.alain_init
            elif char == 'Cassandra':
                pc_init_dict[char] = pc_init_dict[char] + self.cass_init
            elif char == 'Wildheart':
                pc_init_dict[char] = pc_init_dict[char] + self.wildhrt_init
            else:
                pc_init_dict[char] = pc_init_dict[char] + self.idalia_init
            
        #return the dictionary of names and initiatives    
        return pc_init_dict

#create class milfnitiative instance
milf_initiative_instance = Milfnitiative()
#return the milves initiatives in a dictionary
milves_initiat_returned_dict = milf_initiative_instance.pc_initiative()        

#instantiate the functions for enemies
#base enemy function
def base_enemies(base_init = 0, name = 'Base Enemy'):
    base_init_dict = {}
    base_init_dict[name] = np.random.randint(low=1,high=21)
    base_init_dict[name] = base_init_dict[name] + base_init
    
    #return base dict
    return base_init_dict

#mid-tier enemy function
def mid_tier_enemies(base_init = 0, name = 'Mid-Tier'):
    mid_init_dict = {}
    mid_init_dict[name] = np.random.randint(low=1, high = 21)
    mid_init_dict[name] = mid_init_dict[name] + base_init
    
    #return the mid-tier dict
    return mid_init_dict

#mini-boss function
def mini_boss_init(base_init = 0, name = 'Mini-Boss'):
    mini_boss_init_dict = {}
    mini_boss_init_dict[name] = np.random.randint(low=1, high = 21)
    mini_boss_init_dict[name] = mini_boss_init_dict[name] + base_init

    #return mini-boss dict
    return mini_boss_init_dict

#boss function
def boss_initiatives(base_init = 0, name = 'Boss'):
    boss_init_dict = {}
    boss_init_dict[name] = np.random.randint(low=1, high = 21)
    boss_init_dict[name] = boss_init_dict[name] + base_init
    
    #return dict
    return boss_init_dict


#get input for enemies initiatives
#base initiative
st.subheader('Enemy Type 1')
base_name = st.text_input('The name of Enemy Type 1 is:', value = 'Enemy Type 1')
base_init_mod = st.text_input("Enemy Type 1's Initiative Modifier", value='None'
)

#try to cast string to an integer
#if not integer, this enemy is not in combat
try:
    base_init_mod_int = int(base_init_mod)
    st.write(f'The modifier of enemy type 1 is {base_init_mod_int}.')
except:
    st.write('There are no type 1 enemies in combat.')
    base_init_mod_int = 'None'
    pass

st.text("")

#mid-tier initiative
st.subheader('Enemy Type 2')
mid_name = st.text_input('The name of Enemy Type 2 is:', value = 'Enemy Type 2')
mid_init_mod = st.text_input("Enemy Type 2's Initiative Modifier", value='None')

try:
    mid_init_mod_int = int(mid_init_mod)
    st.write(f'The modifier of the type 2 enemy is {mid_init_mod_int}.')
except:
    st.write('There are no type 2 enemies in combat.')
    mid_init_mod_int = 'None'
    pass

st.text("")

#mini-boss initiative
st.subheader('Enemy Type 3')
mini_boss_name = st.text_input ('The name of Enemy Type 3 is:', value = 'Enemy Type 3')
mini_boss_mod = st.text_input("Enemy Type 3's Initiative Modifier", value='None')
try:
    mini_boss_mod_int = int(mini_boss_mod)
    st.write(f'The modifier of enemy type 3 is {mini_boss_mod_int}.')
except:
    st.write('There are no type 3 enemies in combat.')
    mini_boss_mod_int = 'None'
    pass

st.text("")

#boss initiative
st.subheader('Enemy Type 4')
boss_name = st.text_input('The name of Enemy Type 4 is:', value = 'Enemy Type 4')
boss_mod = st.text_input("Enemy Type 4's Initiative Modifier", value='None')
try:
    boss_mod_int = int(boss_mod)
    st.write(f'The modifier of enemy type 4 is {boss_mod_int}.')
except:
    st.write('There are no type 4 enemies in combat.')
    boss_mod_int = 'None'
    pass

st.text("")
st.text("")

st.subheader('Initiatives:')
#load base enemy function
if isinstance(base_init_mod_int, int) and isinstance(base_name, str):
    bs_en_initiative = base_enemies(base_init = base_init_mod_int, name = base_name)
    milves_initiat_returned_dict.update(bs_en_initiative)

#load mid-tier enemy function
if isinstance(mid_init_mod_int, int) and isinstance(mid_name, str):
    mid_en_initiative = mid_tier_enemies(base_init = mid_init_mod_int, name = mid_name)
    milves_initiat_returned_dict.update(mid_en_initiative)
    

#load mini-boss enemy function
if isinstance(mini_boss_mod_int, int) and isinstance(mini_boss_name, str):
    min_boss_initiative = mini_boss_init(base_init = mini_boss_mod_int, name = mini_boss_name)
    milves_initiat_returned_dict.update(min_boss_initiative)

#load boss enemy function
if isinstance(boss_mod_int, int) and isinstance(boss_name, str):
    boss_init = boss_initiatives(base_init = boss_mod_int, name = boss_name)
    milves_initiat_returned_dict.update(boss_init)

#show the milf's and enemies initiatives in a single, sorted dataframe
milf_df = pd.DataFrame(milves_initiat_returned_dict, index = ['Initiatives']).T
milf_df = milf_df.sort_values(by = 'Initiatives', ascending = False)
st.dataframe(milf_df)
