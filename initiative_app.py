import pandas as pd
import numpy as np 
import streamlit as st
from streamlit import caching

#create the header for the app
st.header('Carus Campaign: Initiative Tracker')

#write some text to the app
st.write("This app will re-create initiative rolls for all PCs and NPCs at the end of a combat round.")


#load in the class for fortune seeker's
#always recreate PC initiatives on rerun
#default initiatives in self

#low value is inclusive, high value is exclusive in np.random.randint
#make the output of the class a dictionary to be used in dataframe creation

class FortuneSeekerInitiative:
    
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
    @st.cache(suppress_st_warning = True, allow_output_mutation = True)
    def pc_initiative(self):
        pc_init_dict = {}
        equation_dict = {}
        #name's of the PC's for dict keys
        pc_list = [self.alain_name, self.cass_name, self.wildhrt_name, self.idalia_name]
        for char in pc_list:
            pc_init_dict[char] = (np.random.randint(low=1, high = 21))
            
            #if statement to add in the modifier for each pc
            if char == 'Alain':
                equation_dict[char] = f' ({pc_init_dict[char]} + {self.alain_init})'
                pc_init_dict[char] = pc_init_dict[char] + self.alain_init
                
            elif char == 'Cassandra':
                equation_dict[char] = f' ({pc_init_dict[char]} + {self.cass_init})'
                pc_init_dict[char] = pc_init_dict[char] + self.cass_init
                
            elif char == 'Wildheart':
                equation_dict[char] = f'({pc_init_dict[char]} + {self.wildhrt_init})'
                pc_init_dict[char] = pc_init_dict[char] + self.wildhrt_init
                
            else:
                equation_dict[char] = f'({pc_init_dict[char]} + {self.idalia_init})'
                pc_init_dict[char] = pc_init_dict[char] + self.idalia_init
                

            
        #return the dictionary of names and initiatives    
        return pc_init_dict, equation_dict

#create class milfnitiative instance
fortune_inits = FortuneSeekerInitiative()
#return the milves initiatives in a dictionary
fortune_dict, pc_equation_dict = fortune_inits.pc_initiative()

#instantiate the functions for the different enemy types
#enemy 1 function
@st.cache(suppress_st_warning=True)
def enemy_one(base_init = 0, name = 'Enemy Type One'):
    enemy_one = {}
    equation_one = {}
    enemy_one[name] = np.random.randint(low=1,high=21)
    equation_one[name] = f'({enemy_one[name]} + {base_init})'
    enemy_one[name] = enemy_one[name] + base_init
    
    #return enemy one dictionary
    return enemy_one, equation_one

#enemy 2 function
@st.cache(suppress_st_warning=True)
def enemy_two(base_init = 0, name = 'Enemy Type Two'):
    enemy_two = {}
    equation_two = {}
    enemy_two[name] = np.random.randint(low=1, high = 21)
    equation_two[name] = f'({enemy_two[name]} + {base_init})'
    enemy_two[name] = enemy_two[name] + base_init
    
    #return enemy two dictionary
    return enemy_two, equation_two

#enemy 3 function
@st.cache(suppress_st_warning=True)
def enemy_three(base_init = 0, name = 'Enemy Type Three'):
    enemy_three = {}
    equation_three = {}
    enemy_three[name] = np.random.randint(low=1, high = 21)
    equation_three[name] = f'({enemy_three[name]} + {base_init})'
    enemy_three[name] = enemy_three[name] + base_init
    
    #return enemy three dictionary
    return enemy_three, equation_three

#enemy 4 function
@st.cache(suppress_st_warning=True)
def enemy_four(base_init = 0, name = 'Enemy Type Four'):
    enemy_four = {}
    equation_four = {}
    enemy_four[name] = np.random.randint(low=1, high = 21)
    equation_four[name] = f'({enemy_four[name]} + {base_init})'
    enemy_four[name] = enemy_four[name] + base_init
    
    #return enemy four dictionary
    return enemy_four, equation_four


#get input for enemies initiatives
st.subheader('Enemy Type 1')

#enemy 1 initiative and name input from user
enemy_one_name = st.text_input('The name of Enemy Type 1 is:', value = 'Enemy Type 1', key='enemy_1')
enemy_one_mod = st.text_input(f"{enemy_one_name}'s Initiative Modifier", value='None', key='enemy_1_mod')

#try to cast string to an integer
#if not integer, this enemy is not in combat currently
try:
    enemy_one_mod_int = int(enemy_one_mod)
    st.write(f"{enemy_one_name}'s initiative modifier is {enemy_one_mod_int}.")
