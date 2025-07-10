print("""
  ,----..      ,---,.   ,---,       .--.--.       ,---,.,-.----.   
 /   /   \   ,'  .' |  '  .' \     /  /    '.   ,'  .' |\    /  \  
|   :     :,---.'   | /  ;    '.  |  :  /`. / ,---.'   |;   :    \ 
.   |  ;. /|   |   .':  :       \ ;  |  |--`  |   |   .'|   | .\ : 
.   ; /--` :   :  |-,:  |   /\   \|  :  ;_    :   :  |-,.   : |: | 
;   | ;    :   |  ;/||  :  ' ;.   :\  \    `. :   |  ;/||   |  \ : 
|   : |    |   :   .'|  |  ;/  \   \`----.   \|   :   .'|   : .  / 
.   | '___ |   |  |-,'  :  | \  \ ,'__ \  \  ||   |  |-,;   | |  \ 
'   ; : .'|'   :  ;/||  |  '  '--' /  /`--'  /'   :  ;/||   | ;\  |
'   | '/  :|   |    \|  :  :      '--'.     / |   |    \:   ' | \.'
|   :    / |   :   .'|  | ,'        `--'---'  |   :   .':   : :-'  
 \   \ .'  |   | ,'  `--''                    |   | ,'  |   |.'    
  `---`    `----'  ,-.----.           ,--,    `----'    `---'      
  ,----..     ,---,\    /  \        ,--.'|    ,---,.,-.----.       
 /   /   \ ,`--.' ||   :    \    ,--,  | :  ,'  .' |\    /  \      
|   :     :|   :  :|   |  .\ :,---.'|  : ',---.'   |;   :    \     
.   |  ;. /:   |  '.   :  |: ||   | : _' ||   |   .'|   | .\ :     
.   ; /--` |   :  ||   |   \ ::   : |.'  |:   :  |-,.   : |: |     
;   | ;    '   '  ;|   : .   /|   ' '  ; ::   |  ;/||   |  \ :     
|   : |    |   |  |;   | |`-' '   |  .'. ||   :   .'|   : .  /     
.   | '___ '   :  ;|   | ;    |   | :  | '|   |  |-,;   | |  \     
'   ; : .'||   |  ':   ' |    '   : |  : ;'   :  ;/||   | ;\  \    
'   | '/  :'   :  |:   : :    |   | '  ,/ |   |    \:   ' | \.'    
|   :    / ;   |.' |   | :    ;   : ;--'  |   :   .':   : :-'      
 \   \ .'  '---'   `---'.|    |   ,/      |   | ,'  |   |.'        
  `---`              `---`    '---'       `----'    `---'          """)

def ceaser(start_text,shift_amount,cipher_direction):
  end_text = ""
  if(cipher_direction=="decode"):
    shift_amount*=-1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount)%len(alphabet)
      end_text += alphabet[new_position]
    else:
      end_text+= char
  print(f"The {cipher_direction}d text is {end_text}")
should_continue = True
while should_continue:
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  direction = input("Type 'encode' to encript , Type 'decode' to decript : \n")
  text = input("Type your message : ").lower()
  shift = int(input("Type the Shift number : "))
  shift =shift % 26  
  ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
  restart = input("Type 'yes' if you want to continue or Type 'no' if you want to stop.\n").lower()
  if(restart == "no"):
    should_continue= False
    print("GOOD BYE👋")