except:
    st.write('There are no type 1 enemies in combat.')
    enemy_one_mod_int = 'None'
    pass

st.text("")

#enemy type 2 initiative
st.subheader('Enemy Type 2')
#enemy two initiative and name input from user
enemy_two_name = st.text_input('The name of Enemy Type 2 is:', value = 'Enemy Type 2', key='enemy_2')
enemy_two_mod = st.text_input(f"{enemy_two_name}'s Initiative Modifier", value='None', key='enemy_2_mod')

#try to cast string to an integer
#if not integer, this enemy is not in combat currently
try:
    enemy_two_mod_int = int(enemy_two_mod)
    st.write(f"{enemy_two_name}'s initiative modifier is {enemy_two_mod_int}.")
except:
    st.write('There are no type 2 enemies in combat.')
    enemy_two_mod_int = 'None'
    pass

st.text("")

#enemy type 3 initiative
st.subheader('Enemy Type 3')
#enemy three initiatve and name input from user
enemy_three_name = st.text_input ('The name of Enemy Type 3 is:', value = 'Enemy Type 3', key='enemy_3')
enemy_three_mod = st.text_input(f"{enemy_three_name}'s Initiative Modifier", value='None', key='enemy_3_mod')

#try to cast to an integer
#if not integer, this enemy is not in combat currently
try:
    enemy_three_mod_int = int(enemy_three_mod)
    st.write(f"{enemy_three_name}'s initiative modifier is {enemy_three_mod_int}.")
except:
    st.write('There are no type 3 enemies in combat.')
    enemy_three_mod_int = 'None'
    pass

st.text("")

#enemy type 4 initiative
st.subheader('Enemy Type 4')
#enemy four initiative and name input from user
enemy_four_name = st.text_input('The name of Enemy Type 4 is:', value = 'Enemy Type 4', key='enemy_4')
enemy_four_mod = st.text_input(f"{enemy_four_name}'s Initiative Modifier", value='None', key='enemy_4_mod')
try:
    enemy_four_mod_int = int(enemy_four_mod)
    st.write(f"{enemy_four_name}'s initiative modifier is {enemy_four_mod_int}.")
except:
    st.write('There are no type 4 enemies in combat.')
    enemy_four_mod_int = 'None'
    pass

st.text("")
st.text("")

st.subheader('Initiatives:')
#load enemy type 1 function if the modifier could be cast to an integer and the name is a string
if isinstance(enemy_one_mod_int, int) and isinstance(enemy_one_name, str) and len(enemy_one_name)>0:
    enemy_one_init, eq_one = enemy_one(base_init = enemy_one_mod_int, name = enemy_one_name)
    fortune_dict.update(enemy_one_init)
    pc_equation_dict.update(eq_one)

#load enemy type 2 function if the modifier could be cast to an integer and the name is a string
if isinstance(enemy_two_mod_int, int) and isinstance(enemy_two_name, str) and len(enemy_two_name)>0:
    enemy_two_init, eq_two = enemy_two(base_init = enemy_two_mod_int, name = enemy_two_name)
    fortune_dict.update(enemy_two_init)
    pc_equation_dict.update(eq_two)

#load enemy type 3 function if the modifier could be cast to an integer and the name is a string
if isinstance(enemy_three_mod_int, int) and isinstance(enemy_three_name, str) and len(enemy_three_name)>0:
    enemy_three_init, eq_three = enemy_three(base_init = enemy_three_mod_int, name = enemy_three_name)
    fortune_dict.update(enemy_three_init)
    pc_equation_dict.update(eq_three)

#load enemy type 4 function if the modifier could be cast to an integer and the name is a string
if isinstance(enemy_four_mod_int, int) and isinstance(enemy_four_name, str) and len(enemy_four_name)>0:
    enemy_four_init, eq_four = enemy_four(base_init = enemy_four_mod_int, name = enemy_four_name)
    fortune_dict.update(enemy_four_init)
    pc_equation_dict.update(eq_four)

#show the fortune seeker's initiatives and enemies initiatives in a single, sorted dataframe
fortune_df = pd.DataFrame([fortune_dict, pc_equation_dict], index = ['Initiatives', 'Equation']).T
fortune_df = fortune_df.sort_values(by = 'Initiatives', ascending = False)
st.dataframe(fortune_df)


#create a button for rerunning the clearing the cache & then re-running the python script

st.text("")
st.text("")
if st.button('Clear Cache & Re-Roll'):
    #clear the cache
    caching.clear_cache()
    #rerun the streamlit script from the top
    st.experimental_rerun() 